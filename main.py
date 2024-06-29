import pygame
from entities.Player import Player
from world.Ground import Ground
from world.Platform import Platform
from entities.AmmoBox import AmmoBox
from constants import HEIGHT, WIDTH
from entities.Plane import Plane

def draw():
    player_group.draw(SCREEN)
    for player in player_group:
        player.draw(SCREEN)

    for bullet in bullet_group:
        bullet.draw(SCREEN)

    platform_group.draw(SCREEN)
    bullet_group.draw(SCREEN)
    ammo_group.draw(SCREEN)
    draw_hud()
    plane_group.draw(SCREEN)

def update():
    player_group.update()
    bullet_group.update()
    ammo_group.update()
    plane_group.update()
    platform_group.update()

def draw_hud():
    font = pygame.font.Font(None, 36)
    player1_text = font.render(f'Player 1 - Health: {player1.health} Ammo: {player1.ammunition} ', True, (0, 0, 0))
    player2_text = font.render(f'Player 2 - Health: {player2.health} Ammo: {player2.ammunition}', True, (0, 0, 0))
    SCREEN.blit(player1_text, (20, 20))
    SCREEN.blit(player2_text, (20, 60))


pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

bullet_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
player1 = Player(bullet_group, 1)
player2 = Player(bullet_group, 2)
player_group.add(player1)
player_group.add(player2)

platform_group = pygame.sprite.Group()
platform_group.add(Platform(200, 400, 200, 20,1))
platform_group.add(Platform(400, 300, 200, 20,2))
platform_group.add(Platform(0 , 580, 800, 20,0))

ammo_group = pygame.sprite.Group()
plane_group = pygame.sprite.Group()
plane = Plane(ammo_group)
plane_group.add(plane)


running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for player in player_group:
        collisions = pygame.sprite.spritecollide(player, platform_group, False)
        player.on_ground = False
        for platform in collisions:
            if player.vertical_velocity >= 0 and player.hitbox.bottom >= platform.rect.top: #+ player.vertical_velocity:
                player.hitbox.bottom = platform.rect.top
                player.vertical_velocity = 0
                player.on_ground = True


        for ammo_box in ammo_group:
            if pygame.sprite.spritecollide(ammo_box, platform_group, False):
                ammo_box.on_ground = True
                ammo_box.gravity = 0
            else:
                ammo_box.on_ground = False
                ammo_box.gravity = 1
            for player in player_group:
                if pygame.sprite.collide_rect(ammo_box, player):
                    player.ammunition = 10
                    ammo_box.kill()


    for bullet in bullet_group:
        if pygame.sprite.spritecollide(bullet, player_group, False):
            for player in player_group:
                if bullet.hitbox.colliderect(player.hitbox):
                    player.take_damage(bullet.damage)
                    bullet.kill()


    update()
    SCREEN.fill("white")
    draw()
    pygame.display.flip()

pygame.quit()