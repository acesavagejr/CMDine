import os
from core import Core
def Get_list(CMD):
    if CMD == "test":
        print("hi!")
        Core()
    if CMD == "exit":
        os.system("clear")
        print("Thanks for using CMDine!")
        exit()
    
    if CMD == "help":
        print("----Help----")
        print("Test........returns 'hi' made for testing")
        print("help........You know... this page")
        print("dineout.....To get programs from the dineout repo")
        print("run.........To run programs installed from DineOut or others")
        print("Clear.......To clear your screen")
        print("exit........to exit CMDine")
        Core()
    
    if CMD == "clear":
        os.system("clear")
        Core()
    
    if CMD == "dineout":
        os.system("clear")
        print("What prog?")
        print("1. calc")
        print("2. weatherplug")
        PROG = input()
        
        if PROG == "calc":
            os.system("wget acesavagejr.github.io/DineOut/Calc.py")
            os.system("clear")
            Core()
        
        if PROG == "weatherplug":
            os.system("wget -P /home/entity/Desktop/CMDine acesavagejr.github.io/DineOut/WeatherPlug.py ")
            os.system("clear")
            Core()
   
    if CMD == "run":
        CMD = input("Which program? ")

        if CMD == "calc":
            from Calc import Calc
            Calc()
        
        if CMD == "weatherplug":
            from WPLG import WP
            WP()
        
    if CMD == "rm":
        PROG = input("Which program? ")
        if PROG == "calc":
            os.system("rm Calc.py")
            Core()
            
        if PROG == "weatherplug":
            os.system("rm WPLG.py")
            Core()
