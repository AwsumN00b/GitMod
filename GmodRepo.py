#!/usr/bin/env python3

# Written by Brel00m

import git, os, shutil
from config import Gmod_Location as gmod


class GmodRepo():

    def __init__(self, repo_name, link=None):
        self.name = repo_name

        if link is None:
            repo_dir = os.path.join("GitMod", self.name)
            r = git.Repo.init(repo_dir)

            try:
                os.mkdir("GitMod\\" + repo_name + "\\smh")
                os.mkdir("Gitmod\\" + repo_name + "\\save")
            except FileExistsError:
                pass

            r.index.commit("initial commit")
        else:
            git.Git("GitMod").clone(link)


    def path_checker(self):
        if gmod == "" or not os.path.exists(gmod):
            print("Please add your Gmod directory path to config.py before continuing")
            exit()


    def pick_files(self, path, filetype):
        self.path_checker()

        files = os.listdir(path)
        files = [file for file in files if filetype in file and file.startswith(self.name + "_")]

        return files


    def extract_smh(self):
        files = self.pick_files(gmod + r"\garrysmod\data\smh", ".txt")

        file_source = gmod + r"\garrysmod\data\smh\\"
        file_target = "GitMod\\" + self.name + "\\smh\\"

        for file in files:
            shutil.copy(file_source + file, file_target + file)


    def pull():
        pass


    def commit():
        pass
