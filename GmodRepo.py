#!/usr/bin/env python3

# Written by Brel00m

import git, os, shutil
from config import Gmod_Location as gmod


class GmodRepo():

    def __init__(self, repo_name):
        self.name = repo_name

        if not os.path.isdir("GitMod\\" + repo_name):
            os.mkdir("GitMod\\" + repo_name)

        try:
            os.mkdir("GitMod\\" + repo_name + "\\smh")
            os.mkdir("GitMod\\" + repo_name + "\\saves")

            self.repo = git.Repo.init("GitMod\\" + repo_name)
            self.repo.git.add(".")
            self.repo.index.commit("Initial Commit via GitMod")

        except FileExistsError:
            self.repo = git.Repo("GitMod\\" + repo_name)


    def path_checker(self):
        if gmod == "" or not os.path.exists(gmod):
            print("Please add your Gmod directory path to config.py before continuing")
            exit()


    def pick_files(self, path, filetype):
        self.path_checker()

        files = os.listdir(path)
        files = [file for file in files if filetype in file and file.startswith(self.name + "_")]

        return files


    def dub_files(self, filetype):

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
        adding_files = [int(i) for i in input().split()]

        for num in adding_files:
            file_src = path + "\\" + files[num]
            file_dst = path + "\\" + self.name + "_" + files[num]
            os.rename(file_src, file_dst)

        print("Files renamed within Gmod!")


    def extract_smh(self):
        files = self.pick_files(gmod + r"\garrysmod\data\smh", ".txt")

        file_source = gmod + r"\garrysmod\data\smh\\"
        file_target = "GitMod\\" + self.name + "\\smh\\"

        for file in files:
            shutil.copy(file_source + file, file_target + file)

        self.add_all()

    def extract_save(self):
        saves = self.pick_files(gmod + r"\garrysmod\saves", ".gms")
        icons = self.pick_files(gmod + r"\garrysmod\saves", ".jpg")

        file_source = gmod + r"\garrysmod\saves\\"
        file_target = "GitMod\\" + self.name + "\\saves"

        for file in saves:
            shutil.copy(file_source + file, file_target)
        for file in icons: # taking the save thumbnails into the repo too
            shutil.copy(file_source + file, file_target)

        self.add_all()


    def inject(self):
        smh_dir = "GitMod\\" + self.name + "\\smh\\"
        save_dir = "GitMod\\" + self.name + "\\saves\\"

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
        origin = self.repo.remote("origin")
        origin.push()


    def fetch(self):
        pass


    def commit(self, commit_desc):
        self.add_all()
        self.repo.index.commit(commit_desc)

    def add_all(self):
        self.repo.git.add(".")



def print_columns(list):
    """Prints a list as two columns to save screen space"""
    if len(list) % 2 != 0:
        last = list.pop()
    else:
        last = None

    split = len(list) // 2
    l1 = list[0:split]
    l2 = list[split:]
    i = 0
    for key, value in zip(l1,l2):
        print("[{}]: {:<20s} [{}]: {}".format(i, key, i + split, value))
        i += 1

    if last is not None:
        print(" " * 25, "[{}]: {}".format(i + split, last))
