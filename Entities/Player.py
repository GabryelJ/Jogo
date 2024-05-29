import pygame
from Program.constants import SPEED, GAME_SPEED


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # inicializa Sprite
        self.image = pygame.image.load('Entities/sprites/sprite_0.png').convert_alpha()
        self.rect = pygame.Rect(100, 100, 100, 100)
        self.current_image = 0
        # lista contem sequencia de imagens para animação do boneco correndo.
        self.sprite_running = [pygame.image.load('Entities/sprites/sprite_0.png').convert_alpha(),
                               pygame.image.load('Entities/sprites/sprite_1.png').convert_alpha(),
                               pygame.image.load('Entities/sprites/sprite_2.png').convert_alpha(),
                               pygame.image.load('Entities/sprites/sprite_3.png').convert_alpha()]

    def update(self, *args):
        def player_movement(self):
            key = pygame.key.get_pressed()
            if key[pygame.K_d]:  # se a tecla d for pressionada move para direita
                self.rect[0] += GAME_SPEED
            if key[pygame.K_a]:  # se a tecla a for pressionada move para esquerda
                self.rect[0] -= GAME_SPEED
            self.current_image = (self.current_image + 1) % 4
            self.image = self.sprite_running[self.current_image]
            self.image = pygame.transform.scale(self.image, [100, 100])

        player_movement(self)
