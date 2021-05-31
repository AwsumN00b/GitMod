#!/usr/bin/env python3

# Written by Brel00m

import os
from cmd import Cmd
from thunking import thunking
from GmodRepo import GmodRepo
from config import KamThunking
from RepoShell import RepoShell


class GMShell(Cmd):

    prompt = "~~~> "
    repo = None

    # ~~ Commands for when not in a repo ~~
    def do_quit(self, args):
        """Exits the program"""
        print("Bye Bye!")
        raise SystemExit


    def do_open(self, args):
        """Choose a repo to work out of. From here you can import and export
        files from GarrysMod as you need to"""

        repos = get_local_repos()

        if args.isdigit():
            n = int(args)
        else:
            self.do_repos("")
            n = int(input("Enter the number of the repo you want to open: "))

        self.repo = GmodRepo(repos[n])


        self.prompt = "[" + self.repo.name + "] ~~~> "


    def do_init(self, args):
        """Creates a new repo with whatever name you give it.
        This is only for local repos. Make a repo on GitHub and clone it
        if you wish to share your project with multiple people online"""

        if len(args) == 0:
            name = input("Enter a name for the repo: ")
        else:
            name = "-".join(args.split())

        new_repo = GmodRepo(name)


    def do_repos(self, args):
        """Lists out all repos in the GitMod folder"""

        repos = get_local_repos()

        i = 0
        for repo in repos:
            print(i, ":", repo)
            i += 1


    def do_clone(self, args):
        """Takes a link to a Git Repository (GitHub primarily) as an argument.
        This will attempt to clone the repo in to the GitMod directory"""

        name = get_repo_name_from_url(args)

        cloned_repo = GmodRepo(name, args)

        self.do_open(name)


    # ~~ Commands for inside a repo ~~
    def do_close(self, args):
        """Closes the current repo"""

        if self.repo is None:
            print("No repo is currently opened")
        else:
            self.prompt = "~~~> "
            self.repo = None


    def do_extract(self, args):
        """Retrieves all known associated files from your Gmod
        and updates the repo (Associated files will have the repo's
        name at the beginning of their filename)"""

        if self.repo is None:
            print("No repo is currently opened")
        else:
            self.repo.extract_smh()
            self.repo.extract_save()



def get_local_repos():
    """Lists all folders inside the GitMod directory"""

    return os.listdir("GitMod")


def get_repo_name_from_url(url: str) -> str:
    last_slash_index = url.rfind("/")
    last_suffix_index = url.rfind(".git")
    if last_suffix_index < 0:
        last_suffix_index = len(url)

    if last_slash_index < 0 or last_suffix_index <= last_slash_index:
        raise Exception("Badly formatted url {}".format(url))

    return url[last_slash_index + 1:last_suffix_index]


if __name__ == '__main__':
    if KamThunking:
        thunking()
    GMShell().cmdloop()
