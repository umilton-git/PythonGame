import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, group):
        super().__init__(group)
        player_image = pygame.image.load(
            "Resources/Sprites/Player/AIM.png")
        scaled_image = pygame.transform.scale(player_image, (30,57))
        self.image = scaled_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def move(self, dx, dy):
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
