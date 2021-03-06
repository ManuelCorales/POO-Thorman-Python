import time
import copy
from thing import thing


class Bomb(thing):
    def __init__(self, position):
        self.explotionTime = 3  # seconds
        self.explotionRange = 3
        self.position = copy.deepcopy(position)
        self.damage = 1
        self.hp = 0
        self.hitbox = [128, 128]

    def setPosition(self, pos):
        self.position = pos

    def getPosition(self):
        return self.position

    def setExplotionRange(self, exprng):
        self.explotionRange = exprng

    def getExplotionRange(self,):
        return self.explotionRange

    def setExplotionTime(self, exptm):
        self.explotionTime = exptm

    def getExplotionTime(self):
        return self.explotionTime

    def explode(self,):
        pass

    def getTime(self):
        return self.explotionTime

    def setTime(self, explotionTime):
        self.explotionTime += explotionTime

