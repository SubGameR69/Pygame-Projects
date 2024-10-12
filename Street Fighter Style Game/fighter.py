import pygame


class Fighter:
    def __init__(self, x, y, flip, data, sprite_sheet, animation_steps):
        self.size = data[0]
        self.image_scale = data[1]
        self.offset = data[2]
        self.flip = flip
        self.animation_list = self.load_sprites(sprite_sheet, animation_steps)
        self.action = 0  # 0: idle 1: run 2: jump 3: attack 4: attack2 5: hit 6: death
        self.frame_idx = 0
        self.image = self.animation_list[self.action][self.frame_idx]
        self.rect = pygame.Rect(x, y, 80, 180)
        self.vel_y = 0
        self.jumping = False
        
        self.attacking = False
        self.attack_type = 0
        
        self.health = 100

    def load_sprites(self, sprite_sheet, animation_steps):
        animation_list = []
        for y, animation in enumerate(animation_steps):
            temp_img_list = []
            for x in range(animation):
                temp_img = sprite_sheet.subsurface(x * self.size, y * self.size, self.size, self.size)
                scaled_img = pygame.transform.scale(temp_img, (self.size * self.image_scale, self.size * self.image_scale))
                temp_img_list.append(scaled_img)
            animation_list.append(temp_img_list)
        return animation_list

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
            
        if target.rect.centerx > self.rect.centerx:
            self.flip = False
        else:
            self.flip = True
                
    def attack(self, screen, target):
        self.attacking = True
        attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, self.rect.width * 2, self.rect.height)
        if attacking_rect.colliderect(target.rect):
            target.health -= 10
        
        pygame.draw.rect(screen, "green", attacking_rect)

    def draw(self, screen):
        img = pygame.transform.flip(self.image, self.flip, False)
        pygame.draw.rect(screen, "red", self.rect)
        screen.blit(img, (self.rect.x - (self.offset[0] * self.image_scale), self.rect.y - (self.offset[1] * self.image_scale)))
