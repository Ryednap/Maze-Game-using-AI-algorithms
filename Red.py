from Setting import *
from helper import *
from math import ceil
from Algorithms import Astar, Pair, BFS
import pygame
import random

class Red:
    def __init__(self, App, x, y):
        self.App = App
        self.currPos = Pair(x, y)
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


    def Update(self):

        if(self.currPos == self.nextPos):
            here = Pair(int (self.currPos.x), int (self.currPos.y))

            self.updateBestPath(here, self.App.retPlayerPos())
            self.nextPos = (self.bestPath.pop())
            self.nextPos = self.nextPos
            self.dir = self.nextPos - self.currPos
            print(self.bestPath)
        
        self.currPos = self.currPos + self.dir / 4.0
        self.turn = (self.turn + 1)%12

    def draw(self):
        INDEX = self.turn // 3
        if(self.dir == EAST or self.dir == NORTH):
            self.App.screen.blit(
                self.image_right[INDEX],
                (self.currPos.x * CELL_WIDTH, self.currPos.y * CELL_HEIGHT)
            )
        else :
            self.App.screen.blit(
                self.image_left[INDEX],
                (self.currPos.x * CELL_WIDTH, self.currPos.y * CELL_WIDTH)
            )
        pygame.display.update()
        

        

    
