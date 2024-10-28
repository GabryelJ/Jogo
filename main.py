import pygame
import constants
from entities.Plane import Plane
from entities.Player import Player
from world.Platform import Platform


class Game:
    def __init__(self):  # inicializa Game
        pygame.init()
        self.screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.playing = False
        self.menu_running = False
        self.show_score_running = False
        self.rodada = 0
        self.player1_name = ""
        self.player2_name = ""
        self.scores = {}  # Dicionário para armazenar os nomes e pontuações dos jogadores
        # fontes
        self.font = pygame.font.Font(None, 100)
        self.hud_font = pygame.font.Font(None, 36)
        self.input_font = pygame.font.Font(None, 50)
        self.instruction_font = pygame.font.Font(None, 40)
        # recursos score
        self.back_text = self.font.render('Back(1)', True, (255, 255, 255))
        self.back_rect = self.back_text.get_rect(center=(constants.WIDTH / 2, constants.HEIGHT - 100))
        # recursos menu
        self.play_text = self.font.render('Play (1)', True, (255, 255, 255))
        self.play_rect = self.play_text.get_rect(center=(constants.WIDTH / 2, constants.HEIGHT / 2 + 50))
        self.quit_text = self.font.render('Quit (2)', True, (255, 255, 255))
        self.quit_rect = self.quit_text.get_rect(center=(constants.WIDTH / 2, constants.HEIGHT / 2 + 150))
        self.score_text = self.font.render('Score (3)', True, (255, 255, 255))
        self.score_rect = self.score_text.get_rect(center=(constants.WIDTH / 2, constants.HEIGHT / 2 + 250))
        self.player1_input_rect = pygame.Rect(constants.WIDTH / 2 - 150, constants.HEIGHT / 2 - 150, 300, 50)
        self.player2_input_rect = pygame.Rect(constants.WIDTH / 2 - 150, constants.HEIGHT / 2 - 90, 300, 50)
        self.player1_instruction = self.instruction_font.render('Enter Player 1 Name:', True, (255, 255, 255))
        self.player2_instruction = self.instruction_font.render('Enter Player 2 Name:', True, (255, 255, 255))
        # sprites e grupos
        self.bullet_group = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()
        self.platform_group = pygame.sprite.Group()
        self.ammo_group = pygame.sprite.Group()
        self.plane_group = pygame.sprite.Group()
        # self.bomb_group = pygame.sprite.Group()
        self.player1 = None
        self.player2 = None
        self.plane = None

    def new_game(self):  # instancia e inicializa grupos e seus componentes
        self.player1 = Player(self.bullet_group, 1, 100, 470)
        self.player2 = Player(self.bullet_group, 2, 600, 470)
        self.player_group.add(self.player1)
        self.player_group.add(self.player2)
        self.plane = Plane(self.ammo_group)
        self.plane_group.add(self.plane)

        if self.rodada % 2 == 0:
            # cenário 1 abaixo
            self.platform_group.add(Platform(200, 400, 200, 20, 1))
            self.platform_group.add(Platform(400, 300, 200, 20, 2))
            self.platform_group.add(Platform(0, 580, 800, 20, 0))

        elif self.rodada % 2 == 1:
            # cenário 2 abaixo que deve ser modificado de forma a instanciar as plataformas em outro padrão
            self.platform_group.add(Platform(100, 450, 150, 20, 1))  # Plataforma menor e mais alta
            self.platform_group.add(Platform(300, 350, 150, 20, 2))  # Plataforma mais alta e à esquerda
            self.platform_group.add(Platform(500, 250, 150, 20, 3))  # Plataforma ainda mais alta e à direita
            self.platform_group.add(Platform(0, 580, 800, 20, 0))  # Chão

        self.run()

    def draw(self):
        self.screen.fill("white")
        self.player_group.draw(self.screen)
        for player in self.player_group:  # para debug de hitbox
            player.draw(self.screen)

        for bullet in self.bullet_group:  # para debug de hitbox
            bullet.draw(self.screen)

        self.platform_group.draw(self.screen)
        self.bullet_group.draw(self.screen)
        self.ammo_group.draw(self.screen)
        # self.bomb_group.draw(self.screen)
        self.plane_group.draw(self.screen)
        self.draw_hud()

    def update(self):
        self.player_group.update()
        self.bullet_group.update()
        self.ammo_group.update()
        # self.bomb_group.update()
        self.plane_group.update()
        self.platform_group.update()

    def draw_hud(self):
        player1_text = self.hud_font.render(
            f'{self.player1_name} - Health: {self.player1.health} Ammo: {self.player1.ammunition} ', True,
            (0, 0, 0))
        player2_text = self.hud_font.render(
            f'{self.player2_name} - Health: {self.player2.health} Ammo: {self.player2.ammunition}', True,
            (0, 0, 0))

        self.screen.blit(player1_text, (20, 20))
        self.screen.blit(player2_text, (20, 60))

    def run(self):  # game loop
        self.playing = True
        while self.playing:
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.playing = False
                    self.running = False

            self.players_collision()
            self.check_ammo_status()
            self.check_bullet_impact()
            # self.check_bomb_impact()  # desativado

            if self.player1.health == 0 or self.player2.health == 0:  # game over
                self.sprite_collect()
                self.playing = False
                winner = self.player1_name if self.player2.health == 0 else self.player2_name
                self.scores[winner] += 1  # Adiciona ponto ao vencedor
                self.menu()

            self.update()
            self.draw()
            pygame.display.flip()

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

    def check_bomb_impact(self):  # desativado
        for bomb in self.bomb_group:
            platform_collisions = pygame.sprite.spritecollide(bomb, self.platform_group, False)
            player_collisions = pygame.sprite.spritecollide(bomb, self.player_group, False)

            if platform_collisions:
                for platform in platform_collisions:
                    platform.kill()
                bomb.kill()

            if player_collisions:
                for player in self.player_group:
                    if bomb.rect.colliderect(player.hitbox):  # Verifica colisão com a hitbox do player
                        player.health = 0
                        player.kill()
                        bomb.kill()

    def sprite_collect(self):
        self.player_group.empty()
        self.bullet_group.empty()
        self.ammo_group.empty()
        # self.bomb_group.empty()
        self.plane_group.empty()
        self.platform_group.empty()

    def show_score(self):
        self.show_score_running = True
        while self.show_score_running:
            self.screen.fill((30, 30, 30))
            # Desenhe o placar
            sorted_scores = sorted(self.scores.items(), key=lambda item: item[1], reverse=True)
            for i, (player, score) in enumerate(sorted_scores):
                placar_text = self.input_font.render(f'{player}: {score}', True, (255, 255, 255))
                self.screen.blit(placar_text, (constants.WIDTH / 2 - 150, 100 + i * 40))

            # Desenhe botão voltar
            pygame.draw.rect(self.screen, (128, 0, 0), self.back_rect.inflate(20, 20))
            self.screen.blit(self.back_text, self.back_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.show_score_running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.back_rect.collidepoint(event.pos):
                        self.show_score_running = False
                        self.menu()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.show_score_running = False
                        self.menu()

            pygame.display.flip()

    def menu(self):
        player1_input_active = False
        player2_input_active = False
        self.menu_running = True
        while self.menu_running:
            # botões do menu

            self.screen.fill((30, 30, 30))  # Cor de fundo do menu

            # Desenhe instruções
            self.screen.blit(self.player1_instruction, (self.player1_input_rect.x, self.player1_input_rect.y - 40))
            self.screen.blit(self.player2_instruction, (self.player2_input_rect.x, self.player2_input_rect.y - 40))

            # Desenhe caixas de texto
            pygame.draw.rect(self.screen, (0, 0, 0), self.player1_input_rect)
            pygame.draw.rect(self.screen, (0, 0, 0), self.player2_input_rect)

            if player1_input_active:
                pygame.draw.rect(self.screen, (0, 255, 0), self.player1_input_rect, 3)
            else:
                pygame.draw.rect(self.screen, (255, 255, 255), self.player1_input_rect, 3)

            if player2_input_active:
                pygame.draw.rect(self.screen, (0, 255, 0), self.player2_input_rect, 3)
            else:
                pygame.draw.rect(self.screen, (255, 255, 255), self.player2_input_rect, 3)

            player1_surface = self.input_font.render(self.player1_name, True, (255, 255, 255))
            player2_surface = self.input_font.render(self.player2_name, True, (255, 255, 255))

            self.screen.blit(player1_surface, (self.player1_input_rect.x + 5, self.player1_input_rect.y + 5))
            self.screen.blit(player2_surface, (self.player2_input_rect.x + 5, self.player2_input_rect.y + 5))

            # Desenhe botões de ação
            pygame.draw.rect(self.screen, (0, 128, 0), self.play_rect.inflate(20, 20))
            pygame.draw.rect(self.screen, (128, 0, 0), self.quit_rect.inflate(20, 20))
            pygame.draw.rect(self.screen, (0, 0, 128), self.score_rect.inflate(20, 20))
            self.screen.blit(self.play_text, self.play_rect)
            self.screen.blit(self.quit_text, self.quit_rect)
            self.screen.blit(self.score_text, self.score_rect)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.menu_running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.player1_input_rect.collidepoint(event.pos):
                        player1_input_active = True
                        player2_input_active = False
                    elif self.player2_input_rect.collidepoint(event.pos):
                        player1_input_active = False
                        player2_input_active = True
                    else:
                        player1_input_active = False
                        player2_input_active = False

                    if self.play_rect.collidepoint(event.pos):
                        if self.player1_name and self.player2_name:  # Verifica se os nomes foram inseridos
                            if self.player1_name not in self.scores:
                                self.scores[self.player1_name] = 0
                            if self.player2_name not in self.scores:
                                self.scores[self.player2_name] = 0
                            self.menu_running = False
                            self.rodada = self.rodada + 1
                            self.new_game()
                    if self.quit_rect.collidepoint(event.pos):
                        self.running = False
                        self.menu_running = False
                    if self.score_rect.collidepoint(event.pos):
                        self.menu_running = False
                        self.show_score()

                if event.type == pygame.KEYDOWN:
                    if player1_input_active:
                        if event.key == pygame.K_BACKSPACE:
                            self.player1_name = self.player1_name[:-1]
                        else:
                            self.player1_name += event.unicode
                    elif player2_input_active:
                        if event.key == pygame.K_BACKSPACE:
                            self.player2_name = self.player2_name[:-1]
                        else:
                            self.player2_name += event.unicode

                    if event.key == pygame.K_1:
                        if self.player1_name and self.player2_name:  # Verifica se os nomes foram inseridos
                            if self.player1_name not in self.scores:
                                self.scores[self.player1_name] = 0
                            if self.player2_name not in self.scores:
                                self.scores[self.player2_name] = 0
                            self.menu_running = False
                            self.rodada = self.rodada + 1
                            self.new_game()
                    if event.key == pygame.K_2:
                        self.running = False
                        self.menu_running = False

                    if event.key == pygame.K_3:
                        self.menu_running = False
                        self.show_score()


game = Game()
game.menu()
pygame.quit()
