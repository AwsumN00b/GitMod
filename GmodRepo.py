#!/usr/bin/env python3

# Written by Brel00m

import os, shutil, subprocess
from config import Gmod_Location as gmod


class GmodRepo():

    def __init__(self, repo_name):
        """
Constructor for a gmod repo object.
"""
        self.name = repo_name
        self.dir = "Projects\\" + repo_name


    def initiate(self):
        """
Checks if Saves and SMH folder exist.
If they dont, they will be created.
"""
        if not os.path.exists(self.dir + "Saves"):
            os.makedirs(self.dir + "\\Saves")
        if not os.path.exists(self.dir + "SMH"):
            os.makedirs(self.dir + "\\SMH")


    def requirements_checker(self):
        """
Kicks the user out if they havent properly added their gmod install directory.
Also checks if Git is installed
"""
        if not os.path.exists(gmod):
            print("Please add your Gmod directory path to config.py before continuing")
            exit()

        try:
            subprocess.run(["git", "--version"])
        except:
            print("Git is not installed correctly, please do this before continuing")
            exit()


    def pick_files(self, path, filetype):
        """
Lists out all files within a given path, and is of a certain filetype.
Then prompts user to pick out each file they wish to select.
"""
        files = os.listdir(path)
        files = [file for file in files if filetype in file and file.startswith(self.name + "_")]

        return files


    def dub_files(self, filetype):
        """
Used to rename files within Gmod to have the current repo's name as a prefix.
GmodRepo utilises these prefixes to know what files are meant to be a part of itself.
"""

        # Get correct file path for each file type
        if filetype == "smh":
            path = gmod + r"\garrysmod\data\smh"
            endw = ".txt"
        elif filetype == "saves":
            path = gmod + r"\garrysmod\saves"
            endw = ".gms"

        files = os.listdir(path)
        files = [file for file in files if not file.startswith(self.name + "_") and file.endswith(endw)]
        print_columns(files)
        print("Type the numbers of files you wish to add (You can type multiple): ")
        adding_files = [int(i) for i in input().split() if i.isdigit()]

        for num in adding_files:
            if num > len(files):
                file_src = path + "\\" + files[num]
                file_dst = path + "\\" + self.name + "_" + files[num]
                os.rename(file_src, file_dst)
            else:
                print(f"File number {num} does not exist.")

        print("Files renamed within Gmod!")


    def extract_smh(self):
        """
Takes smh files that have this repo's name as a suffix and copies them over to the git repo.
"""
        files = self.pick_files(gmod + r"\garrysmod\data\smh", ".txt")

        file_source = gmod + r"\garrysmod\data\smh\\"
        file_target = "Projects\\" + self.name + "\\smh\\"

        for file in files:
            shutil.copy(file_source + file, file_target + file)

        self.add_all()


    def extract_save(self):
        """
Takes .gms files and their thumbnail that from Gmod and copies them to the repo
"""
        saves = self.pick_files(gmod + r"\garrysmod\saves", ".gms")
        icons = self.pick_files(gmod + r"\garrysmod\saves", ".jpg")

        file_source = gmod + r"\garrysmod\saves\\"
        file_target = "Projects\\" + self.name + "\\saves"

        for file in saves:
            shutil.copy(file_source + file, file_target)
        for file in icons: # taking the save thumbnails into the repo too
            shutil.copy(file_source + file, file_target)

        self.add_all()


    def inject(self):
        """
Takes the files in the repo and copies them into Gmod.
"""
        smh_dir = "Projects\\" + self.name + "\\smh\\"
        save_dir = "Projects\\" + self.name + "\\saves\\"

        smh_gmod = gmod + r"\garrysmod\data\smh\\"
        save_gmod = gmod + r"\garrysmod\saves\\"

        files = self.pick_files(smh_dir, ".txt")
        for file in files:
            shutil.copy(smh_dir + file, smh_gmod)

        files = self.pick_files(save_dir, ".txt")
        for file in files:
            shutil.copy(save_dir + file, save_gmod)
            file = file[:-4] + ".jpg"  # For copying the save thumbnail too
            shutil.copy(save_dir + file, save_gmod)


    def push(self):
        """
Pushes the repo's commits back to it's Remote, which in most cases is likely going to be a GitHub repo.
"""
        origin = self.repo.remote("origin")
        origin.push()

        subprocess.run("git", "--git-dir=" + self.dir, "push")


    def fetch(self):
        """
Retrieves the latest commits from the Remote repo, which is likely a GitHub repo.
"""

        subprocess.run("git", "--git-dir=" + self.dir, "pull")


    def commit(self, commit_desc):
        """
Take all extracted files and save them as a commit, takes a commit description as an argument.
"""
        self.add_all()
        subprocess.run(["git", "--git-dir=" + self.dir, "commit", "-m", commit_desc])


    def add_all(self):
        """
Adds all newly copied files to the repo tree so that they can be committed.
"""
        subprocess.run(["git", "--git-dir=" + self.dir + "\\.git", "add", "--all"])


    def list_smh_files(self):
        """
Returns a list of all smh files in the directory of the repo
"""
        try:
            smh_files = os.listdir(self.dir + r"\SMH")
        except FileNotFoundError:
            smh_files = []

        return smh_files


    def list_save_files(self):
        """
Returns a list of all save filels in the directory of the repo
"""
        try:
            save_files = os.listdir(self.dir + r"\Saves")
        except FileNotFoundError:
            save_files = []

        return save_files
