#!/usr/bin/env python3

# Written by Brel00m

import os
from cmd import Cmd
from thunking import thunking
from GmodRepo import GmodRepo

class GMShell(Cmd):

    def do_quit(self, args):
        """Exits the program"""
        print("Bye Bye!")
        raise SystemExit


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

        i = 1
        for repo in repos:
            print(i, ":", repo)
            i += 1

    def do_open(self, args):




def get_local_repos():
    """Looks in the GitMod folder and takes every subfolder to be a Git repo"""

    return os.listdir("GitMod")


def get_repo_name_from_url(url: str) -> str:
    last_slash_index = url.rfind("/")
    last_suffix_index = url.rfind(".git")
    if last_suffix_index < 0:
        last_suffix_index = len(url)

    if last_slash_index < 0 or last_suffix_index <= last_slash_index:
        raise Exception("Badly formatted url {}".format(url))

    return url[last_slash_index + 1:last_suffix_index]


def main():
    prompt = GMShell()
    prompt.prompt = "~~~> "
    prompt.cmdloop(thunking())

if __name__ == '__main__':
    main()
