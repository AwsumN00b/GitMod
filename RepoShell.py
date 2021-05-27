#!/usr/bin/env python3

# Written by Brel00m

import cmd
from GmodRepo import GmodRepo


class RepoShell(cmd.Cmd):

    def __init__(self, repo):

        super(RepoShell, self).__init__()
        self.repo = repo


    def do_extract(self, args):
        print("s")
        print(args)
        self.repo.extract_smh()


    def do_close(self, args):
        """Closes the current repo and returns to the shell"""

        return True


    def do_extract(self, args):
        """Pick files from Gmod (SMH Files, GM Save Files, etc.)"""
