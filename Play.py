import pygame
from Setting import *
from Mariko import *

vector = pygame.math.Vector2

class Play:
    def __init__(self, App):
        self.App = App
        self.mariko = Mariko(App, 8, 26)
        self.grid = self.App.grid


    def Event(self):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                self.App.running = False
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

    

    def Update(self):
        self.mariko.Update()

    def draw(self):
        self.mariko.draw()
        pygame.display.update()

    

            