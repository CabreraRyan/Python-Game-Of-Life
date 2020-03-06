import sys
import os
import copy
import random
import pygame

class Game:
    def __init__(self):
        """
        Initialize everything
        """ 

        os.environ['SDL_VIDEO_WINDOW_POS'] = "800, 300" # Window Position on Start

        # Initialize Pygame display
        pygame.init()
        pygame.display.set_caption('Game Of Life')
        self.size = WIDTH, HEIGHT = 640, 480
        self.BLACK = 0, 0, 0 # DEAD CELL COLOR
        self.ORANGE = 255, 165, 0 # ALIVE CELL COLOR
        self.screen = pygame.display.set_mode(self.size)

        # Initialize Grid
        self.col = WIDTH // 10
        self.row = HEIGHT // 10
        self.random_grid()

        self.max_fps = 10

    def random_grid(self):
        """
        Initialize a random grid
        0 = DEAD CELL
        1 = ALIVE CELL
        """
        self.grid = []
        for row in range(self.col):
            self.grid.append([])
            for col in range(self.row):
                self.grid[row].append(random.randint(0,1))

        return self.grid

    def draw_grid(self):
        """
        Draw the grid into the screen
        """
        for col in range(self.col):
            for row in range(self.row):
                x = (col * 10)
                y = (row * 10)
                if self.grid[col][row] == 1:
                    pygame.draw.circle(self.screen, self.ORANGE, (x, y), 5)
                else:
                    pygame.draw.circle(self.screen, self.BLACK, (x, y), 5)

        pygame.display.flip()

    def check_cell(self, row, col):
        try:
            cell_value = self.grid[row][col]
        except:
            cell_value = 0
        return cell_value

    def update_grid(self):
        self.newGrid = copy.deepcopy(self.grid)
        for i in range(self.col):
            for j in range(self.row):
                total = 0
                total += self.check_cell(i - 1, j - 1)
                total += self.check_cell(i - 1, j)
                total += self.check_cell(i - 1, j + 1)
                total += self.check_cell(i, j - 1)
                total += self.check_cell(i, j + 1)
                total += self.check_cell(i + 1, j - 1)
                total += self.check_cell(i + 1, j)
                total += self.check_cell(i + 1, j + 1)
        
        # apply Conway's rules 
                if self.grid[i][j]  == 1: 
                    if (total < 2) or (total > 3): 
                        self.newGrid[i][j] = 0
                    elif total == 3:
                        self.newGrid[i][j] = 1
                else: 
                    if total == 3: 
                        self.newGrid[i][j] = 1
        
        self.grid[:] = self.newGrid[:]


    def run(self):
        """
        Main loop of the game
        """

        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

            self.screen.fill(self.BLACK)
            self.update_grid()
            self.draw_grid()

            clock.tick(self.max_fps)


if __name__ == "__main__":
    game = Game()
    game.run()