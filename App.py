import pygame, sys, os
from Setting import *
from helper import *
from Mariko import *
from Red import *
from Black import *
from fellow import *
from pinky import *
from Blue import *

pygame.init()


class App:
    def __init__(self):
        # initilizing screen
        self.screen = pygame.display.set_mode(
            (WIDTH, HEIGHT)
        )
        # pygame clock for rendering
        self.clock = pygame.time.Clock()
        # running flag
        self.running = True
        # current state 
        self.state= "PLAY"
        # turn variable to 
        self.turn = 0
        self.Load()
        self.GetLayout()
    

    def Load(self):
        self.background = pygame.image.load(
            "CTF/Data/map.png"
        )
        self.background = pygame.transform.scale(
            self.background,
            (WIDTH, HEIGHT)
        )

        self.coinSprites = ['' for _ in range(8)]
        for i in range(8):
            self.coinSprites[i] = Get(
                "GoldCoins/sprite_" + str(i),
                -10
            )
    
    def GetLayout(self):
        self.grid = [[] for i in range(GRID_HEIGHT)]
        file = open("CTF/Data/Layout/grid.lay", "r")
        i = 0
        for line in file.readlines():
            j = 0
            for cell in line:
                if(j == 0):
                    self.grid[i].append(cell)
                j ^= 1
            i += 1
        file.close()
    
    def Drawgrid(self):
        for x in range(WIDTH // CELL_WIDTH):
            pygame.draw.line(
                self.background,
                GREY,
                (x * CELL_WIDTH, 0),
                (x * CELL_WIDTH, HEIGHT)
            )
        
        for x in range(HEIGHT // CELL_HEIGHT):
            pygame.draw.line(
                self.background,
                GREY,
                (0, x * CELL_HEIGHT),
                (WIDTH, x * CELL_HEIGHT)
            )      

    def Run(self):
        self.LoadAgents()
        while (self.running):
            if(self.state == "INTRO"):
                pass # Intro screen here
            if (self.state == "PLAY"):
                self.draw()
                self.mariko.draw()
                self.Red.draw()
                self.Blue.draw()
                self.Fellow.draw()
                self.Pinky.draw()
                self.Black.draw()

                self.playingEvent()
                self.playingUpdate()

            else :
                self.running = False
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit(0)

    
    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.Drawgrid()
        count = 0

        for i in range(GRID_HEIGHT):
            for j in range(GRID_WIDTH):
                if(self.grid[i][j] == '2'):
                    self.screen.blit(
                        self.coinSprites[self.turn // 3],
                        (j * CELL_WIDTH, i * CELL_HEIGHT)
                    )
                elif(self.grid[i][j] == '1'):
                    count += 1

        self.turn = (self.turn + 1)%24
        pygame.display.update()

    def LoadAgents(self):
        self.mariko = Mariko(self, 8, 26)
        self.Red = Red(self, 20, 6)
        self.Black = Black(self, 40, 6)
        self.Blue = Blue(self, 21, 6)
        self.Fellow = Fellow(self, 22, 6)
        self.Pinky = Pinky(self, 23, 6)


    ##############################################
    ###########   Playing Module Here  ###########
    ##############################################

    def retPlayerPos(self):
        return self.mariko.gridpos

    def playingEvent(self):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                self.running = False
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_LEFT):
                    print("Move Left")
                    self.mariko.Move(WEST)
                if (event.key == pygame.K_RIGHT):
                    print("Move Right")
                    self.mariko.Move(EAST)
                if (event.key == pygame.K_DOWN):
                    print("Move Down")
                    self.mariko.Move(SOUTH)
                if (event.key == pygame.K_UP):
                    print("Move Up")
                    self.mariko.Move(NORTH)
            if (event.type == pygame.KEYUP):
                self.mariko.Move(DEFAULT)
    

    def playingUpdate(self):
        self.mariko.Update()
        self.Red.Update()
        self.Black.Update()
        self.Blue.Update()
        self.Pinky.Update()
        self.Fellow.Update()

