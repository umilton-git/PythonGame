import math

# General

RES = WIDTH, HEIGHT = 800, 600
FPS = 60

# Player

player_pos = 1.5, 5
player_angle = 0
player_speed = 0.002
player_rot_speed = 0.001

# Raycasting

FOV = math.pi / 3
half_FOV = FOV / 2
num_rays = WIDTH // 2
half_num_rays = num_rays // 2
delta_angle = FOV / num_rays
max_depth = 20
