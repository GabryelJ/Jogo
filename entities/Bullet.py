import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, walk_direction, damage=10):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('entities/sprites/sprite_bullet.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, [100, 100])
        if walk_direction == "right":
            self.rect.center = (x + 60, y - 5)
            self.speed = speed
        elif walk_direction == "left":
            self.rect.center = (x - 60, y - 5)
            self.speed = speed * (-1)
        else:
            self.rect.center = (x + 35, y)
            self.speed = 500
        self.damage = damage

    def update(self):
        if self.speed == 500:
            self.rect.y -= 10
            self.rect = self.image.get_rect(topleft=self.rect.topleft)
        else:
            self.rect.x += self.speed
            self.rect = self.image.get_rect(topleft=self.rect.topleft)
        if self.rect.x > 800 or self.rect.x < -100 or self.rect.y < 0 or self.rect.y > 600:

            self.kill()

    def draw(self, screen):
        # Desenhe a imagem do jogador
        screen.blit(self.image, self.rect.topleft)
        # Desenhe o rect em vermelho para visualização
        pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)
