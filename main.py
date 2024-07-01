import pygame
import constants
from entities.Plane import Plane
from entities.Player import Player
from world.Platform import Platform


class Game:
    def __init__(self):  # inicializa Game
        pygame.init()
        self.SCREEN = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.game_over = False

    def new_game(self):  # instancia e inicializa grupos e seus componentes
        self.bullet_group = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()
        self.player1 = Player(self.bullet_group, 1)
        self.player2 = Player(self.bullet_group, 2)
        self.player_group.add(self.player1)
        self.player_group.add(self.player2)
        self.platform_group = pygame.sprite.Group()
        self.platform_group.add(Platform(200, 400, 200, 20, 1))
        self.platform_group.add(Platform(400, 300, 200, 20, 2))
        self.platform_group.add(Platform(0, 580, 800, 20, 0))
        self.ammo_group = pygame.sprite.Group()
        self.plane_group = pygame.sprite.Group()
        self.plane = Plane(self.ammo_group)
        self.plane_group.add(self.plane)
        self.run()

    def draw(self):
        self.SCREEN.fill("white")
        self.player_group.draw(self.SCREEN)
        for player in self.player_group:  # para debug de hitbox
            player.draw(self.SCREEN)

        for bullet in self.bullet_group: # para debug de hitbox
            bullet.draw(self.SCREEN)

        self.platform_group.draw(self.SCREEN)
        self.bullet_group.draw(self.SCREEN)
        self.ammo_group.draw(self.SCREEN)
        self.draw_hud()
        self.plane_group.draw(self.SCREEN)

    def update(self):
        self.player_group.update()
        self.bullet_group.update()
        self.ammo_group.update()
        self.plane_group.update()
        self.platform_group.update()

    def draw_hud(self):
        font = pygame.font.Font(None, 36)
        player1_text = font.render(f'Player 1 - Health: {self.player1.health} Ammo: {self.player1.ammunition} ', True,
                                   (0, 0, 0))
        player2_text = font.render(f'Player 2 - Health: {self.player2.health} Ammo: {self.player2.ammunition}', True,
                                   (0, 0, 0))
        self.SCREEN.blit(player1_text, (20, 20))
        self.SCREEN.blit(player2_text, (20, 60))

    def run(self):  # game loop
        self.playing = True
        while self.playing:
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    if self.playing:
                        self.playing = False
                    self.running = False

            self.players_collision()
            self.check_ammo_status()
            self.check_bullet_impact()
            if self.player1.health == 0 or self.player2.health == 0:  # game over
                self.collect()
                self.new_game()

            self.update()
            self.draw()
            pygame.display.flip()

        pygame.quit()

    def players_collision(self):
        for player in self.player_group:
            collisions = pygame.sprite.spritecollide(player, self.platform_group, False)
            player.on_ground = False
            for platform in collisions:
                if player.vertical_velocity >= 0 and player.hitbox.bottom >= platform.rect.top:  # + player.vertical_velocity:
                    player.hitbox.bottom = platform.rect.top
                    player.vertical_velocity = 0
                    player.on_ground = True

    def check_bullet_impact(self):
        for bullet in self.bullet_group:
            if pygame.sprite.spritecollide(bullet, self.player_group, False):
                for player in self.player_group:
                    if bullet.hitbox.colliderect(player.hitbox):
                        player.take_damage(bullet.damage)
                        bullet.kill()

    def check_ammo_status(self):
        for ammo_box in self.ammo_group:
            if pygame.sprite.spritecollide(ammo_box, self.platform_group, False):
                ammo_box.on_ground = True
                ammo_box.gravity = 0
            else:
                ammo_box.on_ground = False
                ammo_box.gravity = 1
            for player in self.player_group:
                if pygame.sprite.collide_rect(ammo_box, player):
                    player.ammunition = 10
                    ammo_box.kill()

    def collect(self):  # tratar vazamento de memória após reinicio
        self.player_group.empty()
        self.bullet_group.empty()
        self.ammo_group.empty()
        self.plane_group.empty()
        self.platform_group.empty()

    def menu(self): # TODO: 1: um game loop próprio? - 2: interação por teclas
        # display
        print('estado menu')
        pass


game = Game()
game.menu()
while game.running:
    game.new_game() #loop aqui
    game.menu()
