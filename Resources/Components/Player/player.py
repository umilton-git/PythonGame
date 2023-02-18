import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, group):
        super().__init__(group)
        self.image = pygame.image.load(
            "Resources/Sprites/Placeholder/LilDude.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def move(self, dx, dy):
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)
