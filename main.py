#!/usr/bin/env python3

# Written by Brel00m

"""
This is the main script that will run in the compiled version
of this program. It should handle creating any prerequisite
files and folders necessary for the operation of the program.

It should also handle running all the other dependencies easier.
"""

import GmodRepo
from GUI import GUI
import os
import tkinter as tk


def read_config():
    with open("config.txt") as fd:
        lines = fd.readlines()

    config = [] # For if there are more config vars in future

    for line in lines:
        line = line.split()
        if line[0] == "Gmod_Location":
            Gmod_Location = " ".join(line[2:]).strip()
            print("Gmod Location:", Gmod_Location)

    return Gmod_Location
    # return config


def main():
    if not os.path.exists("Projects"):
        os.makedirs("Projects")

    config = read_config()

    app = GUI(config)
    app.mainloop()


if __name__ == '__main__':
    main()
