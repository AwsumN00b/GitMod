#!/usr/bin/env python3

# Written by Brel00m

"""
This is the main script that will run in the compiled version
of this program. It should handle creating any prerequisite
files and folders necessary for the operation of the program.

It should also handle running all the other dependencies easier.
"""

import config
import GmodRepo
import GUI
import os



def main():

    if not os.path.exists("Projects"):
        os.makedirs("Projects")

    GUI.main()




if __name__ == '__main__':
    main()
