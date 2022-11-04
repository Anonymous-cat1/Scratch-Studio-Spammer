print("Setting up scratchattach, Please wait.")
import os
os.system("pip install -U scratchattach")
import scratchattach as scratch3
#silly scratchattach setup

#````````````````````````````````````````````````````````````````````````````````
session = scratch3.login("USER HERE", "PASSWORD HERE")
#ENTER YOUR INFO HERE!!!! no... It does not steal your info
studio = 32343806
#ENTER THE FIRST STUDIO TO COUNTDOWN FROM FOR YOUR PROJECT TO BE ADDED TO!!
maxstudios = 300
#NOTE: Projects can only be added to a MAX of 300 studios, so you CANNONT go above it or you'll just waste a bunch of time...
#Another note, this WILL re-add your project to studios that alredy have it, and will insead bump your project up to the top.
#Ps, use an alt.
#````````````````````````````````````````````````````````````````````````````````

cproject = int(input('What project? (enter prject id...) '))
#Asks you for the project id

cstudio = ""
#Sets as a empty string

aproject = 0
#Initalizes the added project to # of studios var

if maxstudios > 300:
    print("Oops! you cannont add a project to over 300 studios! this is a scratch limit and NOT a shortcoming of this program!")
    exit(1)
#Kill program if maxstudios is over 300
    
print("Adding Started!, now wait.")
while True:
    #we do a little trolling
    cstudio = session.connect_studio(studio)
    #Gets Information
    if str(cstudio) == 'None':
        #If studio is dead (i.e deleted, unreachable)
        while str(cstudio) == 'None':
            #Try to find a studio that ISN'T dead.
            print("Dead Studio! Skipping to next one...")
            studio -= 1
            cstudio = session.connect_studio(studio)
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
        studio -= 1
        print("Added project to " + str(studio) + " Studio " + str(aproject) + " out of " + str(maxstudios))
        if aproject == maxstudios:
            print("Reached " + str(aproject) + " out of " + str(maxstudios) + " studios")
            print("Finshed")
            exit()
    else:
        #If studio is not open to all
        print('Everyone adding disabled. Skipping...  Now On Studio ' + str(studio))
        studio -= 1
