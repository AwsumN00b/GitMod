# GitMod - Git Version control for Gmod Animators!

## Introduction
The aim of this program is to use Git to allow Gmod Animators to work together on videos and projects. Prior, there was no easy way for them to do this.

The function goals of this application are to incorporate Stop Motion Helper saves and GarrysMod map saves into a Git repository. The Gmod Animation Community, with specific reference to House of the Gmodders, has shown much interest in pursuing multi-person projects within Gmod Animation. Stop Motion Helper is a Gmod addon that is generally accepted as a standard tool for use in the creation of animations. I think Git is a tool that could have extreme potential for this community but it is, by default, not intuitive to use with how GarrysMod is set up. This is to be a program that identifies relevant Gmod save files, SMH .txt files, and any other possibly relevant files to creators and incorporate them into a Git repository for easy sharing and updating across several parties. This also means including the ability to interact with GitHub to share such Git repositories online.

If you are a more savvy Python user running the uncompiled scripts, I reccommend you run the scripts outside of the git repo because having multiple git repos inside of another git repo creates some incredibly unwanted side effects.

To use this program, run GitMod.exe

**Make sure you set the correct path for you Gmod's install location in the file called config.txt, or else it wont work**

**Windows Defender might see this as a virus, but I assure you there is nothing harmful here.**


## Requirements
To make this program work, you are going to need the following installed on your computer. (This program is set up to work for Windows 10 only)
- [Git](https://git-scm.com/downloads)
- GarrysMod (Steam install)
- [Stop Motion Helper](https://steamcommunity.com/sharedfiles/filedetails/?id=111895870)

## To Do
Fix/Add these things:
- prompt user at initial launch for:
- * Git global email
- * Git global Name
- * How do you sign in to GitHub locally beforehand?
- check if overwriting files are smaller than original and ask user if they are sure about this action
- GmodRepo.dub_files() does not dub save images

## Credits
If you have assisted in any way, please add your name!

[Ethan Clarke](https://github.com/AwsumN00b)
