from Setting import *
from helper import *
from math import ceil
from Algorithms import Astar, Pair, BFS
import pygame
import random

class Red:
    def __init__(self, App, x, y):
        self.App = App
        self.currPos = self.Scale(Pair(x, y))
        self.nextPos = self.currPos
        self.dir = Pair(0, 0)
        self.deadCount = 0
        self.turn = 0
        self.bestPath = Path([], OO)

        self.load()

    
    def load(self):
        self.image_left = []
        self.image_right = []

        for i in range(4):
            self.image_left.append(Get("Redleft_" + str(i + 1)))
        
        for i in range(4):
            self.image_right.append(Get("Redright_" + str(i + 1)))

    def updateBestPath(self, curr, target):
        astar =  BFS(self.App.grid, curr, target)
        maybe = astar.optimalPath()
        self.bestPath = maybe

    """ 
        We have integer co-ordinates for the grid i.e x, y
        But to draw it on the screen we need to scale it
        to the CELL_PIXELS else if the movement will be 
        so fast that it won't look nice.

        Scale Function scales the grid co-ordinates to Screen Co-ordinates
        Unscale does the opposite.
    """
    
    def Scale(self, p):
        p = Pair(p.x * CELL_WIDTH, p.y * CELL_HEIGHT)
        return p

    def Unscale(self, p):
     #   return p
        return Pair(ceil(p.x // CELL_WIDTH), ceil(p.y // CELL_HEIGHT))


    def Update(self):

        if(self.currPos >= self.nextPos):
            self.updateBestPath(self.Unscale(self.currPos), self.App.retPlayerPos())
            self.nextPos = (self.bestPath.pop())
            self.nextPos = self.Scale(self.nextPos)
            self.dir = self.Unscale(self.nextPos) - self.Unscale(self.currPos)
            print(self.bestPath)
        
        self.currPos += self.dir * 3
        self.turn = (self.turn + 1)%12

    def draw(self):
        INDEX = self.turn // 3
        if(self.dir == EAST or self.dir == NORTH):
            self.App.screen.blit(
                self.image_right[INDEX],
                (self.currPos.x, self.currPos.y)
            )
        else :
            self.App.screen.blit(
                self.image_left[INDEX],
                (self.currPos.x, self.currPos.y)
            )
        pygame.display.update()
        

        

    
