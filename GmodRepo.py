#!/usr/bin/env python3

# Written by Brel00m

import os, shutil, subprocess


class GmodRepo():

    def __init__(self, repo_name, gmod, dir):
        """
Constructor for a gmod repo object.
"""
        self.name = repo_name
        self.dir = dir + "\\Projects\\" + repo_name
        self.gmod = gmod


    def initiate(self):
        """
Checks if Saves and SMH folder exist.
If they dont, they will be created.
"""
        if not os.path.exists(self.dir + "\\Saves"):
            os.makedirs(self.dir + "\\Saves")
        if not os.path.exists(self.dir + "\\SMH"):
            os.makedirs(self.dir + "\\SMH")


    def pick_files(self, filetype):
        """
Lists out all files within a given path, and is of a certain filetype.
"""
        if filetype == "smh":
            path = self.gmod + r"\garrysmod\data\smh"
            endw = ".txt"
        elif filetype == "saves":
            path = self.gmod + r"\garrysmod\saves"
            endw = ".gms"
        elif filetype == "jpeg":
            path = self.gmod + r"\garrysmod\saves"
            endw = ".jpg"

        files_desired = []
        for file in os.listdir(path):
            if endw in file:
                files_desired.append(file)

        # files_desired.sort(key=os.path.getctime)

        return files_desired


    def dub_files(self, filetype, file_list):
        """
Used to rename files within Gmod to have the current repo's name as a prefix.
GmodRepo utilises these prefixes to know what files are meant to be a part of itself.
"""

        # Get correct file path for each file type
        if filetype == "smh":
            path = self.gmod + r"\garrysmod\data\smh"
            endw = ".txt"
        elif filetype == "saves":
            path = self.gmod + r"\garrysmod\saves"
            endw = ".gms"

        for file in file_list:
            file_src = path + "\\" + file
            file_dst = path + "\\" + self.name + "_" + file
            os.rename(file_src, file_dst)


    def extract_smh(self):
        """
Takes smh files that have this repo's name as a suffix and copies them over to the git repo.
"""
        files = self.pick_files("smh")

        file_source = self.gmod + "\\garrysmod\\data\\smh\\"
        file_target = self.dir + "\\smh\\"

        for file in files:
            if file.startswith(self.name):
                shutil.copy(file_source + file, file_target + file)

        self.add_all()


    def extract_save(self):
        """
Takes .gms files and their thumbnail that from Gmod and copies them to the repo
"""
        saves = self.pick_files("saves")
        icons = self.pick_files("jpeg")

        file_source = self.gmod + "\\garrysmod\\saves\\"
        file_target = self.dir + "\\Saves\\"

        for file in saves:
            if file.startswith(self.name):
                shutil.copy(file_source + file, file_target)
        for file in icons: # taking the save thumbnails into the repo too
            if file.startswith(self.name):
                shutil.copy(file_source + file, file_target)

        self.add_all()


    def inject(self):
        """
Takes the files in the repo and copies them into Gmod.
"""
        smh_dir = self.dir + "\\SMH\\"
        save_dir = self.dir + "\\Saves\\"

        if os.path.exists(smh_dir):
            for file in os.listdir(smh_dir):
                shutil.copy(smh_dir+file, self.gmod+"\\garrysmod\\data\\smh\\")

        if os.path.exists(save_dir):
            for file in os.listdir(save_dir):
                shutil.copy(save_dir+file, self.gmod+"\\garrysmod\\saves\\")


    def push(self):
        """
Pushes the repo's commits back to it's Remote, which in most cases is likely going to be a GitHub repo.
"""
        subprocess.run(["git", "push"])


    def pull(self):
        """
Retrieves the latest commits from the Remote repo, which is likely a GitHub repo.
"""
        subprocess.run(["git", "pull"])


    def commit(self, commit_desc):
        """
Take all extracted files and save them as a commit, takes a commit description as an argument.
"""
        self.add_all()
        if len(commit_desc) <= 50:
            subprocess.run(["git", "commit", "-m", commit_desc])
        else:
            subprocess.run(["git", "commit", "-m", commit_desc[:50], "-m", commit_desc[50:]])


    def add_all(self):
        """
Adds all newly copied files to the repo tree so that they can be committed.
"""
        subprocess.run(["git", "add", "--all"])


    def list_smh_files(self):
        """
Returns a list of all smh files in the directory of the repo.
The local path is included in each string
"""
        try:
            smh_files = os.listdir(self.dir + "\\SMH")
        except FileNotFoundError:
            smh_files = []

        return smh_files


    def list_save_files(self):
        """
Returns a list of all save filels in the directory of the repo
"""
        try:
            save_files = os.listdir(self.dir + "\\Saves")
        except:
            save_files = []

        return save_files
