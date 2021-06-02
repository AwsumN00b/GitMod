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
                os.mkdir("Gitmod\\" + repo_name + "\\saves")
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


    def extract_save(self):
        saves = self.pick_files(gmod + r"\garrysmod\saves", ".gms")
        icons = self.pick_files(gmod + r"\garrysmod\saves", ".jpg")

        file_source = gmod + r"\garrysmod\saves\\"
        file_target = "GitMod\\" + self.name + "\\saves"

        for file in saves:
            shutil.copy(file_source + file, file_target)
        for file in icons: # taking the save thumbnails into the repo too
            shutil.copy(file_source + file, file_target)

        print("Data successfully copied into Garry'd Mod")


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



    def pull():
        pass


    def commit():
        pass
