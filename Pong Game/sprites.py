from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)

        # Image
        self.image = pygame.Surface(SIZE["paddle"])
        self.image.fill(COLORS["paddle"])

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