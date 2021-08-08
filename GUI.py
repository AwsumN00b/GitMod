#!/usr/bin/env python3

# Written by Brel00m

from tkinter import *
from GmodRepo import GmodRepo
import os, subprocess



class Add(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.title("Add New Repo")

        self.build()
        self.center_window()


    def center_window(self):
            windowWidth = self.winfo_reqwidth()
            windowHeight = self.winfo_reqheight()

            posRight = int(self.winfo_screenwidth() / 2 - windowWidth / 2)
            posDown = int(self.winfo_screenheight() / 2 - windowHeight / 2)

            self.geometry("+{}+{}".format(posRight, posDown))


    def get_repo_name_from_url(self, url):
        last_slash_index = url.rfind("/")
        last_suffix_index = url.rfind(".git")
        if last_suffix_index < 0:
            last_suffix_index = len(url)

        if last_slash_index < 0 or last_suffix_index <= last_slash_index:
            return False

        return url[last_slash_index + 1:last_suffix_index]


    def create_new_repo(self, name):
    # tries to check if repo is Link or just a filename
    # Then clones or inits a repo

        url_repo = self.get_repo_name_from_url(name)
        if url_repo:
            # when name is a Git url
            subprocess.run(["git", "clone", name, "Projects"])
            self.parent.all_repos[url_repo] = GmodRepo(url_repo)
        else:
            # create local-only repo
            subprocess.run(["git", "init", "Projects\\" + name])
            self.parent.all_repos[name] = GmodRepo(name)

        self.parent.all_repos[name].initial_commit()
        self.parent.update_repoListFrame(self.parent.repoListFrame)
        self.parent.update_current_repo(name)


    def build(self):
        # This is the window for adding a new repo
        self.geometry("400x75")
        self.overrideredirect(1)

        new_repo_name = StringVar().set("")

        add_instructions = Label(self,
        text="Name/Github Link for your repo:")
        add_instructions.pack()

        add_frame = Frame(self,
            bg="lavender")
        add_frame.pack(fill=X)

        textbox = Entry(add_frame,
            font=("Helvetica", 14), bg="white")
        textbox.pack(fill=X)

        btn_add = Button(add_frame, text="Add Repo!",
            command=lambda: self.create_new_repo(textbox.get()))
        btn_add.pack(side=RIGHT)

        btn_close = Button(add_frame, text="Close",
            command=lambda: self.destroy())
        btn_close.pack(side=LEFT)



class GUI(Tk):

    def __init__(self):
        super().__init__()
        self.title("GitMod")

        try:
            self.iconbitmap(default="GitMod.ico")
        except:
            pass

        self.all_repos = None
        self.update_local_repos()
        self.current_open_repo = None
        self.stringvar_current_open_repo = StringVar().set("None")

        self.buildGUI()
        self.center_window()


    def center_window(self):
        windowWidth = self.winfo_reqwidth()
        windowHeight = self.winfo_reqheight()

        posRight = int(self.winfo_screenwidth() / 2 - windowWidth / 2)
        posDown = int(self.winfo_screenheight() / 2 - windowHeight / 2)

        self.geometry("+{}+{}".format(posRight, posDown))


    def update_current_repo(self, s_repo):
        if s_repo in self.all_repos.values():
            self.stringvar_current_open_repo.set(s_repo)
            self.current_open_repo = self.all_repos[s_repo]


    def update_local_repos(self):
        dict_repos = {}
        for repo in os.listdir("Projects"):
            dict_repos[repo] = GmodRepo(repo)

        self.all_repos = dict_repos


    def update_repoListFrame(self, frame):
        frame.pack_forget()

        self.update_local_repos()
        build_repoListFrame(frame)


    def build_repoListFrame(self):
        # Tall, not very wide box aligned to left of screen
        # Lists all local repos vertically
        repoListFrame = Frame(self, bg="white")
        repoListFrame.pack(side=LEFT, fill=Y)

        # generates list of local repos
        selected_repo = StringVar()
        selected_repo.set("None")

        self.update_local_repos()
        for repo in self.all_repos:
            repo_RadioButton = Radiobutton(repoListFrame,
                text=repo, variable=selected_repo, value=repo,
                bg="thistle1")
            repo_RadioButton.pack()


    def build_topFrame(self):
        # Long bar along top of window
        topFrame = Frame(self, bg="white")
        topFrame.pack(fill=X)

        label_repo = Label(topFrame,
            text="Current Repo: ")
        label_repo.pack(side=LEFT)

        label_repo_name = Label(topFrame,
            textvariable=self.stringvar_current_open_repo)
        label_repo_name.pack(side=LEFT)

        button_add = Button(topFrame,
            text="Add", bg="lavender")
        button_add.bind("<Button>",
            lambda x: Add(self))
        button_add.pack(side=RIGHT)

        button_refresh = Button(topFrame,
            text="Refresh", bg="coral3")
        button_refresh.pack(side=RIGHT)


    def build_midBoxFrame(self):
        # Big Box in middle of page
        midBoxFrame = Frame(self, bg="white")
        midBoxFrame.pack(fill=X)

        # Key of table
        midKeyTable = Label(midBoxFrame,
            text="Type")
        midKeyTable.grid(row=0, column=0)

        midKeyTable = Label(midBoxFrame,
            text="Name")
        midKeyTable.grid(row=0, column=1)

        midKeyTable = Label(midBoxFrame,
            text="State")
        midKeyTable.grid(row=0, column=2)

        midKeyTable = Label(midBoxFrame,
            text="Git Status")
        midKeyTable.grid(row=0, column=3)

        # Section to display save files
        midKeyTable = Label(midBoxFrame, text="Saves:")
        midKeyTable.grid(row=1, column=0)

        # add function to fill in save data

        # Section to display SMH files
        midKeyTable = Label(midBoxFrame, text="SMH:")
        midKeyTable.grid(row=2, column=0)

        # add function to fill in smh data


    def build_midLongFrame(self):
        # Long bar across middle section of window
        midLongFrame = Frame(self, bg="gray80")
        midLongFrame.pack(fill=X)

        # Buttons inside midLongFrame
        button_extract = Button(midLongFrame,
            text="Extract", bg="sky blue")
        button_extract.pack(side=LEFT)

        button_inject = Button(midLongFrame,
            text="Inject", bg="PaleGreen1")
        button_inject.pack(side=RIGHT)


    def build_bottomRightFrame(self):
        # Long Frame along bottom right side of window for Buttons
        bottomRightFrame = Frame(self, bg="white")
        bottomRightFrame.pack(side=RIGHT)

        # Buttons inside bottomBoxFrame
        button_commit = Button(bottomRightFrame,
            text="Commit", bg="steel blue")
        button_commit.pack()

        button_push = Button(bottomRightFrame,
            text="Push", bg="gold2")
        button_push.pack(fill=X)

        button_pull = Button(bottomRightFrame,
            text="Pull", bg="plum3")
        button_pull.pack(fill=X)


    def build_bottomBoxFrame(self):
        # Box along bottom of screen
        bottomBoxFrame = Frame(self, bg="white")


    def buildGUI(self):
        # Runs all the self.build_X() commands
        # They should be run in the order they are written
        self.build_repoListFrame()
        self.build_topFrame()
        self.build_midBoxFrame()
        self.build_midLongFrame()
        self.build_bottomRightFrame()
        self.build_bottomBoxFrame()
