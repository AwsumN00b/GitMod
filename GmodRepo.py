#!/usr/bin/env python3

import git, os
from config import Gmod_Location as gmod

# Written by Brel00m

class GmodRepo():

    def __init__(self, repo_name, link=None):
        self.name = repo_name

        if link is None:
            repo_dir = os.path.join("GitMod", self.name)
            r = git.Repo.init(repo_dir)
            r.index.commit("initial commit")
        else:
            git.Git("GitMod").clone(link)


    def path_checker():
        if gmod == "" or not os.path.exists(gmod):
            print("Please add your Gmod directory path to config.py before continuing")
            exit()


    def pick_files(path, filetype):
        path_checker()

        files = os.listdir(path)
        files = [file for file in files if filetype in file and self.name in file]

        return files


    def grab_smh():
        files = pick_files(gmod + "\\garrysmod\\data\\smh", ".txt")


    def pull():
        pass


    def commit():
        pass
