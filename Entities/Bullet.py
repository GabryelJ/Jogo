import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, walk_direction):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Entities/sprites/sprite_bullet.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, [100, 100])
        if (walk_direction == "right"):
            self.rect.center = (x + 25, y - 5)
            self.speed = speed
        elif(walk_direction == "left"):
            #self.image = pygame.transform.flip(pygame.image.load('Entities/sprites/sprite_bullet.png').convert_alpha(), True,False)
            self.rect.center = (x - 27, y - 5)
            self.speed = speed * (-1)
        else:
            #self.image = pygame.transform.flip(pygame.image.load('Entities/sprites/sprite_bullet.png').convert_alpha(), True,False)
            self.rect.center = (x + 35, y)
            self.speed = 500

    def update(self):
        if(self.speed == 500):
            self.rect.y -= 10
        else:
            self.rect.x += self.speed  # Mover a bala para a direita

        if self.rect.x > 800 or self.rect.x < -100:  # para largura de tela 800
            self.kill()  # Remover a bala se sair da tela
        if self.rect.y < 0 or self.rect.y > 600:
            self.kill()
