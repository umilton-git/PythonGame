import math

# General

RES = WIDTH, HEIGHT = 800, 600
h_width = WIDTH // 2
h_height = HEIGHT // 2
FPS = 60

# Player

player_pos = 6.5, 5
player_angle = 0
player_speed = 0.002
player_rot_speed = 0.001
player_size_scale = 60

# Raycasting

FOV = math.pi / 3
half_FOV = FOV / 2
num_rays = WIDTH // 2
half_num_rays = num_rays // 2
delta_angle = FOV / num_rays
max_depth = 20

screen_dist = h_width / math.tan(half_FOV)
scale = WIDTH // num_rays

texture_size = 256
h_texture_size = texture_size // 2

floor_color = (21, 1, 56)
