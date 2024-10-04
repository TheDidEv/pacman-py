import pygame

YELLOW = (255, 255, 0)
PACMAN_SIZE = 40
CELL_SIZE = 40


class Pacman:
    def __init__(self, x, y):
        self.grid_x = x // CELL_SIZE
        self.grid_y = y // CELL_SIZE
        self.moving = False

    def update(self, maze, events):
        for event in events:
            if event.type == pygame.KEYDOWN and not self.moving:
                if event.key == pygame.K_LEFT:
                    self.try_move(-1, 0, maze)
                elif event.key == pygame.K_RIGHT:
                    self.try_move(1, 0, maze)
                elif event.key == pygame.K_UP:
                    self.try_move(0, -1, maze)
                elif event.key == pygame.K_DOWN:
                    self.try_move(0, 1, maze)

            if event.type == pygame.KEYUP:
                self.moving = False

    def try_move(self, dx, dy, maze):
        new_x = self.grid_x + dx
        new_y = self.grid_y + dy

        if 0 <= new_x < len(maze.grid[0]) and 0 <= new_y < len(maze.grid):
            if maze.grid[new_y][new_x] == 0:
                self.grid_x = new_x
                self.grid_y = new_y
                self.moving = True  

    def draw(self, screen):
        pixel_x = self.grid_x * CELL_SIZE
        pixel_y = self.grid_y * CELL_SIZE

        pygame.draw.circle(screen, YELLOW, (pixel_x + CELL_SIZE // 2, pixel_y + CELL_SIZE // 2), PACMAN_SIZE // 2)
