import pygame
from Entities.Player import Player
from World.Ground import Ground
from Program.constants import HEIGHT, WIDTH

# entry point
if __name__ == '__main__':

    # inicializa o modulo pygame.
    pygame.init()

    # TODO: definir plano de fundo
    # BACKGROUND = recebe o path para o plano de fundo

    # instancia a tela e passa altura e largura
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

    # instancia clock para controlar a taxa de frames
    clock = pygame.time.Clock()

    # cria um grupo de sprites para jogador(es) (player).
    playerGroup = pygame.sprite.Group()
    # Grupo de sprites
    all_sprites = pygame.sprite.Group()
    bullet_group = pygame.sprite.Group()

    player = Player(bullet_group)  # instancia de player
    playerGroup.add(player)
    all_sprites.add(player)

    # Criar instância do jogador
   # player = Player(bullet_group)  # instancia de player
    #player = Player(bullet_group)
   # all_sprites.add(player)

    #player = Player(bullet_group)  # instancia de player
    #playerGroup.add(player)

    # cria um grupo de sprites para o chão (ground)
    groundGroup = pygame.sprite.Group()
    GROUND = Ground()  # instancia de ground
    groundGroup.add(GROUND)


    def draw():  # renderiza os objetos dos grupos na tela
        playerGroup.draw(SCREEN)
        groundGroup.draw(SCREEN)
        bullet_group.draw(SCREEN)




    def update():  # atualiza o estado dos sprites
        playerGroup.update()
        all_sprites.update()
        bullet_group.update()


    running = True
    while running:  # game loop
        clock.tick(60)  # limita o número de frames por segundo

        # espaço para eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # colisão de player com o chão.
        if pygame.sprite.groupcollide(playerGroup, groundGroup, False, False):
            player.gravity = 0
        else:
            player.gravity = 4

        update()
        SCREEN.fill("white")  # limpa rastros do frame anterior cobrindo o frame atual para que o proximo frame seja renderizado sem rastros.
        draw()
        pygame.display.flip()  # flip() atualiza o frame.

    pygame.quit()
