import pygame

class Bomb(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('entities/sprites/sprite_bomb.png').convert_alpha()  # Assumindo que você tenha uma imagem de bomba
        self.image = pygame.transform.scale(self.image, [30, 30])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.gravity = 3
        self.on_ground = False

        self.mask = pygame.mask.from_surface(self.image)

    def physic(self):
        if not self.on_ground:
            self.rect.y += self.gravity

    def update(self):
        self.physic()
