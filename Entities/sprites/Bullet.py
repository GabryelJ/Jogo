import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.image = pygame.image.load('Entities/sprites/sprite_4.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (x+69, y+20)
        self.speed = speed

    def update(self):
        self.rect.x += self.speed  # Mover a bala para a direita
        if self.rect.x > 800:  # Supondo que a largura da tela seja 800
            self.kill()  # Remover a bala se sair da tela
