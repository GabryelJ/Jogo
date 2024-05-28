import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # inicializa Sprite
        self.image = pygame.image.load('Entities/sprites/sprite_0.png')
        self.rect = pygame.Rect(100, 100, 100, 100)
        self.current_image = 0
        # lista contem sequencia de imagens para animação do boneco correndo.
        self.sprite_running = [pygame.image.load('Entities/sprites/sprite_0.png'),
                               pygame.image.load('Entities/sprites/sprite_1.png'),
                               pygame.image.load('Entities/sprites/sprite_2.png'),
                               pygame.image.load('Entities/sprites/sprite_3.png')]

    def update(self, *args):
        def player_movement(self):
            # key = pygame.key.get_pressed()
            self.current_image = (self.current_image + 1) % 4
            self.image = self.sprite_running[self.current_image]
            self.image = pygame.transform.scale(self.image, [100, 100])

        player_movement(self)
