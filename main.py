import pygame
import sys
from Resources.Components.Player import player, camera
from Settings.main_settings import *

# Initialize PyGame
pygame.init()

# Set up the window
win = pygame.display.set_mode(RES)

# Camera setup
camera_group = camera.Camera()

# Create the player object

player1 = player.Player(400, 300, p_speed, camera_group)

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

    # Handle input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player1.rect.bottomleft[0] - 1 >= 1:
        player1.move(-1, 0)
    if keys[pygame.K_RIGHT] and player1.rect.topright[0] + 1 <= pygame.display.get_surface().get_size()[0] - 1:
        player1.move(1, 0)
    if keys[pygame.K_UP] and player1.rect.top >= 2:
        player1.move(0, -1)
    if keys[pygame.K_DOWN] and player1.rect.bottom <= pygame.display.get_surface().get_size()[1] - 3:
        player1.move(0, 1)
    if keys[pygame.K_x]:
        player1.speed = p_speed * 2
    else:
        player1.speed = p_speed

    # Fill the window with white
    win.fill((0, 0, 0))

    # Draw the player
    camera_group.update()
    camera_group.custom_draw(player1)

    # Update the display
    pygame.display.update()

    clock.tick(FPS)
    pygame.display.set_caption(f'{clock.get_fps() :.1f}')

# Clean up
pygame.quit()
