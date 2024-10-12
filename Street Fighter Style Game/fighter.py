import pygame


class Fighter:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 80, 180)
        self.vel_y = 0
        self.jumping = False
        
        self.attacking = False
        self.attack_type = 0

    def move(self, screen_width, screen_height, screen, target):
        speed = 10
        gravity = 2

        # movement
        keys = pygame.key.get_pressed()
        
        if not self.attacking:
            if keys[pygame.K_a]:
                self.rect.x += -speed
            if keys[pygame.K_d]:
                self.rect.x += speed
            # jumping
            if keys[pygame.K_SPACE] and not self.jumping:
                self.vel_y = -30
                self.jumping = True
                
            # attack
            if keys[pygame.K_r] or keys[pygame.K_t]:
                self.attack(screen, target)
                if keys[pygame.K_r]:
                    self.attack_type = 1
                if keys[pygame.K_t]:
                    self.attack_type = 2
        
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
            
                
    def attack(self, screen, target):
        self.attacking = True
        attacking_rect = pygame.Rect(self.rect.centerx, self.rect.y, self.rect.width * 2, self.rect.height)
        if attacking_rect.colliderect(target.rect):
            print("Hit")
        
        pygame.draw.rect(screen, "green", attacking_rect)

    def draw(self, screen):
        pygame.draw.rect(screen, "red", self.rect)