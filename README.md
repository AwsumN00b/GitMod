# GitMod - Git Version control for Gmod Animators!

## Introduction
The aim of this program is to use Git to allow Gmod Animators to work together on videos and projects. Presently, there is no easy way for them to do this.

The function goals of this application are to incorporate Stop Motion Helper saves and GarrysMod map saves into a Git repository. The Gmod Animation Community, with specific reference to House of the Gmodders, has shown much interest in pursuing multi-person projects within Gmod Animation. Stop Motion Helper is a Gmod addon that is generally accepted as a standard tool for use in the creation of animations. I think Git is a tool that could have extreme potential for this community but it is, by default, not intuitive to use with how GarrysMod is set up. This is to be a program that identifies relevant Gmod save files, SMH .txt files, and any other possibly relevant files to creators and incorporate them into a Git repository for easy sharing and updating across several parties. This also means including the ability to interact with GitHub to share such Git repositories online.

To use this program, use Python to run GMShell.py

## Requirements
To make this program work, you are going to need the following installed on your computer. (This program is set up to work for Windows 10 only)
- [Python 3](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)
- GitPython library. Type this in your terminal:
`` python -m pip install GitPython ``
- Colorama. Type this in your terminal:
`` python -m pip install colorama ``
- GarrysMod (Steam install)
- [Stop Motion Helper](https://steamcommunity.com/sharedfiles/filedetails/?id=111895870)

## To Do
Fix these things:
- Edge cases all around (Specifics will be added as testing occurs)
- add repocheck to dub function
- check if overwriting files are smaller than original and ask user if they are sure about this action
- Make repo open as soon as its cloned and also push if its the initial commit

Add following functionalities:
- function for picking files either by name or numerically, and both 
- Create compiled version for non-techy people to use
- Make a GUI, again to enhance the experience

## Credits
If you have assisted in any way, please add your name!

[Ethan Clarke](https://github.com/AwsumN00b)
