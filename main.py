import json
from os import system, name
import re

LINKS=[]

def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

while True:
    cmd=input()
    # + COMMAND
    # USAGE: +[LINK]
    if re.search("^\+",cmd):
        LINKS.append(cmd[1:])
        print("link", cmd[1:], "added")
    # PRINT COMMAND
    # USAGE: PRINT, PRINT [INDEX]
    elif re.search("^print",cmd):
        if cmd == "print":
            print(LINKS)
        else:
            try:
                print(LINKS[int(cmd[6:])])
            except:
                print("this would have killed your memory but i saved it for you :3")
                print("next time dont do this bs again")
    # LEN COMMAND
    elif cmd == "len":
        print(len(LINKS))
    # CLEAR COMMAND
    elif cmd == "cls" or cmd == "clear":
        clear()
    # LOAD COMMAND
    elif cmd == "load":
        print("this will delete all links in the editor and load the links.json file into memory, (idk why you would ever want to do this) are you sure? y/N: ")
        if input()=="y":
            try:
                with open("links.json", "r") as f:
                    LINKS = json.load(f)
                    print("loaded links.json")
            except:
                print("this would have killed your memory but i saved it for you :3")
                print("next time dont do this bs again")
        else:
            print("aborted.")
    # PUSH COMMAND
    elif cmd == "push":
        print("this will append all links in memory to the links.json file, are you sure? y/N: ")
        if input()=="y":
            try:
             with open("links.json", "r") as f:
                 tempLoad = json.load(f)
                 tempLoad.extend(LINKS)
             with open("links.json", "w") as f:
                 json.dump(tempLoad, f)
                 print("pushed editor memory to links.json")
            except:
                print("this would have killed your memory but i saved it for you :3")
                print("next time dont do this bs again")
        else:
            print("aborted.")
    elif cmd == "override":
        print("THIS WILL COMPLETELY OVERRIDE THE LINKS.JSON FILE WITH MEMORY, ARE YOU REALLY SURE YOU WANT TO DO THIS? y/N: ")
        if input() == "y":
            try:
                with open("links.json", "w") as f:
                    json.dump(LINKS, f)
                print("replaced links.json")
            except:
                print("this would have killed your memory but i saved it for you :3")
                print("next time dont do this bs again")
        else:
            print("aborted.")
    elif re.search("^memclear",cmd):
        if cmd == "memclear":
            print("THIS WILL CLEAR ALL OF MEMORY, ONLY DO THIS IF YOU ARE ABSOLUTELY SURE y/N: ")
            if input() == "y":
                LINKS = []
                print("memory cleared")
            else:
                print("aborted.")
        else:
            try:
                LINKS.pop(int(cmd[9:]))
                print("deleted item", int(cmd[9:]), "from memory")
            except:
                print("this would have killed your memory but i saved it for you :3")
                print("next time dont do this bs again")

    elif re.search("^find",cmd):
        try:
            print("we think what you are looking for is in index", LINKS.index(cmd[5:]))
        except:
            print("well we couldn't find what you are looking for but i saved ur memory from death again")
    elif cmd == "help":
        print("JSON EDITOR 1.O BY SKRYBL")
        print("commands:")
        print("help - shows this menu.")
        print("+ - adds a link to memory. EXAMPLE: +https://angusnicneven.com")
        print("print - prints out memory, or optionally a link at a specific index. EXAMPLE: print, print 4")
        print("len - shows you how many links you have in memory.")
        print("clear/cls - clears the screen.")
        print("push - pushes memory to the links.json file.")
        print("load - loads the json file to memory (no clue why you would want to do this).")
        print("memclear - clears memory or a specific link in memory (remember that memory starts at index 0) EXAMPLE: memclear, memclear 4")
        print("override - REPLACES the links.json file with memory. //scary!")
        print("find - find where the hell you put your links. EXAMPLE: find https://angusnicneven.com/")
    else:
        print("no command found, type 'help' for a list of available commands.")
