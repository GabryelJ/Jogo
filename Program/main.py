import pygame
from Entities.Player import Player

if __name__ == '__main__':
    pygame.init()
    height = 800
    width = 600
    screen = pygame.display.set_mode((width, height))
    speed = 4
    game_speed = 8
    # TODO: definir plano de fundo?
    # BACKGROUND = recebe o path para o plano de fundo

    clock = pygame.time.Clock()
    running = True

    playerGroup = pygame.sprite.Group()
    player = Player()
    playerGroup.add(player)


    def draw():
        playerGroup.draw(screen)


    def update():
        playerGroup.update()


    while running:
        clock.tick(4)  # limita frames por segundo em 4

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        update()
        screen.fill("red")  # limpa rastros do frame anterior cobrindo o frame atual com a cor do parametro até o proximo frame ser produzido.
        draw()

        # flip() atualiza o frame.
        pygame.display.flip()

    pygame.quit()
