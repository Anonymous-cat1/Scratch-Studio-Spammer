# Scratch-Studio-Spammer 
Add a project to a billion studios to make children ANGRY!!!! I know I said I wouldn't update this, but someone asked me to make a new version so yall are getting it too.

# How it works
It uses [scratchattach](https://github.com/TimMcCool/scratchattach) by [TimMcCool](https://github.com/TimMcCool) to automate adding a project to hundreds of studios (perhaps only 300 per account per hour, although I haven't tested that far yet).
This is a command-line utility.

Running the program with no or invalid arguments will get you this
```
Help:

Arguments
  - Argument 1: Username
  - Argument 2: Password
  - Argument 3: Project

Modifiers (can be put into any order)
  - Enable logfile: -v
  - Enable blast mode (Disable sleep after adding project, this will cause you to hit the ratelimit) -b

Example: ScratchStudioSpammerVX.exe Anonymous_cat1 "ThisIsMy Password" 12345678 -v -b
(You will need to put an argument into quotes to define it as one argument if it has spaces)
```

To run, open a termial (or command prompt) in the directory the program is stored. and type in:

- For executable `ScratchStudioSpammerV2.exe [Username] [Password [Project ID] [Modifiers (optional)]` (You shouldn't need python to run)
- For PY file `Pyhton ScratchStudioSpammerV2.py [Username] [Password [Project ID] [Modifiers (optional)]`

# Building
Just use Pyinstaller, to install it use `pip install pyinstaller`.
- Run in a terminal `pyinstaller --onefile ScratchStudioSpammerV2.py` and wait. A compiled executable should be put into the `dist` folder.

# Have an issue?
Run the program with `-v` to enable the logfile, copy its contents and the contents of your terminal into a [new issue](https://github.com/Anonymous-cat1/Scratch-Studio-Spammer/issues/new).
- **DO NOT INCLUDE YOUR USERNAME, PASSWORD, OR PROJECT ID. ALSO CHECK THE LOGFILE FOR ANY OF THOSE TOO, AS THEY MAY BE PUT INTO THERE.** Otherwise, I will have to close the issue.

# USE UNDER A VPN. SCRATCH TEAM MAY BAN YOUR IP FOR USING THIS FOR AN EXTENDED TIME. THIS PROGRAM COMES WITH NO WARRENTY.
