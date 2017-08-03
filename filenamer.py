import shutil, os
from shutil import copyfile
stop="False"
while stop=="False":
    PJ64='C:\\Games\\N64\\Project64 1.6\\Save\\'
    Savedir="D:\Files\Programming\Python\Programs\Mario Loader\SaveFiles\\"
    anzahl=int(input("Weivill Savefiles? "))
    start=int(input("Eichten Savefile (Nummer): "))
    with open("SaveFiles\\Names.txt","r") as op:
        lescht=op.readlines()

    sourcename1 = 'SUPER MARIO 64.pj'
    sourcename2 = '.zip'
    i=0
    while i<anzahl:
        filename = sourcename1 + str(i+1) + sourcename2
        numm = lescht[start +i-1]
        numm = numm[:(len(numm)-1)]
        copyfile(PJ64+filename, Savedir+numm+sourcename2)
        print(numm)
        i+=1

    response=input("Again? y/n :")
    if response!="y":
        stop="True"
    
    
        
