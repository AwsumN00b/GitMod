#!/usr/bin/env python3

# Written by Brel00m

from cmd import Cmd
from GmodRepo import GmodRepo


class RepoShell(Cmd):

    def __init__(self, repo):

        super(RepoShell, self).__init__()

        self.repo = repo


    def do_close(self, args):
        """Closes the current repo and returns to the shell"""

        return True
