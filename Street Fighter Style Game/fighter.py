import pygame


class Fighter:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 80, 180)
        self.vel_y = 0
        self.jumping = False

    def move(self, screen_width, screen_height):
        speed = 10
        gravity = 2

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x += -speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += speed
        
        if keys[pygame.K_SPACE] and not self.jumping:
            self.vel_y = -30
            self.jumping = True
            
        self.vel_y += gravity
        self.rect.y += self.vel_y
        
        if self.rect.bottom >= screen_height - 110:
            self.rect.bottom = screen_height - 110
            self.jumping = False
            self.vel_y = 0

        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= screen_width:
            self.rect.right = screen_width

    def draw(self, screen):
        pygame.draw.rect(screen, "red", self.rect)