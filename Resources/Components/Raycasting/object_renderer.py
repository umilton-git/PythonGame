import pygame
from Settings.raycast_settings import *

class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()
        self.sky_image = self.get_texture('Resources/Sprites/Placeholder/sky.png', (WIDTH, h_height))
        self.sky_offset = 0

    def draw(self):
        self.draw_background()
        self.render_game_objects()

    def draw_background(self):
        #self.sky_offset = (self.sky_offset + 4.5 * self.game.player.angle) % WIDTH
        self.screen.blit(self.sky_image, (-self.sky_offset, 0))
        self.screen.blit(self.sky_image, (-self.sky_offset * WIDTH, 0))

        pygame.draw.rect(self.screen, floor_color, (0, h_height, WIDTH, HEIGHT))

    def render_game_objects(self):
        list_objects = self.game.raycasting.objects_to_render
        for depth, image, pos in list_objects:
            self.screen.blit(image, pos)

    @staticmethod
    def get_texture(path, res=(texture_size, texture_size)):
        texture = pygame.image.load(path).convert_alpha()
        return pygame.transform.scale(texture, res)

    def load_wall_textures(self):
        return {
            1: self.get_texture('Resources/Sprites/Placeholder/wall.png')
        }