import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, walk_direction, damage=10):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('entities/sprites/sprite_bullet.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, [100, 100])
        if walk_direction == "right":
            self.rect.center = (x + 60, y - 30)
            self.speed = speed
        elif walk_direction == "left":
            self.rect.center = (x - 70, y - 30)
            self.speed = speed * (-1)
        else:
            self.rect.center = (x + 35, y)
            self.speed = 500
        self.damage = damage


        hitbox_width = 20
        hitbox_height = 30

        #Calcule a posição X e Y para centralizar a hitbox
        hitbox_x = self.rect.x + (self.rect.width - hitbox_width) // 2
        hitbox_y = self.rect.y + (self.rect.height - hitbox_height) // 2

        # Defina a hitbox personalizada centralizada
        self.hitbox = pygame.Rect(hitbox_x, hitbox_y, hitbox_width, hitbox_height)

    def update(self):
        if self.speed == 500:
            self.rect.y -= 10
        else:
            self.rect.x += self.speed
        if self.rect.x > 800 or self.rect.x < -100 or self.rect.y < 0 or self.rect.y > 600:
            self.kill()
        self.image = pygame.transform.scale(self.image, [100, 98])
        self.rect = self.image.get_rect(topleft=self.rect.topleft)

        hitbox_width = 20
        hitbox_height = 30

         #Calcule a posição X e Y para centralizar a hitbox
        hitbox_x = self.rect.x + (self.rect.width - hitbox_width) // 2
        hitbox_y = self.rect.y + (self.rect.height - hitbox_height) // 2

        # Defina a hitbox personalizada centralizada
        self.hitbox = pygame.Rect(hitbox_x, hitbox_y, hitbox_width, hitbox_height)

    def draw(self, screen):

        screen.blit(self.image, self.rect.topleft)
        # Desenhe o rect em vermelho para visualização
        #pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)

        # Desenhe a hitbox em azul para visualização
        #pygame.draw.rect(screen, (0, 0, 255), self.hitbox, 2)
