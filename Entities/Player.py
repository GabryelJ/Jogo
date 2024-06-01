import pygame
from Entities.Bullet import Bullet
class Player(pygame.sprite.Sprite):

    def __init__(self, bullet_group):
        self.speed = 4  # velocidade do boneco
        self.gravity = 0.3 # gravidade do boneco
        self.vertical_velocity = 0 # Velocidade vertical inicial
        self.jump_speed = -40 # Velocidade inicial do salto (negativa para subir)
        self.on_ground = True  # Para verificar se o jogador está no chão
        pygame.sprite.Sprite.__init__(self)  # inicializa Sprite
        # carrega imagem e convert_alpha() mantem os pixels transparentes
        self.image = pygame.image.load('Entities/sprites/sprite_0.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.current_image = 0
        # lista contem sequencia de imagens para animação do boneco correndo.
        self.sprite_running_right = [pygame.image.load('Entities/sprites/sprite_0.png').convert_alpha(),
                               pygame.image.load('Entities/sprites/sprite_1.png').convert_alpha(),
                               pygame.image.load('Entities/sprites/sprite_2.png').convert_alpha(),
                               pygame.image.load('Entities/sprites/sprite_3.png').convert_alpha(),
                               pygame.image.load('Entities/sprites/sprite_4.png').convert_alpha()]
        #Fazer a mesma cois do running_right só que para _left
        self.sprite_running_left = [pygame.transform.flip(img, True, False) for img in self.sprite_running_right]
        self.is_shooting = False
        self.shooting_timer = 0
        self.shooting_duration = 10
        self.bullet_group = bullet_group
        self.contadortiros=5
        self.walk_direction = "right"

    def player_movement(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_d]:  # se a tecla d for pressionada move para _right
            self.walk_direction = "right"
            self.rect[0] += self.speed
            self.walk()
        if key[pygame.K_a]:  # se a tecla a for pressionada move para _left
            self.walk_direction = "left"
            self.rect[0] -= self.speed
            self.walk()
        if key[pygame.K_SPACE] and self.on_ground:  # Tecla de espaço para saltar
            self.jump()
        if key[pygame.K_s]:
            self.shoot()
        else:
            self.is_shooting = False
            self.contadortiros = 5
        #TODO: animação de atirar + tiro


        if not any (key):
            if(self.walk_direction == "right"):
             self.image = self.sprite_running_right[0]
            else:
             self.image = self.sprite_running_left[0]

        self.image = pygame.transform.scale(self.image, [100, 98])

    def walk(self):
        self.current_image = (self.current_image + 0.2) % 4
        if(self.walk_direction == "right"):
          self.image = self.sprite_running_right[int(self.current_image)]
        else:
            self.image = self.sprite_running_left[int(self.current_image)]

    def update(self, *args):

        self.player_movement()
        # Aplicar gravidade
        self.vertical_velocity += self.gravity
        self.rect.y += self.vertical_velocity

        # Simular o chão (ajustar conforme necessário)
        if self.rect.bottom >= 525:  # Suponha que 300 seja a posição do chão
            self.rect.bottom = 525
            self.vertical_velocity = 0
            self.on_ground = True




    def jump(self):
        if self.on_ground:  # Permite pular somente se estiver no chão
            self.vertical_velocity = self.jump_speed
            self.on_ground = False  # Marca que o jogador não está no chão


    def shoot(self):
       #if not self.is_shooting:
            #self.is_shooting = True
            if(self.walk_direction == "right"):
               self.image = self.sprite_running_right[4]
            else:
               self.image = self.sprite_running_left[4]
            self.shooting_timer = 0
            self.contadortiros += 1

            if(self.contadortiros % 10==0):
              if(self.walk_direction == "right"):
                bullet = Bullet(self.rect.centerx, self.rect.centery, 10,"right")
              else:
                bullet = Bullet(self.rect.centerx, self.rect.centery, 10, "left")
              self.bullet_group.add(bullet)
