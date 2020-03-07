"""
 Pygame base template for opening a window
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

# Set the width and height of the screen [width, height]
width=20
height=20
margin=5
size = (255, 255)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

grid = []
# Loop for each row
for row in range(10):
    # For each row, create a list that will
    # represent an entire row
    grid.append([])
    # Loop for each column
    for column in range(10):
        # Add a the number zero to the current row
        grid[row].append(0)
grid[1][5] = 1

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONUP:
            print("Click: " + str(pygame.mouse.get_pos()))
            pos = pygame.mouse.get_pos()
            column = pos[0] // (height + 5)
            row = pos[1] // (width + 5)
            print("Row: " + str(row) + " Column: " + str(column))
            grid[row][column] = 1

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)

    # --- Create grid of numbers
    # Create an empty list

    colour = WHITE
    # --- Drawing code should go here
    upper = margin
    for row in range(10):
        left = margin
        for column in range(10):
            if grid[row][column] == 1:
                colour = GREEN
            else:
                colour = WHITE
            pygame.draw.rect(screen, colour, [left, upper, width, height])
            left = left + width + margin
        upper = upper + height + margin

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()