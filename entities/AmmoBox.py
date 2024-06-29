import pygame

class AmmoBox(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.gravity = 1
        self.on_ground = False
        self.image = pygame.image.load('entities/sprites/sprite_ammo_box.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, [30,30])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def physic(self):
        if not self.on_ground:
            self.rect.y += self.gravity


    def update(self):
        self.physic()
