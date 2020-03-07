import sys
import os
import copy
import pygame

class Game:

    """ 
    TODO:
    - Add Comments
    - Add Main Menu
    """

    def __init__(self):
        """
        Initialize everything
        """

        os.environ['SDL_VIDEO_WINDOW_POS'] = "800, 300" # Window Position on Start

        # Initialize Pygame display
        pygame.init()
        pygame.display.set_caption('Game Of Life')
        self.size = WIDTH, HEIGHT = 605, 455
        self.BLACK = 0, 0, 0 
        self.ORANGE = 255, 165, 0 # ALIVE CELL COLOR
        self.WHITE = 255, 255, 255 # DEAD CELL COLOR
        self.screen = pygame.display.set_mode(self.size)

        # Draw Test Grid
        self.margin = 5
        self.cell_height = 20
        self.cell_width = 20

        # Initialize Grid
        self.col = WIDTH // (self.cell_width + self.margin)
        self.row = HEIGHT // (self.cell_height + self.margin)
        self.grid = self.init_grid()


        # Game State
        # 0: Player Control
        # 1: Looping Generation
        # 2: Pause
        self.game_state = 0
        self.paused = False

        # FPS
        self.max_fps = 5

    def init_grid(self):
        grid = []
        for row in range(self.row):
            grid.append([])
            for _ in range(self.col):
                grid[row].append(0)

        return grid

    def check_cell(self, row, col):
        try:
            cell_value = self.grid[row][col]
        except:
            cell_value = 0
        return cell_value

    def update_grid(self):
        self.newGrid = copy.deepcopy(self.grid)
        for i in range(self.row):
            for j in range(self.col):
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
                if self.grid[i][j] == 1: 
                    if (total < 2) or (total > 3): 
                        self.newGrid[i][j] = 0
                    elif total == 3:
                        self.newGrid[i][j] = 1
                else: 
                    if total == 3: 
                        self.newGrid[i][j] = 1
        
        self.grid[:] = self.newGrid[:]

    def game_state_handler(self):
        if self.game_state == 0:
            self.paused = False
        if self.game_state == 1:
            self.update_grid()
            self.paused = False
        if self.game_state == 2:
            self.paused = True

    def reset_grid(self):
        self.game_state = 0
        self.grid = self.init_grid()
        self.paused = False
        print("Game Has been Reset!")

    def event_handler(self):

        """ 
        Keyboard Shortcuts:
        Space: Start // Pause // Resume
        R: Reset
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif self.game_state <= 0:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        print("You pressed space!")
                        self.game_state = 1
                    elif event.key == pygame.K_r:
                        self.reset_grid()
                elif event.type == pygame.MOUSEBUTTONUP:
                    print("Click: " + str(pygame.mouse.get_pos()))
                    pos = pygame.mouse.get_pos()
                    column = pos[0] // (self.cell_height + 5)
                    row = pos[1] // (self.cell_width + 5)
                    print("Row: " + str(row) + " Column: " + str(column))
                    self.grid[row][column] = 1
                    print(str(self.game_state))
            elif self.game_state == 1:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        print("You pressed space!")
                        self.game_state = 2
                    if event.key == pygame.K_r:
                        self.reset_grid()
            elif self.game_state == 2:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        print("You pressed space!")
                        self.game_state = 1
                    if event.key == pygame.K_r:
                        self.reset_grid()
                            
    def cell_onclick(self):
        colour = self.WHITE
        # --- Drawing code should go here
        upper = self.margin
        for row in range(self.row):
            left = self.margin
            for column in range(self.col):
                if self.grid[row][column] == 1:
                    colour = self.ORANGE
                else:
                    colour = self.WHITE
                pygame.draw.rect(self.screen, colour, [left, upper, self.cell_width, self.cell_height])
                left = left + self.cell_width + self.margin
            upper = upper + self.cell_height + self.margin

    def run(self):
        """
        Main loop of the game
        """

        clock = pygame.time.Clock()

        while True:
            self.event_handler()
            self.game_state_handler()
            if not self.paused:
                self.screen.fill(self.BLACK)
                self.cell_onclick()
                #self.update_grid()
                pygame.display.flip()

            clock.tick(self.max_fps)

if __name__ == "__main__":
    game = Game()
    game.run()