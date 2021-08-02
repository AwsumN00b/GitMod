from tkinter import *

def main():
    root = Tk()
    root.iconbitmap("GitMod.ico")
    root.title("GitMod")


    # Tall, not very wide box aligned to left of screen
    # Lists all local repos vertically
    repolistFrame = Frame(root, bg="blue")
    repolistFrame.pack(fill=Y, side=LEFT)

    button_open = Button(repolistFrame, text="Open", fg="BLUE")
    button_open.grid(row=0, column=0)

    # Placeholder list of objects to show size
    for i in range(1, 7):
        label_placeholder = Label(repolistFrame, text="Kamiflage")
        label_placeholder.grid(row=i)


    # Long bar along top of window
    topFrame = Frame(root, bg="white")
    topFrame.pack(fill=X)

    label_placeholder = Label(topFrame, text="Current Repo: Magic Gay")
    label_placeholder.pack(side=LEFT)

    button_add = Button(topFrame, text="Add", fg="YELLOW")
    button_add.pack(side=RIGHT)

    button_refresh = Button(topFrame, text="Refresh", fg="RED")
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
    main()
