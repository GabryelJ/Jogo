import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed,direcao):
        super().__init__()
        if (direcao== "direita"):
            self.image = pygame.image.load('Entities/sprites/sprite_4.png').convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.center = (x+69, y+20)
            self.speed = speed
        else:
            #self.image = pygame.image.load('Entities/sprites/sprite_4.png').convert_alpha()
            self.image = pygame.transform.flip(pygame.image.load('Entities/sprites/sprite_4.png').convert_alpha(), True,False)
            self.rect = self.image.get_rect()
            self.rect.center = (x - 5, y + 20)
            self.speed = speed * (-1)

    def update(self):
        self.rect.x += self.speed  # Mover a bala para a direita
        if self.rect.x > 800 or self.rect.x < -100:  # Supondo que a largura da tela seja 800
            self.kill()  # Remover a bala se sair da tela
