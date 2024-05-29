import pygame
from Entities.Player import Player
from World.Ground import Ground
from Program.constants import HEIGHT, WIDTH

if __name__ == '__main__':
    pygame.init()
    # TODO: definir plano de fundo
    # BACKGROUND = recebe o path para o plano de fundo
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    clock = pygame.time.Clock()

    running = True

    playerGroup = pygame.sprite.Group()
    player = Player()
    playerGroup.add(player)

    groundGroup = pygame.sprite.Group()
    ground = Ground()
    groundGroup.add(ground)


    def draw():
        playerGroup.draw(screen)
        groundGroup.draw(screen)


    def update():
        playerGroup.update()
        groundGroup.update()


    while running:
        clock.tick(4)  # limita frames por segundo em 12
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        update()
        screen.fill("white")  # limpa rastros do frame anterior cobrindo o frame atual com a cor do parametro até o proximo frame ser produzido.
        draw()
        pygame.display.flip()  # flip() atualiza o frame.

    pygame.quit()
