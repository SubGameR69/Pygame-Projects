import pygame, sys
from player import Player
import obstacle
from alien import Alien, Extra
from random import choice, randint
from laser import Laser


class Game:
    def __init__(self):
        # player setup
        player_sprite = Player((SCREEN_WIDTH / 2, SCREEN_HEIGHT), SCREEN_WIDTH, 5)
        self.player = pygame.sprite.GroupSingle(player_sprite)

        # health and score system
        self.lives = 3
        self.live_surf = pygame.image.load("./graphics/player.png").convert_alpha()
        self.live_x_pos = SCREEN_WIDTH - (self.live_surf.get_size()[0] * 2 + 20)
        self.score = 0
        self.font = pygame.font.Font("./font/Pixeled.ttf", 20)

        # obstacle setup
        self.shape = obstacle.shape
        self.block_size = 6
        self.blocks = pygame.sprite.Group()
        self.obstacle_amount = 4
        self.obstacle_x_offset = [num * (SCREEN_WIDTH / self.obstacle_amount) for num in range(self.obstacle_amount)]
        self.create_multiple_obstacles(*self.obstacle_x_offset, x_start=SCREEN_WIDTH / 15, y_start=480)

        # Aline setup
        self.aliens = pygame.sprite.Group()
        self.alien_lasers = pygame.sprite.Group()
        self.aliens_setup(rows=6, cols=8)
        self.alien_direction = 1

        # Extra setup
        self.extra = pygame.sprite.GroupSingle()
        self.extra_spawn_time = randint(400, 800)

        # Audio
        music = pygame.mixer.Sound("./audio/music.wav")
        music.set_volume(0.2)
        music.play(loops=-1)
        self.laser_sound = pygame.mixer.Sound("./audio/laser.wav")
        self.laser_sound.set_volume(0.5)
        self.explosion_sound = pygame.mixer.Sound("./audio/explosion.wav")
        self.explosion_sound.set_volume(0.3)

    def aliens_setup(self, rows, cols, x_distance=60, y_distance=48, x_offset=70, y_offset=100):
        for row_idx, row in enumerate(range(rows)):
            for col_idx, col in enumerate(range(cols)):
                x = col_idx * x_distance + x_offset
                y = row_idx * y_distance + y_offset
                if row_idx == 0: alien_sprite = Alien("yellow", x, y)
                elif 1 <= row_idx <= 2: alien_sprite = Alien("green", x, y)
                else: alien_sprite = Alien("red", x, y)
                self.aliens.add(alien_sprite)

    def create_obstacle(self, x_start, y_start, offset_x):
        for row_idx, row in enumerate(self.shape):
            for col_idx, col in enumerate(row):
                if col == "x":
                    x = x_start + col_idx * self.block_size + offset_x
                    y = y_start + row_idx * self.block_size
                    block = obstacle.Block(self.block_size, (241, 79, 80), x, y)
                    self.blocks.add(block)

    def create_multiple_obstacles(self, *offset, x_start, y_start):
        for offset_x in offset:
            self.create_obstacle(x_start, y_start, offset_x)

    def alien_pos_checker(self):
        all_aliens = self.aliens.sprites()
        for alien in all_aliens:
            if alien.rect.right >= SCREEN_WIDTH:
                self.alien_direction = -1
                self.alien_move_down(2)
            elif alien.rect.left <= 0:
                self.alien_direction = 1
                self.alien_move_down(2)

    def alien_shoot(self):
        if self.aliens.sprites():
            random_alien = choice(self.aliens.sprites())
            laser_sprite = Laser(random_alien.rect.center, 6, SCREEN_HEIGHT)
            self.alien_lasers.add(laser_sprite)
            self.laser_sound.play()

    def alien_move_down(self, distance):
        if self.aliens:
            for alien in self.aliens.sprites():
                alien.rect.y += distance

    def extra_alien_timer(self):
        self.extra_spawn_time -= 1
        if self.extra_spawn_time <= 0:
            self.extra.add(Extra(choice(["right", "left"]), SCREEN_WIDTH))
            self.extra_spawn_time = randint(400, 800)

    def collision_checker(self):
        # player lasers
        if self.player.sprite.lasers:
            for laser in self.player.sprite.lasers:
                # obstacle collision
                if pygame.sprite.spritecollide(laser, self.blocks, True):
                    laser.kill()

                # alien collision
                alien_hit = pygame.sprite.spritecollide(laser, self.aliens, True)
                if alien_hit:
                    for alien in alien_hit:
                        self.score += alien.value
                        laser.kill()
                        self.explosion_sound.play()

                # extra collision
                if pygame.sprite.spritecollide(laser, self.extra, True):
                    self.score += 500
                    laser.kill()

        # aliens lasers
        if self.alien_lasers:
            for laser in self.alien_lasers:
                # obstacle collision
                if pygame.sprite.spritecollide(laser, self.blocks, True):
                    laser.kill()

                # player collision
                if pygame.sprite.spritecollide(laser, self.player, False):
                    laser.kill()
                    self.lives -= 1
                    if self.lives <= 0:
                        pygame.quit()
                        sys.exit()
        # aliens
        if self.aliens:
            for alien in self.aliens:
                pygame.sprite.spritecollide(alien, self.blocks, True)
                if pygame.sprite.spritecollide(alien, self.player, False):
                    pygame.quit()
                    sys.exit()

    def display_lives(self):
        for live in range(self.lives - 1):
            x = self.live_x_pos + (live * (self.live_surf.get_size()[0] + 10))
            screen.blit(self.live_surf, (x, 8))

    def display_score(self):
        score_surf = self.font.render(f"score: {self.score}", False, "white")
        score_rect = score_surf.get_rect(topleft=(10, -10))
        screen.blit(score_surf, score_rect)

    def victory_msg(self):
        if not self.aliens.sprites():
            victory_surf = self.font.render("YOU WON!", False, "white")
            victory_rect = victory_surf.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
            screen.blit(victory_surf, victory_rect)

    def run(self):
        # update all sprite groups
        self.player.update()
        self.aliens.update(self.alien_direction)
        self.alien_pos_checker()
        self.alien_lasers.update()
        self.extra_alien_timer()
        self.extra.update()
        self.collision_checker()

        # draw all sprite groups
        self.player.sprite.lasers.draw(screen)
        self.player.draw(screen)
        self.blocks.draw(screen)
        self.aliens.draw(screen)
        self.alien_lasers.draw(screen)
        self.extra.draw(screen)
        self.display_lives()
        self.display_score()
        self.victory_msg()


class CRT:
    def __init__(self):
        self.tv = pygame.image.load("./graphics/tv.png").convert_alpha()
        self.tv = pygame.transform.scale(self.tv, (SCREEN_WIDTH, SCREEN_HEIGHT))

    def crt_lines(self):
        line_height = 3
        line_amount = int(SCREEN_HEIGHT / line_height)
        for line in range(line_amount):
            y_pos = line * line_height
            pygame.draw.line(self.tv, "black", (0, y_pos), (SCREEN_WIDTH, y_pos), 1)

    def draw(self):
        self.tv.set_alpha(randint(75, 90))
        self.crt_lines()
        screen.blit(self.tv, (0, 0))


if __name__ == "__main__":
    pygame.init()
    SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    game = Game()
    crt = CRT()

    ALIENLASER = pygame.USEREVENT + 1
    pygame.time.set_timer(ALIENLASER, 800)

    running = True
    FPS = 60

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False
            if event.type == ALIENLASER:
                game.alien_shoot()

        screen.fill((30, 30, 30))
        game.run()
        crt.draw()

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()
