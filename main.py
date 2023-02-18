import pygame
import sys
from Resources.Components.Player import player, camera

# Initialize PyGame
pygame.init()

# Set up the window
win_width = 800
win_height = 600
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("PyGame")

# Camera setup
camera_group = camera.Camera()

# Create the player object
player1 = player.Player(400, 300, 5, camera_group)

# Main game loop
running = True
clock = pygame.time.Clock()
FPS = 60

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

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
    win.fill((0, 0, 0))

    # Draw the player
    camera_group.update()
    camera_group.custom_draw(player1)

    # Update the display
    pygame.display.update()

    clock.tick(FPS)

# Clean up
pygame.quit()
