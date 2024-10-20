import pygame


class Fighter:
    def __init__(self, player, x, y, flip, data, sprite_sheet, animation_steps):
        self.player = player
        self.size = data[0]
        self.image_scale = data[1]
        self.offset = data[2]
        self.flip = flip
        self.animation_list = self.load_sprites(sprite_sheet, animation_steps)
        self.action = 0  # 0: idle 1: run 2: jump 3: attack 4: attack2 5: hit 6: death
        self.frame_idx = 0
        self.image = self.animation_list[self.action][self.frame_idx]
        self.update_time = pygame.time.get_ticks()
        self.rect = pygame.Rect(x, y, 80, 180)
        self.vel_y = 0
        self.jumping = False
        self.running = False
        self.attacking = False
        self.attack_type = 0
        self.attack_cooldown = 0
        self.hit = False
        self.health = 100
        self.alive = True

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

    def move(self, screen_width, screen_height, screen, target, round_over):
        speed = 10
        gravity = 2
        self.running = False
        self.attack_type = 0

        # movement
        keys = pygame.key.get_pressed()
        
        if not self.attacking and self.alive and not round_over:
            if self.player == 1:
                if keys[pygame.K_a]:
                    self.rect.x += -speed
                    self.running = True
                if keys[pygame.K_d]:
                    self.rect.x += speed
                    self.running = True
                # jumping
                if keys[pygame.K_SPACE] and not self.jumping:
                    self.vel_y = -30
                    self.jumping = True

                # attack
                if keys[pygame.K_r] or keys[pygame.K_t]:
                    self.attack(target)
                    if keys[pygame.K_r]:
                        self.attack_type = 1
                    if keys[pygame.K_t]:
                        self.attack_type = 2

            if self.player == 2:
                if keys[pygame.K_LEFT]:
                    self.rect.x += -speed
                    self.running = True
                if keys[pygame.K_RIGHT]:
                    self.rect.x += speed
                    self.running = True
                # jumping
                if keys[pygame.K_UP] and not self.jumping:
                    self.vel_y = -30
                    self.jumping = True

                # attack
                if keys[pygame.K_KP1] or keys[pygame.K_KP2]:
                    self.attack(target)
                    if keys[pygame.K_KP1]:
                        self.attack_type = 1
                    if keys[pygame.K_KP2]:
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

        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1

        if target.rect.centerx > self.rect.centerx:
            self.flip = False
        else:
            self.flip = True

    def update(self):
        if self.health <= 0:
            self.health = 0
            self.alive = False
            self.update_action(6)  # 6: death
        elif self.hit:
            self.update_action(5)  # 5: hit
        elif self.attacking:
            if self.attack_type == 1:
                self.update_action(3)  # 3: attack1
            elif self.attack_type == 2:
                self.update_action(4)  # 4: attack2
        elif self.jumping:
            self.update_action(2)  # 2: jump
        elif self.running:
            self.update_action(1)  # 1: run
        else:
            self.update_action(0)  # 0: idle

        animation_cooldown = 60
        self.image = self.animation_list[self.action][self.frame_idx]
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.frame_idx += 1
            self.update_time = pygame.time.get_ticks()
        if self.frame_idx >= len(self.animation_list[self.action]):
            if not self.alive:
                self.frame_idx = len(self.animation_list[self.action]) - 1
            else:
                self.frame_idx = 0
                if self.action == 3 or self.action == 4:
                    self.attacking = False
                    self.attack_cooldown = 20
                if self.action == 5:
                    self.hit = False
                    self.attacking = False
                    self.attack_cooldown = 20
                
    def attack(self, target):
        if self.attack_cooldown == 0:
            self.attacking = True
            attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, self.rect.width * 2, self.rect.height)
            if attacking_rect.colliderect(target.rect):
                target.health -= 10
                target.hit = True

    def update_action(self, action):
        if action != self.action:
            self.action = action
            self.frame_idx = 0
            self.update_time = pygame.time.get_ticks()

    def draw(self, screen):
        img = pygame.transform.flip(self.image, self.flip, False)
        screen.blit(img, (self.rect.x - (self.offset[0] * self.image_scale), self.rect.y - (self.offset[1] * self.image_scale)))
