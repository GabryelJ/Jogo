import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, direction):
        super().__init__()
        self.image = pygame.image.load('Entities/sprites/sprite_bullet.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, [100, 100])
        self.rect = self.image.get_rect()
        if (direction == "right"):
            self.rect.center = (x + 58, y + 30)
            self.speed = speed
        else:
            self.rect.center = (x + 7, y + 30)
            self.speed = speed * (-1)

    def update(self):
        self.rect.x += self.speed  # Mover a bala para a direita
        if self.rect.x > 800 or self.rect.x < -100:  # Supondo que a largura da tela seja 800
            self.kill()  # Remover a bala se sair da tela
