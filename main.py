import pygame
from entities.Player import Player
from world.Ground import Ground
from world.Platform import Platform
from entities.AmmoBox import AmmoBox
from constants import HEIGHT, WIDTH

def draw():
    player_group.draw(SCREEN)
    #ground_group.draw(SCREEN)
    for player in player_group:
        player.draw(SCREEN)
    for bullet in bullet_group:
        bullet.draw(SCREEN)
    GROUND.draw(SCREEN)
    platform_group.draw(SCREEN)
    bullet_group.draw(SCREEN)
    ammo_group.draw(SCREEN)
    draw_hud()

def update():
    player_group.update()
    bullet_group.update()
    ammo_group.update()

def draw_hud():
    font = pygame.font.Font(None, 36)
    player1_text = font.render(f'Player 1 - Health: {player1.health} Ammo: {player1.ammunition} Ground: {player1.on_ground}', True, (0, 0, 0))
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
#ground_group = pygame.sprite.Group()
GROUND = Ground()
#ground_group.add(GROUND)

platform_group = pygame.sprite.Group()
platform_group.add(Platform(200, 400, 200, 20))
platform_group.add(Platform(400, 300, 200, 20))
platform_group.add(GROUND)

ammo_group = pygame.sprite.Group()
ammo_box = AmmoBox(300, 500,player_group)#encontrar uma forma de verificar se existe alguma amobox,se não existir nenhuma viva,cria
ammo_group.add(ammo_box)                 #eventos talvez verificar a todo clock?

running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Colisões com o chão
   # for player in player_group:
    #    if pygame.sprite.spritecollide(player, platform_group, False):#tava ground_group
     #       player.rect.bottom = 525
      #      player.vertical_velocity = 0
       #     player.on_ground = True
        #else:
         #   player.on_ground = False

    for player in player_group:
        collisions = pygame.sprite.spritecollide(player, platform_group, False)
        player.on_ground = False
        for platform in collisions:
            if player.vertical_velocity >= 0 and player.rect.bottom >= platform.rect.top: #+ player.vertical_velocity:
                player.rect.bottom = platform.rect.top
                player.vertical_velocity = 0
                player.on_ground = True


#player.vertical_velocity >= 0 and
    for bullet in bullet_group:
        if pygame.sprite.spritecollide(bullet, player_group, False):
            for player in player_group:
                if pygame.sprite.collide_rect(bullet, player):
                    player.take_damage(bullet.damage)
                    bullet.kill()

    update()
    SCREEN.fill("white")
    draw()
    pygame.display.flip()

pygame.quit()