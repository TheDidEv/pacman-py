import sys

import pygame

from constants import *
from ghosts import Ghost
from maze import Maze
from pacman import Pacman

pygame.init()

SCREEN_WIDTH = MAZE_WIDTH * 40
SCREEN_HEIGHT = MAZE_HEIGHT * 40
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

pacman = Pacman(1 * 40, 1 * 40)
maze = Maze()

agg_x = 9 * 40
agg_y = 9 * 40
rand_x = 10 * 40
rand_y = 10 * 40
caut_x = 11 * 40
caut_y = 11 * 40

ghosts = [
    Ghost(agg_x, agg_y, RED, 'aggressive'),
    Ghost(rand_x, rand_y, GREEN, 'random'),
    Ghost(caut_x, caut_y, PINK, 'cautious') 
]

ghost_move_counter = 0
ghost_move_interval = 40
min_ghost_move_interval = 15
difficulty_timer = 0
difficulty_increase_interval = 5000 

def game_loop():
    global ghost_move_counter, ghost_move_interval, difficulty_timer
    running = True

    while running:
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

        pacman.update(maze, events)

        maze.remove_pellet(pacman)

        if maze.all_pellets_collected():
            print("Ви виграли!")
            running = False

        if ghost_move_counter % ghost_move_interval == 0:
            for ghost in ghosts:
                ghost.update(maze, pacman)
        ghost_move_counter += 1

        for ghost in ghosts:
            if pacman.grid_x == ghost.grid_x and pacman.grid_y == ghost.grid_y:
                print("Пакмена спіймали! Ви програли.")
                running = False

        screen.fill(BLACK)

        maze.draw(screen)

        pacman.draw(screen)

        for ghost in ghosts:
            ghost.draw(screen)

        pygame.display.flip()

        clock.tick(FPS)


if __name__ == "__main__":
    game_loop()
