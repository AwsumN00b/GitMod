#!/usr/bin/env python3

# Written by Brel00m

import os, git

def init_repo():
    repo_dir = os.path.join("GitMod", 'test-repo')
    r = git.Repo.init(repo_dir)
    r.index.commit("initial commit")

def main():
    init_repo()

if __name__ == '__main__':
    main()
