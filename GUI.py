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
            subprocess.run(["git", "clone", name, "Projects\\" + url_repo])
            self.parent.all_repos.append(GmodRepo(url_repo))
            name = url_repo
        else:
            # create local-only repo
            subprocess.run(["git", "init", "Projects\\" + name])
            self.parent.all_repos.append(GmodRepo(name))

        self.parent.all_repos[-1].initiate()
        self.destroy()
        self.parent.refresh()


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



class Include(Toplevel):
    def __init__(self, parent, mode):
        super().__init__(parent)
        self.parent = parent

        self.title("Add files to this repo")

        if self.parent.current_open_repo is None:
            self.parent.raise_error("You need to select a repo first!")
            self.destroy()
        else:
            self.build(mode)
            self.center_window()


    def confirm_include(self, files, filetype):
        dub = [file for file in files.keys() if files[file].get() == 1]
        print(dub)
        self.parent.current_open_repo.dub_files(filetype, dub)


    def center_window(self):
            windowWidth = self.winfo_reqwidth()
            windowHeight = self.winfo_reqheight()

            posRight = int(self.winfo_screenwidth() / 2 - windowWidth / 2)
            posDown = int(self.winfo_screenheight() / 2 - windowHeight / 2)

            self.geometry("+{}+{}".format(posRight, posDown))


    def build(self, mode):
        # Window for choosing files to include as part of this project
        # Chosen files get their filename's changed

        topMenuFrame = Frame(self,
            bg="gray80")
        topMenuFrame.pack(fill=X)

        button_close = Button(topMenuFrame, text="Close",
            command=lambda: self.destroy())
        button_close.pack(side=RIGHT)

        button_confirm = Button(topMenuFrame,
            text="Confirm", bg="royal blue",
            command=lambda: self.confirm_include(files, mode))
        button_confirm.pack(side=LEFT)

        if mode == "saves":
            files = {file: IntVar() for file in self.parent.current_open_repo.pick_files("saves")}
        elif mode == "smh":
            files = {file: IntVar() for file in self.parent.current_open_repo.pick_files("smh")}

        # Scrollbar for the long checkbox
        scrollFrame = Frame(self)
        scrollFrame.pack(fill=BOTH)

        cbox_canvas = Canvas(scrollFrame)
        cbox_canvas.pack(side=LEFT, fill=BOTH)

        cbox_scrollbar = Scrollbar(scrollFrame, orient=VERTICAL,
            command=cbox_canvas.yview)
        cbox_scrollbar.pack(side=RIGHT, fill=Y, anchor="e")

        cbox_canvas.configure(yscrollcommand=cbox_scrollbar.set)
        cbox_canvas.bind("<Configure>",
            lambda e: cbox_canvas.configure(scrollregion=cbox_canvas.bbox("all")))

        cboxFrame = Frame(cbox_canvas)

        for i, file in enumerate(files.keys()):
            checkBox_file = Checkbutton(cboxFrame,
                text=file, variable=files[file], anchor="w",
                width=60)
            checkBox_file.pack(anchor="w")

        cbox_canvas.create_window((0,0), window=cboxFrame, anchor="nw")




