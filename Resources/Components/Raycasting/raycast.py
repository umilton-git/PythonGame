import pygame
import math
from Settings.raycast_settings import *

class Raycast:
    def __init__(self, game):
        self.game = game
        self.ray_casting_result = []
        self.objects_to_render = []
        self.textures = self.game.object_renderer.wall_textures

    def get_objects_to_render(self):
        self.objects_to_render = []
        for ray, values in enumerate(self.ray_casting_result):
            depth, proj_height, texture, offset = values

            if proj_height < HEIGHT:
                wall_column = self.textures[texture].subsurface(
                    offset * (texture_size - scale), 0, scale, texture_size
                )
                wall_column = pygame.transform.scale(wall_column, (scale, proj_height))
                wall_pos = (ray * scale, h_height - proj_height // 2)
            else:
                texture_height = texture_size * HEIGHT / proj_height
                wall_column = self.textures[texture].subsurface(
                    offset * (texture_size - scale), h_texture_size - texture_height // 2,
                    scale, texture_height
                )
                wall_column = pygame.transform.scale(wall_column, (scale, HEIGHT))
                wall_pos = (ray * scale, 0)

            self.objects_to_render.append((depth, wall_column, wall_pos))
    
    def ray_cast(self):
        self.ray_casting_result = []
        ox, oy = self.game.player.pos
        x_map, y_map = self.game.player.map_pos

        texture_vert, texture_hor = 1, 1

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
                    texture_hor = self.game.map.world_map[tile_hor]
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
                    texture_vert = self.game.map.world_map[tile_vert]
                    break
                x_vert += dx
                y_vert += dy
                depth_vert += delta_depth

            # depth, texture offset
            if depth_vert < depth_hor:
                depth, texture = depth_vert, texture_vert
                y_vert %= 1
                offset = y_vert if cos_a > 0 else (1 - y_vert)
            else:
                depth, texture = depth_hor, texture_hor
                x_hor %= 1
                offset = (1 - x_hor) if sin_a > 0 else x_hor

            # remove fishbowl effect
            depth *= math.cos(self.game.player.angle - ray_angle)
            
            # projection
            proj_height = screen_dist / (depth + 0.0001)

            # draw walls
            #color = [255 / (1 + depth ** 5 * 0.00002)] * 3
            #pygame.draw.rect(self.game.screen, color,
            #                 (ray * scale, h_height - proj_height // 2, scale, proj_height))

            # ray casting result
            self.ray_casting_result.append((depth, proj_height, texture, offset))

            ray_angle += delta_angle

    def update(self):
        self.ray_cast()
        self.get_objects_to_render()