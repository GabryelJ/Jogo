import pygame
from Program.constants import WIDTH, GROUND_HEIGHT, HEIGHT


class Ground(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # inicializa Sprite
        self.image = pygame.image.load('World/sprite_ground_0.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (WIDTH, GROUND_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect[0] = 0  # posicao x do chao
        self.rect[1] = HEIGHT - GROUND_HEIGHT  # posicao y do chão
