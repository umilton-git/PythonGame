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
    if keys[pygame.K_LEFT] and player1.rect.bottomleft[0] - 1 >= 0:
        player1.move(-1, 0)
    if keys[pygame.K_RIGHT] and player1.rect.topright[0] + 1 <= pygame.display.get_surface().get_size()[0]:
        player1.move(1, 0)
    if keys[pygame.K_UP] and player1.rect.top >= 1:
        player1.move(0, -1)
    if keys[pygame.K_DOWN] and player1.rect.bottom <= pygame.display.get_surface().get_size()[1]:
        player1.move(0, 1)
    if keys[pygame.K_a]:
        print(player1.rect.centerx)

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
