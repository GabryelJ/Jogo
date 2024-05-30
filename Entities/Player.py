import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.speed = 4  # velocidade do boneco
        self.gravity = 4  # gravidade do boneco
        pygame.sprite.Sprite.__init__(self)  # inicializa Sprite
        # carrega imagem e convert_alpha() mantem os pixels transparentes
        self.image = pygame.image.load('Entities/sprites/sprite_0.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.current_image = 0
        # lista contem sequencia de imagens para animação do boneco correndo.
        self.sprite_running = [pygame.image.load('Entities/sprites/sprite_0.png').convert_alpha(),
                               pygame.image.load('Entities/sprites/sprite_1.png').convert_alpha(),
                               pygame.image.load('Entities/sprites/sprite_2.png').convert_alpha(),
                               pygame.image.load('Entities/sprites/sprite_3.png').convert_alpha()]

    def player_movement(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_d]:  # se a tecla d for pressionada move para direita
            self.rect[0] += self.speed
            self.walk()
        if key[pygame.K_a]:  # se a tecla a for pressionada move para esquerda
            self.rect[0] -= self.speed
            self.walk()
        #TODO: animação de atirar + tiro


        if not any (key):
            self.image = self.sprite_running[0]

        self.image = pygame.transform.scale(self.image, [100, 98])

    def walk(self):
        self.current_image = (self.current_image + 0.2) % 4
        self.image = self.sprite_running[int(self.current_image)]

    def update(self, *args):

        self.player_movement()

        self.rect[1] += self.gravity #
