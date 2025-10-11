import pygame
import sys

result = pygame.init()
print(result)

# Constants
GRID_SIZE = 40
GRID_WIDTH = 15
GRID_HEIGHT = 10
SCREEN_WIDTH = GRID_WIDTH * GRID_SIZE
SCREEN_HEIGHT = GRID_HEIGHT * GRID_SIZE
FPS = 60


# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PLAYER_COLOR = (255, 0, 0)  # Red player
GRASS_COLOR = (34, 139, 34)  # Green grass
WATER_COLOR = (0, 105, 148)  # Blue water
TREE_COLOR = (0, 100, 0)     # Dark green trees
MOUNTAIN_COLOR = (139, 137, 137)  # Gray mountains

# Terrain types
GRASS = 0
WATER = 1
TREE = 2
MOUNTAIN = 3

screen = pygame.display.set_mode(SCREEN_WIDTH, SCREEN_HEIGHT)

def create_grid():
    grid = []
    for y in range 