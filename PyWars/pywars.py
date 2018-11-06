from os import system, name 
from curses import *
import sys
import time
import subprocess
import gamemap

import player

class Pywars():
    def __init__(self,xsize,ysize):
        self.title_loop = True
        self.game_loop = False
        self.pause_loop = False
        self.inventory_loop = False
        self.battle_loop = False
        self.map = gamemap.GameMap(0,xsize,ysize)
        wrapper(self._Graphics)
    
    def Start(self):
        while self.title_loop:
            self._Clear()
            self.Title()
            time.sleep(1)

    def Title(self):
        print("Welcome to PyWars")
        menu = [ ["","New Game"] ,["","Continue"], ["" , "Settings"], ["" , "Quit"] ]
        for i in menu: print(i[1])\

    # UTILITIES
    # Clears the screen
    def _Clear(self): 
        if name == 'nt': 
            _ = system('cls') 
        else: 
            _ = system('clear') 

    def _Execute_Shell(self, inputstring, argv = None):
        result = None
        comd = [inputstring]
        if argv is not None:
            test = comd.extend(argv)
            print(test)
            result = subprocess.run(comd, stdout=subprocess.PIPE)
        else:
            result = subprocess.run(comd, stdout=subprocess.PIPE)
        return result.stdout

    def _Graphics(self,stdscr):
        # Clear screen
        stdscr.clear()

        map = self.map.GetMap()
        xsize = len(map)
        ysize = len(map[0])
        for x in range(0,xsize):
            for y in range(0,ysize):
                init_pair(1, COLOR_RED, COLOR_GREEN)
                stdscr.addstr(x,y,map[x][y],color_pair(1))
        stdscr.refresh()
        stdscr.getkey()

#game = Pywars(70,250)
#game.Start()
#print(game._Execute_Shell("ls",["-l", "-a"]).decode('utf-8'))

#newmap = gamemap.GameMap(0,10,10)
#newmap.GetMap
#mainplayer = player.Player(100)
#mainplayer.EntityTest()