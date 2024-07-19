from settings import *

class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)
        
class Player(Sprite):
    def __init__(self, pos, groups, collision_sprites):
        surf = pygame.Surface((40, 80))
        super().__init__(pos, surf, groups)
        # movement & collision
        self.direction = pygame.Vector2()
        self.collision_sprites = collision_sprites
        self.speed = 400
        self.gravity = 50
        self.on_floor = False
        
    def input(self):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        if keys[pygame.K_SPACE] and self.on_floor:
            self.direction.y = -20
        
    def move(self, dt):
        # horizontal
        self.rect.x += self.direction.x * self.speed * dt
        self.collision("horizontal")
        
        # vertical
        self.on_floor = False
        self.direction.y += self.gravity * dt
        self.rect.y += self.direction.y
        self.collision("vertical")
    
    def collision(self, direction):
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.rect):
                if direction == "horizontal":
                    if self.direction.x > 0 : self.rect.right = sprite.rect.left
                    if self.direction.x < 0 : self.rect.left = sprite.rect.right
                if direction == "vertical":
                    if self.direction.y > 0 : 
                        self.rect.bottom = sprite.rect.top
                        self.direction.y = 0
                        self.on_floor = True
                    if self.direction.y < 0 : self.rect.top = sprite.rect.bottom
        
    def update(self, dt):
        self.input()
        self.move(dt)