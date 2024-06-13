import pygame

class AmmoBox(pygame.sprite.Sprite):
    def __init__(self, x, y,playergrp):#gerar a aleatoriedade de onde ela vai surgir na main
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Entities/sprites/sprite_1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.player_group=playergrp

    def update(self):
        for player in self.player_group:
            if pygame.sprite.collide_rect(self, player):
                if player.ammunition < 10:
                    player.ammunition = 10
                    #self.kill()
