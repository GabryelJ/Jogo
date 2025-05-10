import pygame
import time
from entities.Bullet import Bullet


class Player(pygame.sprite.Sprite):
    def __init__(self, bullet_group, player_id, start_x, start_y):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 4
        self.gravity = 0.5
        self.vertical_velocity = 0
        self.jump_speed = -15
        self.on_ground = True
        self.last_jump_time = 0
        self.jump_delay = 0.2
        self.image = pygame.image.load('entities/sprites/sprite_0.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.y = start_y
        self.rect.x = start_x
        self.current_image = 0
        self.sprite_running_right = [pygame.image.load('entities/sprites/sprite_0.png').convert_alpha(),
                                     pygame.image.load('entities/sprites/sprite_1.png').convert_alpha(),
                                     pygame.image.load('entities/sprites/sprite_2.png').convert_alpha(),
                                     pygame.image.load('entities/sprites/sprite_3.png').convert_alpha(),
                                     pygame.image.load('entities/sprites/sprite_4.png').convert_alpha()]
        self.sprite_running_left = [pygame.transform.flip(img, True, False) for img in self.sprite_running_right]
        self.is_shooting = False
        self.bullet_group = bullet_group
        self.bullet_counter = 5
        self.walk_direction = "right"
        self.aimming_up = False
        self.player_id = player_id
        self.health = 100
        self.ammunition = 10

        # Defina as dimensões da hitbox
        hitbox_width = 60
        hitbox_height = 80

        # Calcule a posição X e Y para centralizar a hitbox
        hitbox_x = self.rect.x + (self.rect.width - hitbox_width) // 2
        hitbox_y = self.rect.y + (self.rect.height - hitbox_height) // 2

        # Defina a hitbox personalizada centralizada
        self.hitbox = pygame.Rect(hitbox_x, hitbox_y, hitbox_width, hitbox_height)

        # Controles específicos para cada jogador
        if player_id == 1:
            self.controls = {
                "left": pygame.K_a,
                "right": pygame.K_d,
                "jump": pygame.K_w,
                "aim_up": pygame.K_f,
                "shoot": pygame.K_s
            }
        else:
            self.controls = {
                "left": pygame.K_LEFT,
                "right": pygame.K_RIGHT,
                "jump": pygame.K_UP,
                "aim_up": pygame.K_RCTRL,
                "shoot": pygame.K_DOWN
            }

    def player_movement(self):
        key = pygame.key.get_pressed()
        if key[self.controls["right"]]:
            self.walk_direction = "right"
            self.rect.x += self.speed
            self.walk()
        if key[self.controls["left"]]:
            self.walk_direction = "left"
            self.rect.x -= self.speed
            self.walk()
        if key[self.controls["jump"]] and self.on_ground:
            self.jump()
        if key[self.controls["aim_up"]]:
            self.aimming_up = True
        else:
            self.aimming_up = False
        if key[self.controls["shoot"]]:
            if self.ammunition > 0:
                self.shoot()
        else:
            self.is_shooting = False
            self.bullet_counter = 5
        if not any(key):
            if self.walk_direction == "right":
                self.image = self.sprite_running_right[0]
            else:
                self.image = self.sprite_running_left[0]

        self.image = pygame.transform.scale(self.image, [100, 98])

    def walk(self):
        self.current_image = (self.current_image + 0.05) % 4
        if self.walk_direction == "right":
            self.image = self.sprite_running_right[int(self.current_image)]
        else:
            self.image = self.sprite_running_left[int(self.current_image)]

    def update(self, *args):
        self.player_movement()
        self.apply_gravity()
        self.rescue()
        self.image = pygame.transform.scale(self.image, [100, 98])
        self.rect = self.image.get_rect(topleft=self.rect.topleft)

        # atualiza pos da hitbox
        #self.hitbox.topleft = self.rect.topleft

        # Defina as dimensões da hitbox
        hitbox_width = 50
        hitbox_height = 80

        # Calcule a posição X e Y para centralizar a hitbox
        hitbox_x = self.rect.x + (self.rect.width - hitbox_width) // 2
        hitbox_y = self.rect.y + (self.rect.height - hitbox_height) + 7 // 2

        self.hitbox = pygame.Rect(hitbox_x, hitbox_y, hitbox_width, hitbox_height)

    def apply_gravity(self):
        if not self.on_ground:
            self.vertical_velocity += self.gravity
        else:
            self.vertical_velocity = 0
        self.rect.y += self.vertical_velocity

    def jump(self):
        current_time = time.time()
        if self.on_ground and (current_time - self.last_jump_time >= self.jump_delay):
            self.vertical_velocity = self.jump_speed
            self.on_ground = False
            self.last_jump_time = current_time

    def shoot(self):
        if self.walk_direction == "right":
            self.image = self.sprite_running_right[4]
        else:
            self.image = self.sprite_running_left[4]
        self.bullet_counter += 1
        if self.bullet_counter % 10 == 0:
            if self.aimming_up:
                bullet = Bullet(self.rect.centerx, self.rect.centery, 10, "cima")
                self.ammunition -= 1
            elif self.walk_direction == "right":
                bullet = Bullet(self.rect.centerx, self.rect.centery, 10, "right")
                self.ammunition -= 1
            elif self.walk_direction == "left":
                bullet = Bullet(self.rect.centerx, self.rect.centery, 10, "left")
                self.ammunition -= 1
            self.bullet_group.add(bullet)

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.kill()

    def rescue(self):
        if self.rect.y > 600:
            self.rect.y = 300
            self.rect.x = 300


    def draw(self, screen):

        screen.blit(self.image, self.rect.topleft)
        # Desenhe o rect em vermelho para visualização
        #pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)

        # Desenhe a hitbox em azul para visualização
        #pygame.draw.rect(screen, (0, 0, 255), self.hitbox, 2)
