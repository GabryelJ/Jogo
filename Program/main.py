import pygame
from Entities.Player import Player
from World.Ground import Ground
from Program.constants import HEIGHT, WIDTH


def draw():  # renderiza os objetos dos grupos na tela
    player_group.draw(SCREEN)
    ground_group.draw(SCREEN)
    bullet_group.draw(SCREEN)


def update():  # atualiza o estado dos sprites
    player_group.update()
    bullet_group.update()


# entry point
if __name__ == '__main__':
    pygame.init()  # inicializa o modulo pygame.
    # BACKGROUND = recebe o path para o plano de fundo TODO: definir plano de fundo
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))  # instancia a tela e passa uma tupla com altura e largura
    clock = pygame.time.Clock()  # instancia clock para controlar a taxa de frames

    bullet_group = pygame.sprite.Group()  # cria um grupo de sprites para projéteis (Bullet)
    player_group = pygame.sprite.Group()  # cria um grupo de sprites para o player
    player = Player(bullet_group)  # instancia de player
    player_group.add(player)  # adiciona player ao player_group
    ground_group = pygame.sprite.Group()  # cria um grupo de sprites para o chão (ground)
    GROUND = Ground()  # instancia de ground
    ground_group.add(GROUND)  #´adiciona ground ao ground_group

    running = True
    while running:  # game loop
        clock.tick(60)  # define o número de frames por segundo
        for event in pygame.event.get():  # espaço para eventos
            if event.type == pygame.QUIT:
                running = False

        # colisão de player com o chão.
        if pygame.sprite.groupcollide(player_group, ground_group, False, False):
            player.gravity = 0  # ao colidir a gravidade de player é zerada.
        else:
            player.gravity = 4  # caso contrário a gravidade é a padrão de player.

        update()
        SCREEN.fill("white")  # limpa rastros do frame anterior cobrindo o frame atual para que o proximo frame seja renderizado sem rastros.
        draw()
        pygame.display.flip()  # flip() atualiza o frame.

    pygame.quit()
