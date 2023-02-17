import pygame

# Initialize PyGame
pygame.init()

# Set up the window
win_width = 800
win_height = 600
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("PyGame")

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the window with white
    win.fill((0, 0, 0))

    # Update the display
    pygame.display.update()

# Clean up
pygame.quit()
