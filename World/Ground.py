import pygame
from Program.constants import WIDTH, HEIGHT


class Ground(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # inicializa Sprite
        self.ground_height = 80
        self.image = pygame.image.load('World/sprites/sprite_ground_0.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (WIDTH, self.ground_height))  # 80 é altura de ground
        self.rect = self.image.get_rect()
        self.rect.x = 0  # posicao x do chao
        self.rect.y = HEIGHT - self.ground_height  # posicao y do chão
