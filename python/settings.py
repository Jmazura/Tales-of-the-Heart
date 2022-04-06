import pygame, sys

WIN_SIZE = [800, 600]
FPS = 30
TITLE = "Tales of the heart"

#Grid system for the layout of the Menu
GRID_SIZE = 32
GRID = []

for i in range(int(WIN_SIZE[0]/GRID_SIZE)+1):
    GRID.append([])
    for j in range(int(WIN_SIZE[1]/GRID_SIZE)+1):
        GRID[i].append([i*GRID_SIZE,j*GRID_SIZE])

print(len(GRID), len(GRID[0]))
