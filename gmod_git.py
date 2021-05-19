#!/usr/bin/env python3

# Written by Brel00m

import os, git

# Functions create/use GitMod/ directory to store repos

def query_user():
    # the loop this function is based on
    print("\nWelcome to GitMod (prototype version)\n\n")

    while True:
        print("clone | create : ", end="")
        command = input()

        if command == "create":
            print("What will this project be called? : ", end="")
            try:
                name = input()
                init_repo(name)
                print(f"repo {name} created successfully!")
            except:
                print("Something went wrong, repo initialisation was not successful :/")

        elif command == "clone":
            print("Link to repo (right click to paste in terminal) : ", end="")
            try:
                repo = input()
                clone_repo(repo)
                print(f"repo successfully cloned!")
            except:
                print("Something went wrong, repo was not successfully cloned :/")

def init_repo(repo_name):
    repo_dir = os.path.join("GitMod", repo_name)
    r = git.Repo.init(repo_dir)
    r.index.commit("initial commit")

def clone_repo(repo_link):
    git.Git("GitMod").clone(repo_link)

def main():
    query_user()

if __name__ == '__main__':
    main()
