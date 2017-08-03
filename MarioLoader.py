import shutil
import pyhk
import os
import pickle
import fnmatch
import glob
import random
import pyautogui
from shutil import copyfile

random.seed()

## .ini-File Loading -- Reads the .ini file and grabs the saved variables from it
if (os.path.isfile("Memory.ini")) :
    with open("Memory.ini","rb") as opo:
        Load=pickle.load(opo)
else:
    Load={}
    
### Check for correct Directories
# first checks for the correct PJ64 directory
try:
    PJ64dir=Load["PJ64dir_mem"]
except KeyError:
    PJ64dir=""

# next checks if the PJ64.exe and the "SaveFiles" folder are in the expected location    
Dircheck=False
while Dircheck==False:
    if (os.path.isfile(PJ64dir+"\\Project64.exe")) :
        if os.path.isdir("SaveFiles"):
            Dircheck=True
        else:
            print("SaveFiles folder not found! Ple0ase place the Folder in the same Directory as this Program")
            exit()
            
    else: # asks for the PJ64 directory if it couldn't be found
        PJ64dir=input("Insert PJ64 Path: ")
        #PJ64dir=r"P:\FVV - Radialverdichter\09_Studenten\HIWI_Rommes\Programmieren\Python\Testprogramme\Loader\Programm Bob\PJ64"

os.chdir("SaveFiles")

## Saves Stuff
def savestuff():
    "saves relevant Data into a .ini File"
    Saves={"PJ64dir_mem": PJ64dir,"LoadList_mem": LoadList} 
    with open("..\\Memory.ini","wb") as opo:
        #pickle.dump(PJ64dir,opo)
        #pickle.dump(SaveList,opo)
        pickle.dump(Saves,opo)

        

## List Initializer
# Tries to load the List containing all the information. Otherwise initializes the list in the standard format
try:
    LoadList=Load["LoadList_mem"]
except KeyError:
    ActualList=glob.glob("[0-9][0-9]*.zip")  # looks for the savefiles in the standard format (example: "05_WF_3.zip")
    LoadList=[]
    for i in range(0,len(ActualList)):
        LoadList.append({"name":ActualList[i],"active":1,"hist":0,"diff":1}) 
        
        # Format: 
        # name: name of the Savefile, 
        # active: is the Savefile active and thereby loadable?(0=off,1=on)
        # hist: integer representing the time this save has last been used
        # diff: difficulty of the save (assigned by user)
        
## Select and Copy
    #pyautogui.typewrite("0")
    #pyautogui.press('f7')
    #print(LoadList[Sel])
def SelAndCop():
    # pyautogui.keyDown('alt')
    # pyautogui.press('tab')
    # pyautogui.keyUp('alt')
    "Selects a Savefile based on different criteria, then copies it to the loadable location and finally loads it in PJ64"
    diffList=[]
    for i in range(0,len(LoadList)): #generiert eine Liste mit allen Schwierigkeiten als Einträge (Integer Werte von 1-unendlich)
        if diffList.count(LoadList[i]["diff"])==0: #falls noch nicht vorhanden -> hinzufügen
            d=LoadList[i]["diff"]
            diffList.extend([d]*d)
        
        
    diff=diffList[random.randint(0,len(diffList)-1)] # Schwierigkeitsgrad ermitteln
    #print(diff)
    
    match=False
    while (match==False):
        RNG=random.randint(0,len(LoadList)-1)  # Eintrag suchen
        Sel=LoadList[RNG] # Eintrag zwischenspeichern
    #    print(Sel)
    #    print(match)
        if (Sel['diff']==diff) and (Sel['active']==1):  # Kriterien überprüfen
            match=True
            #LoadList[RNG]['active']=0 #Aktivstatus auf 0 Setzen (aus)
            
    copyfile(Sel['name'],PJ64dir+"\\Save\\SUPER MARIO 64.pj0.zip")
    #pyautogui.typewrite("0")
    #pyautogui.press('f7')
    # pyautogui.keyDown('alt')
    # pyautogui.press('tab')
    # pyautogui.keyUp('alt')
    print(Sel['name'][0:-4])
    
    # PLACEHOLDER: Aktivstatus überprüfen und History updaten


SelAndCop()
def stopo():
    hot.end()
    
hot = pyhk.pyhk()
id1 = hot.addHotkey(['Home'],SelAndCop)
id2 = hot.addHotkey(['End'],stopo)
hot.start()
print("yoyo")
                    
savestuff()
########### 
#arch='D:\Files\Programming\Python\Programs\Mario Loader\SaveFiles'
#shutil.copy(arch+'\\SF1.zip',mario+'\\SUPER MARIO 64.pj0.zip')






