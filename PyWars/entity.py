from os import system, name 
import time
import subprocess

class Entity:
    def __init__(self, entityid):
        self.entity_id = entityid
        self.is_visible = False
        self.x_pos = None
        self.y_pos = None

    def getPosition(self):
        if(x_pos == None):
            return False
        else:
            return True, (self.x_pos, self.y_pos)

    def GetVisible(self):
        return self.is_visible

    def SetVisible(self,setvalue):
        if(setvalue == True or setvalue == False):
            self.is_visible = setvalue

    def GetPosition(self):
        return (self.x_pos, self.y_pos)

    def SetPosition(self, xytuple):
        if(len(xytuple) == 2):
            if(xytuple[0] is not None and xytuple[1] is not None):
                self.x_pos = xytuple[0]
                self.y_pos = xytuple[1]

    def EntityTest(self):
        self.SetVisible(True)
        print(self.GetVisible())
        self.SetVisible(False)
        self.SetPosition((10,10))
        print(self.GetPosition())