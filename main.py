import pygame
from Resources.Components.Player import player

# Initialize PyGame
pygame.init()

# Set up the window
win_width = 800
win_height = 600
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("PyGame")

# Create the player object
player1 = player.Player(400, 300, 5)

# Main game loop
running = True
clock = pygame.time.Clock()
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player1.move(-1, 0)
    if keys[pygame.K_RIGHT]:
        player1.move(1, 0)
    if keys[pygame.K_UP]:
        player1.move(0, -1)
    if keys[pygame.K_DOWN]:
        player1.move(0, 1)

    # Fill the window with white
    win.fill((255, 255, 255))

    # Draw the player
    player1.draw(win)

    # Update the display
    pygame.display.update()

    clock.tick(60)

# Clean up
pygame.quit()
