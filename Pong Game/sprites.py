from settings import *
from random import choice, uniform

class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)

        # Image
        self.image = pygame.Surface(SIZE["paddle"], pygame.SRCALPHA)
        pygame.draw.rect(self.image, COLORS["paddle"], pygame.Rect((0, 0), SIZE["paddle"]), 0, 6)

        # Rect & Movements
        self.rect = self.image.get_rect(center = POS["player"])
        self.direction = 0
        self.speed = SPEED["player"]

    def move(self, dt):
        self.rect.centery += self.direction * self.speed * dt
        self.rect.top = 0 if self.rect.top < 0 else self.rect.top
        self.rect.bottom = WINDOW_HEIGHT if self.rect.bottom > WINDOW_HEIGHT else self.rect.bottom

    def get_direction(self):
        keys = pygame.key.get_pressed()
        self.direction = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])

    def update(self, dt):
        self.get_direction()
        self.move(dt)


class Ball(pygame.sprite.Sprite):
    def __init__(self, groups, paddle_sprites):
        super().__init__(groups)

        # Image
        self.image = pygame.Surface(SIZE["ball"], pygame.SRCALPHA)
        pygame.draw.circle(self.image, COLORS["ball"], (SIZE["ball"][0] / 2, SIZE["ball"][1] / 2), SIZE["ball"][0] / 2)

        # Rect & Movement
        self.rect = self.image.get_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        self.direction = pygame.Vector2(choice((1, -1)), uniform(0.7, 0.8) * choice((1, -1)))

    def move(self, dt):
        self.rect.center += self.direction * SPEED["ball"] * dt

    def wall_collision(self):
        if self.rect.top <= 0:
            self.rect.top = 0
            self.direction.y *= -1

        if self.rect.bottom >= WINDOW_HEIGHT:
            self.rect.bottom = WINDOW_HEIGHT
            self.direction.y *= -1

        if self.rect.right >= WINDOW_WIDTH:
            self.rect.right = WINDOW_WIDTH
            self.direction.x *= -1

        if self.rect.left <= 0:
            self.rect.left = 0
            self.direction.x *= -1

    def update(self, dt):
        self.move(dt)
        self.wall_collision()