import random

import pygame

from constants import CELL_SIZE, PATH_COLOR, BLUE, YELLOW


class Maze:
    def __init__(self, level=1):
        self.level = level
        self.grid = self.generate_dynamic_maze(level)
        self.pellets = self.generate_pellets() 

    def generate_dynamic_maze(self, level):
        base_maze = [
            [1] * 18,
            [1] + [0] * 16 + [1],
            [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1],
            [1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
            [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1],
            [1] + [0] * 16 + [1],
            [1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
            [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
            [1] + [0] * 16 + [1],
            [1] * 18
        ]

        for _ in range(level): 
            for _ in range(random.randint(3, 6)): 
                row = random.randint(1, len(base_maze) - 2)
                col = random.randint(1, len(base_maze[0]) - 2)
                if base_maze[row][col] == 0:  
                    base_maze[row][col] = 1

        return base_maze

    def generate_pellets(self):
        pellets = []
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.grid[row][col] == 0:  
                    pellets.append((row, col))
        return pellets

    def draw(self, screen):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                color = BLUE if self.grid[row][col] == 1 else PATH_COLOR
                pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        for pellet in self.pellets:
            pygame.draw.circle(screen, YELLOW,
                               (pellet[1] * CELL_SIZE + CELL_SIZE // 2, pellet[0] * CELL_SIZE + CELL_SIZE // 2), 5)

    def remove_pellet(self, pacman):
        pacman_position = (pacman.grid_y, pacman.grid_x)
        if pacman_position in self.pellets:
            self.pellets.remove(pacman_position)

    def all_pellets_collected(self):
        return len(self.pellets) == 0
