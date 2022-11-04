print("Setting up scratchattach, Please wait.")
import os
os.system("pip install -U scratchattach")
import scratchattach as scratch3
#silly scratchattach setup

session = scratch3.login("USERNAME HERE", "PASSWORD HERE!!")
#ENTER YOUR INFO HERE!!!! no... It does not steal your info

studio = 32343806
#ENTER THE FIRST STUDIO TO COUNTDOWN FROM FOR YOUR PROJECT TO BE ADDED TO!!

cproject = int(input('What project? (enter prject id...) '))
#Asks you for the project id

cstudio = ""
#Sets as a empty string

while True:
    #we do a little trolling
    studio = studio - 1
    print("Attempt for studio " + str(studio))
    cstudio = session.connect_studio(studio)
    #Gets Information
    if str(cstudio) == 'None':
        #If studio is dead (i.e deleted, unreachable)
        while str(cstudio) == 'None':
            #Try to find a studio that ISN'T dead.
            print("Dead Studio! Skipping to next one...")
            studio = studio - 1
            print("Attempt for studio " + str(studio))
            cstudio = session.connect_studio(studio)
            if str(cstudio) == 'None':
                #If studio is dead (i.e deleted, unreachable)
               continue
            else:
                #If studio is NOT dead
                break
    if cstudio.open_to_all:
        #if studio is open to all
        cstudio.add_project(cproject)
        print("Added project to " + str(studio))
    else:
        #If studio is not open to all 
        print('Everyone adding disabled. Skipping...')
