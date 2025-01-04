import sys
import datetime
from time import sleep


#import first required libs

def createlog(txt):
    # creates a new log
    logs.write("Log: "+str(txt)+" | "+str(datetime.datetime.now())+"\n")

def getIds(inp):
    # converts studio objects into ids
    out = []
    for i in range(0, len(inp)):
        out.append(inp[i].id)
    return out

if "-v" in sys.argv:
    # check for verbose arg
    verbose = True
    print("Logfile enabled.")
    # create/open the logfile
    logs = open('errorlog.txt', 'a')
    logs.write("Program Start: " + str(datetime.datetime.now()) + "\n")
else:
    verbose = False

if "-b" in sys.argv:
    # check for blast mode arg
    blast = True
    print("Blast mode enabled.")
else:
    blast = False

try:
    # check and set args
    loginUser = str(sys.argv[1])
    loginPass = str(sys.argv[2])
    project = int(sys.argv[3])

except Exception as e:
    # print help
    print("""
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
    """)

    if verbose:
        createlog(e)
    exit(1)

import time
try:
    # attempt to install scratch attach
    import scratchattach as scratch3
except:
    # if scratchattach isn't installed
    print("\nScratchattch is not installed, installing...")
    import os
    os.system("pip install scratchattach")
# import other libs

try:
    # log in
    session = scratch3.login(loginUser, loginPass)
    print("\nLogged in!")
except Exception as e:
    print("\nError logging in.")
    if verbose:
        createlog(e)
    exit(1)
# log in as user

try:
    project = session.connect_project(project)
    # overwrite project id with project object
    input("""
    Just to be sure, you are going to spam:
    
    """ +project.title+ " by " +str(project.author())+ """ 
    
    Under the account """ +loginUser+ """. 
    
    Anonymous_cat does not assume any responsibility to what you are about to do.
    Using this script on a VPN with an alt created under a VPN is highly recommended.
    
    Press ENTER to start the script.
    """)


except Exception as e:
    print("\nError Getting project.")
    if verbose:
        createlog(e)
    exit(1)
# get project, ask user to verify

try:
    # get newest studio
    curStudio = session.explore_studios(query="*", mode="recent", language="en", limit=1, offset=0)
    curStudio = 75 + curStudio[0].id
    # the explore tab is delayed by about 30 minutes, so we add an arbitrary number
except Exception as e:
    print("\nError Getting most recent studio.")
    if verbose:
        createlog(e)
    exit(1)

# Counts how many studios a project has been added to # of studios var
addedCount = len(project.studios())

print("\nAdding Started!, now wait.\n(Note, you may get multiple dead studios at first, don't panic!)\n")
try:
    while True:
        delta = datetime.datetime.now()
        # Initiates a delta to determine how long to wait after adding a project (minimum 12 seconds)

        studioSession = ""
        # Initializes studio object with nothing
        while studioSession == "":
            try:
                # Connect to studio
                studioSession = session.connect_studio(curStudio)
            except:
                # if studio is dead (or error)
                print("Dead studio! skipping... " + str(datetime.datetime.now()))
                curStudio -= 1

        if studioSession.open_to_all:
            # If studio that is open to all is found
            if curStudio in getIds(session.connect_project(project.id).studios()):
                 # If project is already in the studio
                print("Project already in studio, skipping... " + str(datetime.datetime.now()))
                curStudio -= 1
            else:
                studioSession.add_project(int(project.id))
                addedCount += 1
                print("Added project to studio "+str(curStudio)+"! (" + str(addedCount) + " studios added). " + str(datetime.datetime.now()))
                if not blast:
                    # if blast mode is disabled, sleep for at most 12 seconds
                    rest = (max(0.0, (12 - (datetime.datetime.now() - delta).total_seconds())))
                    print("Sleeping for " +str(rest)+ " seconds to avoid hitting ratelimit... " + str(datetime.datetime.now()))
                    time.sleep(rest)
                curStudio -= 1
        else:
            # if studio is not open to all
            print("Studio is not open to all, skipping... " + str(datetime.datetime.now()))
            curStudio -= 1
except Exception as e:
    print("""
    Uh oh, the code monkeys at Anonymous_cat HQ died.
    
    Either:
        - You hit the ratelimit (300 studio adds per hour)
        - You had a network issue
        - The account you used got banned or logged out during script execution
     
    Try running the script again with -v to enable logs.
    """)
    if verbose:
        createlog(e)
    exit(1)
# mainloop