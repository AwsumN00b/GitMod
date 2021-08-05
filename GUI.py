#!/usr/bin/env python3

# Written by Brel00m

from tkinter import *
import os
from GmodRepo import GmodRepo


def addTopLevel(root):
    # This is the window for adding a new repo

    repo_name = StringVar().set("")

    addRoot = Toplevel(root)
    addRoot.title("Add new repo")

    add_instructions = Label(addRoot, text="Name/Github Link for your repo:")
    add_instructions.pack()

    add_frame = Frame(addRoot, bg="lavender")
    add_frame.pack(fill=X)

    textbox = Entry(add_frame, textvariable=repo_name, bg="white")
    textbox.pack(fill=X)

    btn = Button(add_frame, text="Add Repo!",
                command=lambda)
    btn.pack(side=RIGHT)



def buildGUI():
    root = Tk()

    try:
        root.iconbitmap(default="GitMod.ico")
    except:
        pass

    root.title("GitMod")


    # Tall, not very wide box aligned to left of screen
    # Lists all local repos vertically
    repolistFrame = Frame(root)
    repolistFrame.pack(fill=Y, side=LEFT)

    # display checklist of local repos
    selected_repo = StringVar()
    for repo in os.listdir("Projects"):
        repo_RadioButton = Radiobutton(repolistFrame, text=repo,
                                        variable=selected_repo, value=repo, bg="thistle1")
        repo_RadioButton.pack()


    # Long bar along top of window
    topFrame = Frame(root, bg="white")
    topFrame.pack(fill=X)

    label_repo = Label(topFrame, text="Current Repo: ")
    label_repo.pack(side=LEFT)

    current_repo_name = StringVar()
    current_repo_name.set("None")
    label_repo_name = Label(topFrame, text=current_repo_name)
    label_repo_name.pack(side=LEFT)

    button_add = Button(topFrame, text="Add", bg="lavender",
                command=lambda: addTopLevel(root))
    button_add.pack(side=RIGHT)

    button_refresh = Button(topFrame, text="Refresh", bg="coral3")
    button_refresh.pack(side=RIGHT)


    # Big Box in middle of page
    midBoxFrame = Frame(root, bg="white")
    midBoxFrame.pack(fill=X)

    # Key of table
    midKeyTable = Label(midBoxFrame, text="Type")
    midKeyTable.grid(row=0, column=0)
    midKeyTable = Label(midBoxFrame, text="Name")
    midKeyTable.grid(row=0, column=1)
    midKeyTable = Label(midBoxFrame, text="State")
    midKeyTable.grid(row=0, column=2)
    midKeyTable = Label(midBoxFrame, text="Git Status")
    midKeyTable.grid(row=0, column=3)

    midKeyTable = Label(midBoxFrame, text="Saves:")
    midKeyTable.grid(row=1, column=0)

    # add function to fill in save data

    midKeyTable = Label(midBoxFrame, text="SMH:")
    midKeyTable.grid(row=2, column=0)

    # add function to fill in smh data


    # Long bar across middle section of window
    midLongFrame = Frame(root, bg="gray80")
    midLongFrame.pack(fill=X)

    # Buttons inside midLongFrame
    button_extract = Button(midLongFrame, text="Extract", bg="sky blue")
    button_extract.pack(side=LEFT)

    button_inject = Button(midLongFrame, text="Inject", bg="PaleGreen1")
    button_inject.pack(side=RIGHT)


    # Long Frame along bottom right side of window for Buttons
    bottomRightFrame = Frame(root, bg="white")
    bottomRightFrame.pack(side=RIGHT)

    # Buttons inside bottomBoxFrame
    button_commit = Button(bottomRightFrame, text="Commit", bg="steel blue")
    button_commit.pack()

    button_push = Button(bottomRightFrame, text="Push", bg="gold2")
    button_push.pack(fill=X)

    button_pull = Button(bottomRightFrame, text="Pull", bg="plum3")
    button_pull.pack(fill=X)


    # Box along bottom of screen
    bottomBoxFrame = Frame(root, bg="white")


    root.mainloop()


if __name__ == '__main__':
    buildGUI()
