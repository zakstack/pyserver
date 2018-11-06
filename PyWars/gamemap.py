from os import system, name 
import time
import subprocess

class GameMap():
    def __init__(self, mapid, xsize, ysize):
        self.map_id = mapid
        self.x_size = xsize
        self.y_size = ysize
        self.map = []
        for x in range(0,xsize):
            tempcol = []
            for y in range(0,ysize):
                tempcol.extend(["."])
            self.map.extend([tempcol])
            
    def GetMap(self):
        return self.map
