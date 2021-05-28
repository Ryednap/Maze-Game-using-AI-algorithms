from Setting import *
import pygame, math
from Algorithms import Pair
from math import ceil
from helper import *

class Mariko:
    def __init__(self, App, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.initPos = Pair(x, y)
        self.gridpos = self.initPos
        self.dir = pygame.math.Vector2(0, 0)
        self.delta = self.dir # Initially 0, 0
        self.score = 0
        self.lives = 2
        self.gameOver = False
        self.App = App
        self.Load()
        self.turn = 0
    

    def Load(self):
        print("Hello From Mariko")
        self.images = {
            "NORTH" : [Get("NorthStanding"), Get("NorthWalking1"), Get("NorthWalking2")],
            "SOUTH" : [Get("SouthStanding"), Get("SouthWalking1"), Get("SouthWalking2")],
            "EAST" : [Get("EastStanding"), Get("EastWalking1"), Get("EastWalking2")],
            "WEST" : [Get("WestStanding"), Get("WestWalking1"), Get("WestWalking2")]
        }


    def Move(self, dir):
        self.dir = dir
    
    def gridPos(self, pos):
        #/x = int(self.initPos.x  + ceil(2 * pos.x / CELL_WIDTH))
        #y = int(self.initPos.y  + ceil(2 * pos.y / CELL_HEIGHT))

        # nearest reound
        x = int(ceil(self.initPos.x + pos.x / 2.0))
        y = int(ceil(self.initPos.y + pos.y / 2.0))
        
        return Pair(x, y)

    def checkPosition(self, pos):
        temp = self.gridPos(pos)
        x, y = temp.x, temp.y

        if(x < 0 or y < 0 or x > WIDTH or y > HEIGHT):
            return False

        if(self.App.grid[y][x] == '2'):
            self.App.grid[y][x] = '1'
            self.score += 100
        
        here = self.App.grid[y][x]
        assert (here != '2')
        if(here == '1' or here == '2'):
            return True
        return False      

    def Update(self):
        if(self.dir != DEFAULT):
            self.turn = (self.turn + 1)%6
            
        if(self.checkPosition(self.delta + self.dir) == True):
            self.delta += self.dir


    '''
        DRAWER FUNCTION FOR THE CHARACTER WITH ANIMATION
        we know that self.turn can take value from [0, 1, 2, 3, 4, 5] now dividing it by 2
        [0, 0, 1, 1, 2, 2] so this variable INDEX is in which state is in our animation.
        As the numbers are laid twice i.e [0, 0, 1, 1 so on] means one state (for eg. NorthStanding) for twice keyboard click.

        self.turn is increased in Update function
    '''


    def draw(self):
        INDEX = self.turn // 2
        self.gridpos = self.gridPos(self.delta) # update the gridPos
        self.App.screen.blit(
            self.images[Hash(self.dir)][INDEX],
            ((self.initPos.x  +  self.delta.x / 2.0) * CELL_WIDTH, \
                (self.initPos.y  + self.delta.y / 2.0) * CELL_WIDTH)
        )
        pygame.display.update()

'''
    pos.x = self.initPos.x * CELL_HEIGHT + 2 * (self.delta.x + self.dir.x)
'''
    
    
