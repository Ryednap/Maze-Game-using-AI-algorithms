import pygame
vec = pygame.math.Vector2
#general setting
WIDTH, HEIGHT = 1600, 1024
CELL_WIDTH, CELL_HEIGHT = 32, 32
GRID_WIDTH, GRID_HEIGHT = 50, 32
FPS = 60 # 60 Frame Per Second

#color setting
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)
RED = (255, 0, 0)
DARK_GREEN = (0, 100, 0) 
GREY = (128, 128, 128)

#DIRECTION SETTING
#           x y
EAST = vec(1, 0)
WEST = vec(-1, 0)
NORTH = vec(0, -1)
SOUTH = vec(0, 1)
DEFAULT = vec(0, 0)

# 4 direction vectors
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

#player setting

#enemey setting
OO = int(1e9) # infinity