class GUI(Tk):

    def __init__(self):
        super().__init__()
        self.title("GitMod")
        self.geometry("600x300")

        try:
            self.iconbitmap(default="GitMod.ico")
        except:
            pass

        self.all_repos = None
        self.update_local_repos()
        self.current_open_repo = None
        self.stringvar_current_open_repo = StringVar()
        self.stringvar_current_open_repo.set("None")
        self.stringvar_errormsg = StringVar()
        self.stringvar_errormsg.set("")

        self.buildGUI()
        self.center_window()


    def center_window(self):
        windowWidth = self.winfo_reqwidth()
        windowHeight = self.winfo_reqheight()

        posRight = int(self.winfo_screenwidth() / 2 - windowWidth / 2)
        posDown = int(self.winfo_screenheight() / 2 - windowHeight / 2)

        self.geometry("+{}+{}".format(posRight, posDown))


    def update_current_repo(self, s_repo):
        self.current_open_repo = self.all_repos[s_repo]
        self.stringvar_current_open_repo.set(self.current_open_repo.name)


    def update_local_repos(self):
        list_repos = []
        for repo in os.listdir("Projects"):
            list_repos.append(GmodRepo(repo))

        self.all_repos = list_repos


    def raise_error(self, errormsg):
        self.stringvar_errormsg.set(errormsg)


    def list_all_windows(self):
        _list = self.winfo_children()

        for item in _list:
            if item.winfo_children():
                _list.extend(item.winfo_children())

        return _list


    def extract(self):
        if self.current_open_repo is None:
            self.raise_error("You need to select a repo first!")
        else:
            self.current_open_repo.initiate()
            self.current_open_repo.extract_smh()
            self.current_open_repo.extract_save()
            self.refresh()


    def refresh(self):
        widget_list = self.list_all_windows()
        for item in widget_list:
            try:
                item.pack_forget()
            except AttributeError:
                item.destroy()

        self.buildGUI()


    def build_repoListFrame(self):
        # Tall, not very wide box aligned to left of screen
        # Lists all local repos vertically
        v = IntVar()

        repoListFrame = Frame(self, bg="thistle1")
        repoListFrame.pack(side=LEFT, fill=Y)

        # generates list of local repos
        self.update_local_repos()
        for i, repo in enumerate(self.all_repos):
            repo_RadioButton = Radiobutton(repoListFrame,
                text=repo.name, value=i, variable=v,
                indicatoron=0, bg="thistle1", anchor="w",
                command=lambda: self.update_current_repo(v.get()))
            repo_RadioButton.pack(fill="both")


    def build_topFrame(self):
        # Long bar along top of window
        topFrame = Frame(self, bg="white")
        topFrame.pack(fill=X)

        button_add = Button(topFrame,
            text="Add", bg="lavender")
        button_add.bind("<Button>",
            lambda x: Add(self))
        button_add.pack(side=RIGHT)

        button_refresh = Button(topFrame,
            text="Refresh", bg="coral3")
        button_refresh.bind("<Button>",
            lambda x: self.refresh())
        button_refresh.pack(side=LEFT)

        label_repo = Label(topFrame,
        text="Current Repo: ")
        label_repo.pack(side=LEFT)

        label_repo_name = Label(topFrame,
        textvariable=self.stringvar_current_open_repo)
        label_repo_name.pack(side=LEFT)


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

#        midKeyTable = Label(midBoxFrame,
#            text="State")
#        midKeyTable.grid(row=0, column=2)

#        midKeyTable = Label(midBoxFrame,
#            text="Git Status")
#        midKeyTable.grid(row=0, column=3)

        grid_row_len = 1
        if self.current_open_repo is not None:
            midKeyTable = Label(midBoxFrame, text="Saves:")
            midKeyTable.grid(row=1, column=0)

            for i, save_files in enumerate(self.current_open_repo.list_save_files()):
                saveKeyTable = Label(midBoxFrame,
                    text=save_files)
                saveKeyTable.grid(row=i+2, column=1, sticky="w")
                grid_row_len = i + 3

            # Section to display SMH files
            midKeyTable = Label(midBoxFrame, text="SMH:")
            midKeyTable.grid(row=grid_row_len, column=0, sticky="w")

            grid_row_len += 1

            for i, smh_files in enumerate(self.current_open_repo.list_smh_files()):
                smhKeyTable = Label(midBoxFrame,
                    text=smh_files)
                smhKeyTable.grid(row=grid_row_len+i+1, column=1, sticky="w")


    def build_midLongFrame(self):
        # Long bar across middle section of window
        midLongFrame = Frame(self, bg="gray80")
        midLongFrame.pack(fill=X)

        # Buttons inside midLongFrame
        button_include_saves = Button(midLongFrame,
            text="Include Saves", bg="royal blue",
            command=lambda: Include(self, "saves"))
        button_include_saves.pack(side=LEFT)

        button_include_smh = Button(midLongFrame,
            text="Include SMH", bg="royal blue",
            command=lambda: Include(self, "smh"))
        button_include_smh.pack(side=LEFT)

        button_extract = Button(midLongFrame,
            text="Extract", bg="sky blue",
            command=lambda: self.extract())
        button_extract.pack(side=LEFT)

        label_error = Label(midLongFrame,
            textvariable=self.stringvar_errormsg, fg="red", bg="gray80")
        label_error.pack(side=LEFT)

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
        try:
            self.stringvar_errormsg.set("")
        except:
            pass

        self.build_repoListFrame()
        self.build_topFrame()
        self.build_midBoxFrame()
        self.build_midLongFrame()
        self.build_bottomRightFrame()
        self.build_bottomBoxFrame()
