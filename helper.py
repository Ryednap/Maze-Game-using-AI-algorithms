from Setting import *
from math import sqrt,fabs
import pygame

def Get(name, delta = 0):
        name = "CTF/Data/" + name + ".png"
        print (name)
        image = pygame.image.load(name)
        image = pygame.transform.scale(
            image,
            (CELL_WIDTH + delta, CELL_HEIGHT + delta)
        )
        return image

def Hash(s):
    if (s == NORTH):
        return "NORTH"
    if (s == SOUTH):
        return "SOUTH"
    if (s == EAST):
        return "EAST"
    return "WEST"

def Manhattan(a, b, x, y, D = 1):
    return D * abs(a - x) + abs(b - y)

def Euclidean(a, b, x, y, D = 1):
    dx = abs(a - x)
    dy = abs(b - y)
    return D * sqrt(dx * dx + dy * dy)



class Path :
    def __init__(self, path, totalCost):
        self.path = path
        self.totalCost = totalCost
    
    def pop(self):
        return self.path.pop()

    def append(self, el):
        self.path.append(el)
   
    def xySwap(self):
        for i in range(len(self.path)):
            self.path[i].swap()

    def reverse(self):
        self.path.reverse()

    def __str__(self):
        s = ""
        for el in self.path:
            s += str(el)
        
        return s
    
    def __eq__(self, other):
        return(
            self.path == other.path and
            self.totalCost == other.totalCost
        )