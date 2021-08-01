from tkinter import *

def main():
    root = Tk()
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
    midFrame = Frame(root, bg="white")
    midFrame.pack(fill=X)

    # Key of table
    midKeyTable = Label(midFrame, text="Type")
    midKeyTable.grid(row=0, column=0)
    midKeyTable = Label(midFrame, text="Name")
    midKeyTable.grid(row=0, column=1)
    midKeyTable = Label(midFrame, text="State")
    midKeyTable.grid(row=0, column=2)
    midKeyTable = Label(midFrame, text="Git Status")
    midKeyTable.grid(row=0, column=3)

    midKeyTable = Label(midFrame, text="Saves:")
    midKeyTable.grid(row=1, column=0)

    # function to fill in save data

    midKeyTable = Label(midFrame, text="SMH:")
    midKeyTable.grid(row=2, column=0)

    # function to fill in smh data




    root.mainloop()


if __name__ == '__main__':
    main()
