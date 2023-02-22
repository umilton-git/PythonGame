import pygame
import math
from Settings.raycast_settings import *

class Raycast:
    def __init__(self, game):
        self.game = game
    
    def ray_cast(self):
        ox, oy = self.game.player.pos
        x_map, y_map = self.game.player.map_pos

        ray_angle = self.game.player.angle - half_FOV + 0.0001
        for ray in range(num_rays):
            sin_a = math.sin(ray_angle)
            cos_a = math.cos(ray_angle)

            # Horizontals
            y_hor, dy = (y_map + 1, 1) if sin_a > 0 else (y_map - 1e-6, -1)
            depth_hor = (y_hor - oy) / sin_a
            x_hor = ox + depth_hor * cos_a

            delta_depth = dy / sin_a
            dx =  delta_depth * cos_a

            for i in range(max_depth):
                tile_hor = int(x_hor), int (y_hor)
                if(tile_hor in self.game.map.world_map):
                    break
                x_hor += dx
                y_hor += dy
                depth_hor += delta_depth

            # Verticals
            x_vert, dx = (x_map + 1, 1) if cos_a > 0 else (x_map - 1e-6, -1)
            depth_vert = (x_vert - ox) / cos_a

            y_vert = oy + depth_vert * sin_a

            delta_depth = dx / cos_a
            dy = delta_depth * sin_a

            for i in range(max_depth):
                tile_vert = int (x_vert), int(y_vert)
                if tile_vert in self.game.map.world_map:
                    break
                x_vert += dx
                y_vert += dy
                depth_vert += delta_depth

            # depth
            if depth_vert < depth_hor:
                depth = depth_vert
            else:
                depth = depth_hor
            
            # Draw for debug
            pygame.draw.line(self.game.screen, 'yellow', (50 * ox, 50 * oy),
                            (50 * ox + 50 * depth * cos_a, 50 * oy + 50 * depth * sin_a), 2)
            ray_angle += delta_angle

    def update(self):
        self.ray_cast()