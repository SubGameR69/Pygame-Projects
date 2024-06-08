import pygame
import random
import time

pygame.font.init()
WIDTH, HEIGHT = 720, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# Load Images
RED_SPACE_SHIP  = pygame.image.load("assets/pixel_ship_red_small.png")
GREEN_SPACE_SHIP  = pygame.image.load("assets/pixel_ship_green_small.png")
BLUE_SPACE_SHIP  = pygame.image.load("assets/pixel_ship_blue_small.png")

# Player Ship
YELLOW_SPACE_SHIP  = pygame.image.load("assets/pixel_ship_yellow.png")

# Lasers
RED_LASER = pygame.image.load("assets/pixel_laser_red.png")
BLUE_LASER = pygame.image.load("assets/pixel_laser_blue.png")
GREEN_LASER = pygame.image.load("assets/pixel_laser_green.png")
YELLOW_LASER = pygame.image.load("assets/pixel_laser_yellow.png")

# BackGround
BG = pygame.transform.scale(pygame.image.load("assets/background-black.png"), (WIDTH, HEIGHT))

class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        self.y += vel
        
    def off_screen(self, height):
        return self.y >= height and self.y <= 0

    def collision(self, object):
        return collide(self, object)

class Ship:
    COOLDOWN = 30
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    def move_lasers(self, vel, obj):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 10
                self.lasers.remove(laser)

    def get_width(self):
        return self.ship_img.get_width()
    
    def get_height(self):
        return self.ship_img.get_height()
    
    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1
    
    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1

class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = YELLOW_SPACE_SHIP.convert_alpha()
        self.laser_img = YELLOW_LASER.convert_alpha()
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

    def move_lasers(self, vel, objs):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)
                        self.lasers.remove(laser)

class Enemy(Ship):
    COLOR_MAP = {
        "red": (RED_SPACE_SHIP, RED_LASER),
        "green": (GREEN_SPACE_SHIP, GREEN_LASER),
        "blue": (BLUE_SPACE_SHIP, BLUE_LASER)
    }

    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self, vel):
        self.y += vel

def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

def main():
    running = True
    FPS = 60
    level = 0
    lives = 5
    main_font = pygame.font.SysFont("BigBlueTerm437 Nerd Font", 35)
    lost_font = pygame.font.SysFont("BigBlueTerm437 Nerd Font", 50)

    enemies = []
    wave_length = 0
    enemy_vel = 1

    PLAYER_VEL = 5

    LASER_VEL = 4

    clock = pygame.time.Clock()
    player = Player(WIDTH/2, HEIGHT - 150)
    lost = False
    lost_count = 0

    def redraw_window():
        WIN.blit(BG, (0, 0))
        # Draw text
        lives_label = main_font.render(f"Lives: {lives}", 1, "#fdfdfd")
        level_label = main_font.render(f"Level: {level}", 1, "#fdfdfd")

        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        for enemy in enemies:
            enemy.draw(WIN)

        player.draw(WIN)

        if lost:
            lost_label = lost_font.render("You Lost !!", 1, "#fdfdfd")
            WIN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, HEIGHT/2 - lost_label.get_height()/2))

        pygame.display.update()

    while running:
        clock.tick(FPS)
        redraw_window()

        if lives <= 0 or player.health <= 0:
            lost = True
            lost_count += 1

        if lost:
            if lost_count > FPS * 3:
                running = False
                break
            else:
                continue


        if len(enemies) == 0:
            level += 1
            wave_length += 5
            for _ in range(wave_length):
                random_x = random.randrange(50, WIDTH - 100)
                random_y = random.randrange(-1000, -100)
                colors = ["red", "green", "blue"]
                random_color = random.choice(colors)
                enemy = Enemy(random_x, random_y, random_color)
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x > 0:
            player.x -= 1 * PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x <= WIDTH - player.get_width():
            player.x += 1 * PLAYER_VEL
        if keys[pygame.K_UP] and player.y > 0:
            player.y -= 1 * PLAYER_VEL
        if keys[pygame.K_DOWN] and player.y <= HEIGHT  - player.get_height():
            player.y += 1 * PLAYER_VEL

        if keys[pygame.K_SPACE]:
            player.shoot()

        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            enemy.move_lasers(LASER_VEL, player)
            if enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)

        player.move_lasers(-LASER_VEL, enemies)

    pygame.quit()

if __name__ == "__main__":
    main()
