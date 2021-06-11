#!/usr/bin/env python3

# Written by Brel00m

import os, git
from cmd import Cmd
from getpass import getpass
from thunking import thunking
from GmodRepo import GmodRepo
from RepoShell import RepoShell
from config import *


class GMShell(Cmd):

    prompt = "~~~> "
    repo = None

    # ~~ Commands for when not in a repo ~~
    def do_quit(self, args):
        """
Exits the program
"""
        print("Bye Bye!")
        raise SystemExit


    def do_open(self, args):
        """
Choose a repo to work out of. From here you can import and export
files from GarrysMod as you need to
"""
        repos = get_local_repos()

        if args.isdigit():
            try:
                repo_open = repos[int(args)]
            except:
                print("Invalid repo :/")
                return
        elif args in repos:
            repo_open = args
        else:
            self.do_repos("")
            n = int(input("Enter the number of the repo you want to open: "))
            try:
                repo_open = repos[n]
            except:
                print("Invalid repo :/")
                return

        self.repo = GmodRepo(repo_open)
        self.prompt = "[" + self.repo.name + "] ~~~> "


    def do_init(self, args):
        """
Creates a new repo with whatever name you give it.
This is only for local repos. Make a repo on GitHub and clone it
if you wish to share your project with multiple people online
"""
        if len(args) == 0:
            name = input("Enter a name for the repo: ")
        else:
            name = "-".join(args.split())

        # Check if folder of this name already exists
        repos = get_local_repos()
        if name in repos:
            print("Repo of this name already exists.")
            return

        new_repo = GmodRepo(name)


    def do_repos(self, args):
        """
Lists out all repos in the GitMod folder
"""
        repos = get_local_repos()

        print_columns(repos)


    def do_clone(self, args):
        """
Takes a link to a Git Repository (GitHub primarily) as an argument.
This will attempt to clone the repo in to the GitMod directory
"""
        repo_name = get_repo_name_from_url(args)

        if repo_name is not False:
            git.Repo.clone_from(args, "GitMod\\" + repo_name)
            print("Repo has been cloned!")
            self.do_open(repo_name)


        # ~~ Commands for inside a repo ~~

    def do_close(self, args):
        """
Closes the current repo
"""
        if self.repo is None:
            print("No repo is currently opened")
        else:
            self.prompt = "~~~> "
            self.repo = None


    def do_extract(self, args):
        """
Retrieves all known associated files from your Gmod
and updates the repo (Associated files will have the repo's
name at the beginning of their filename)
"""
        if self.repo is None:
            print("No repo is currently opened")
        else:
            self.repo.extract_smh()
            self.repo.extract_save()


    def do_inject(self, args):
        """
Takes the save data from the current repo, and injects it into
Gmod's files so you can use them.
"""
        if self.repo is None:
            print("No repo is currently opened")
        else:
            self.repo.inject()


    def do_dub(self, args):
        """
Rename files to make them part of the current repo.
(You may want to do extract after you are finished adding files)

File types supported (type these terms to add that type of file):
smh
saves
"""
        dubable_filetypes = [
        "smh",
        "saves"
        ]

        if self.repo is None:
            print("No repo is currently opened")
        elif args in dubable_filetypes:
            self.repo.dub_files(args)
        else:
            print("Choose a file type to start dubbing:")
            print_columns(dubable_filetypes)
            args = int(input())

            self.repo.dub_files(dubable_filetypes[args])


    def do_commit(self, args):
        """
Saves the current state of the repo as a new commit.
You will be asked to describe what you have added or changed.
"""
        if args == "":
            commit_desc = input("Describe the changes you have made: ")
        else:
            commit_desc = args

        self.repo.commit(commit_desc)
        print("Commit successful!")


    def do_push(self, args):
        """
Send all your commits off to the remote repo, updating everybody else with the changes you have made.
"""
        if self.repo is None:
            print("No repo is currently opened")
        else:
            self.repo.push()


    def do_fetch(self, args):
        """
Retrieve the latest version of the repo from the Remote.
"""
        if self.repo is None:
            print("No repo is currently opened")
        else:
            self.repo.fetch()



def get_local_repos():
    """
Lists all folders inside the GitMod directory
"""
    return os.listdir("GitMod")


def get_repo_name_from_url(url: str) -> str:
    last_slash_index = url.rfind("/")
    last_suffix_index = url.rfind(".git")
    if last_suffix_index < 0:
        last_suffix_index = len(url)

    if last_slash_index < 0 or last_suffix_index <= last_slash_index:
        return False

    return url[last_slash_index + 1:last_suffix_index]


def print_columns(list):
    """
Prints a list as two columns to save screen space
"""
    if len(list) == 1:
        print("[0]:", list[0])
        return
    elif len(list) % 2 != 0:
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


if __name__ == '__main__':
    if KamThunking:
        thunking()

    print("Welcome to GitMod Alpha Ver 0.2")
    GMShell().cmdloop()
