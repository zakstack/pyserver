from os import system, name 
import time
import subprocess
from entity import *

class Player(Entity):
    def __init__(self, entityid):
        super().__init__(entityid)