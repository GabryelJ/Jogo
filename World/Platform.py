import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill((139, 69, 19))  # Cor marrom para a plataforma
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
