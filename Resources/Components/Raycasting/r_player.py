from Settings.raycast_settings import *

import pygame
import math

class RaycastPlayer:
    def __init__(self, game):
        self.game = game
        self.x, self.y = player_pos
        self.angle = player_angle

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = player_speed * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            dx += speed_cos
            dy += speed_sin
        if keys[pygame.K_s]:
            dx += -speed_cos
            dy += -speed_sin
        if keys[pygame.K_a]:
            dx += speed_sin
            dy += -speed_cos
        if keys[pygame.K_d]:
            dx += -speed_sin
            dy += speed_cos
        
        self.check_wall_collision(dx, dy)

        if keys[pygame.K_LEFT]:
            self.angle -= player_rot_speed * self.game.delta_time
        if keys[pygame.K_RIGHT]:
            self.angle += player_rot_speed * self.game.delta_time
        self.angle %= math.tau

    def check_wall(self, x, y):
        return (x, y) not in self.game.map.world_map

    def check_wall_collision(self, dx, dy):
        if self.check_wall(int(self.x + dx), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy)):
            self.y += dy

    def draw(self):
        #pygame.draw.line(self.game.screen, 'yellow', (self.x * 50, self.y * 50),
        #                (self.x * 50 + WIDTH * math.cos(self.angle),
        #                 self.y * 50 + WIDTH * math.sin(self.angle)), 2)
        pygame.draw.circle(self.game.screen, 'green', (self.x * 50, self.y * 50), 10)

    def update(self):
        self.movement()

    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)