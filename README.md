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


## Tutorial
This is a basic tutorial on how to use GitMod in the context one might want to do certain things.


### Making a Repo (OFFLINE ONLY)
> This is for making a repo that will merely serve as a save-file backup system for one person to use. If you want to create a repo that you will be sharing with others, follow the next step instead.

* In the top right, click "Add".
* Choose a name so you will remember what this project is for.
* Press "Close" to close the popout window.
* Hit "Refresh" in the top left of the window.
* You should see the repo appear in the leftmost column.

### Making a Repo (WITH ONLINE SHARING)
> This takes a few more steps and requires you to have a GitHub account. The first few steps will be carried out on github.com.

* Log in to your account on github.com.
* Navigate to your profile.
* Click on "Repositories".
* Click on "New" in the top right, it's usually a green button.
* Choose a name for this repo, and make sure you set it as private rather than public.
* Once it is created, there should be a box titled "Quick setup — if you've done this kind of thing before"
* In this box, click on "HTTPS", and then copy the link that is shown beside it.
* Now go back to the GitMod application, and click "Add".
* Paste this link into the window, the application should recognise that this is a link rather than a normal name.
* Hit the "Refresh" button, and it should appear on the left hand side.

### Adding SMH and Map-Saves to the repo
> You've got a possibly empty repo at this stage, so once you have done some animation work you should copy it over into the repo you made for it.

* Click on either "Include Saves" or "Include SMH", depending on what you wish to add right now.
* Scroll through the list until you find which one you need (It might be handy to have those filenames nearby to double-check)
* Click the box next to every file you wish to add.
* When you are done, click "Confirm".
* Now hit "Extract" and the files should appear in the window!

### Updating existing files (Committing your work)
> If you have made edits or done more work on a file you had previously added to a repo, you can update the repo with the new version of the file!

* Make sure you have saved everything in Garry's Mod.
* Hit "Extract" in GitMod
* Now hit "Commit" in the bottom right.
* You will be asked to write a short description of what changes you made, this is for keeping track of progress and helps hunt down and reverse mistakes made if something has gone wrong.

### Uploading files to Share with Others (Pushing Files)
> Once you have committed your work and are finished for the day, you probably want to send off your data for other people to access. You should try to do this all the time to make sure everyone has the most up to date version of the project.

* Do this once you have made at least one commit.
* Hit "Push", just below the Commit button.
* Your files *should* be uploaded to the GitHub server.

### Downloading the Latest Files
> Just as you have to upload your files, you will want to make sure you download the latest files so that you arent working with something that is out of date. Make sure you also communicate with your project team to ensure nobody has forgotten this! You should always do this step before you start working on a save.

* Make sure you have the correct repo selected on the left hand side.
* Hit "Pull", in the bottom right.
* Now press "Inject", this will transfer the repo's files over into your GarrysMod install so that you can work on them.


## To Do
Fix/Add these things:
- prompt user at initial launch for:
- * Git global email
- * Git global Name
- * How do you sign in to GitHub locally beforehand?
- check if overwriting files are smaller than original and ask user if they are sure about this action
- GmodRepo.dub_files() does not dub save images
- Move away from TKinter and maybe use Flask instead?

## Credits
If you have assisted in any way, please add your name!

[Ethan Clarke](https://github.com/AwsumN00b)
