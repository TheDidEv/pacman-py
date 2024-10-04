import random

import pygame

from constants import CELL_SIZE, GHOST_SIZE
from search_algos import a_star, bfs


class Ghost:
    def __init__(self, x, y, color, behavior, speed=1):
        self.grid_x = x // CELL_SIZE
        self.grid_y = y // CELL_SIZE
        self.color = color
        self.behavior = behavior
        self.speed = speed
        self.path = []

    def update(self, maze, pacman):
        if self.behavior == 'aggressive':
            self.path = a_star(maze, (self.grid_x, self.grid_y), (pacman.grid_x, pacman.grid_y))
        elif self.behavior == 'random':
            self.random_move(maze)
        elif self.behavior == 'cautious':
            if self.distance_to_pacman(pacman) < 5:
                self.path = bfs(maze, (self.grid_x, self.grid_y), (pacman.grid_x, pacman.grid_y))
            else:
                self.random_move(maze)

        if self.path:
            next_x, next_y = self.path.pop(0)
            self.grid_x, self.grid_y = next_x, next_y

    def random_move(self, maze):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            new_x = self.grid_x + dx
            new_y = self.grid_y + dy
            if len(maze.grid[0]) > new_x >= 0 == maze.grid[new_y][new_x] and 0 <= new_y < len(maze.grid):
                self.grid_x, self.grid_y = new_x, new_y
                break

    def distance_to_pacman(self, pacman):
        return abs(self.grid_x - pacman.grid_x) + abs(self.grid_y - pacman.grid_y)

    def draw(self, screen):
        pixel_x = self.grid_x * CELL_SIZE
        pixel_y = self.grid_y * CELL_SIZE
        pygame.draw.circle(screen, self.color, (pixel_x + CELL_SIZE // 2, pixel_y + CELL_SIZE // 2), GHOST_SIZE // 2)
