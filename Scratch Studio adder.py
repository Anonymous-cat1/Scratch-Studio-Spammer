print("Setting up scratchattach and other libaries, Please wait.")
import os
os.system("pip install -U scratchattach")
import scratchattach as scratch3
#silly scratchattach setup

input("++++WARNING++++ \nThis script should ONLY be ran on an alt account under a VPN! you risk getting your account being permamently blocked and/or ip banned if you do this too many times, press Enter to accept these risks.")
#warnings

loginuser = str(input("\nInput the account's username that you want to add the project from \n"))
loginpass = str(input("\nInput the account's password that you want to add the project from \n"))
#Asks you for login details

try:
    session = scratch3.login(loginuser, loginpass)
except:
    input("\nLogin details are inccorect or the account is banned, press Enter to exit.")
    exit(1)
#Log in as user

istudio = scratch3.explore_studios(query="*", mode="recent", language="en", limit=1, offset=0)
istudio = (istudio[0]['id'])

print("\nLogged in!\nMost recent studio is: " + str(istudio))
#get most recent studio

cproject = int(input('\nWhat project? (enter project id...) \n'))
#Asks you for the project id

maxstudios = int(input("\nHow many studios should the project be added to? (max 300) \n"))
#Asks you for the project id
if maxstudios > 300:
    print("\nOops! you cannont add a project to over 300 studios! this is a scratch limit and NOT a shortcoming of this program!")
    exit(1)
#Kill program if maxstudios is over 300 

cstudio = ""
#Sets as a empty string

aproject = 0
#Initalizes the added project to # of studios var

print("\nAdding Started!, now wait.")
try:
    while True:
        #we do a little trolling
        cstudio = session.connect_studio(istudio)
        #Gets Information
        if str(cstudio) == 'None':
            #If studio is dead (i.e deleted, unreachable)
            while str(cstudio) == 'None':
                #Try to find a studio that ISN'T dead.
                print("Dead Studio! Skipping to next one...")
                istudio -= 1
                cstudio = session.connect_studio(istudio)
                if str(cstudio) == 'None':
                    #If studio is dead (i.e deleted, unreachable)
                   continue
                else:
                    #If studio is NOT dead
                    break
        if cstudio.open_to_all:
            #if studio is open to all
            cstudio.remove_project(cproject)
            #removes project (even it's not in the studio) to re add it (i.e bump)
            cstudio.add_project(cproject)
            aproject += 1
            istudio -= 1
            print("Added project to " + str(istudio) + " Studio " + str(aproject) + " out of " + str(maxstudios))
            if aproject == maxstudios:
                print("Reached " + str(aproject) + " out of " + str(maxstudios) + " studios")
                input("Finshed, press Enter to exit.")
                exit()
        else:
            #If studio is not open to all
            istudio -= 1
            print('Everyone adding disabled. Skipping...  Now On Studio ' + str(istudio))
except:
    input("\n\nUh oh, something bad happend.... The code monkeys to Anonymous_cat HQ have died so this script has suddenly stopped working...\nPerhaps check your internet connection,\nIf the project is stil up,\nIf your account isn't banned,\nOr if the project is already in 300 studios.\n\Press Enter to exit.")
    exit(0)
