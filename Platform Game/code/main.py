from settings import *
from sprites import Sprite

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Platformer")
        self.clock = pygame.time.Clock()
        self.running = True
        
        # groups
        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()
        
        # load game
        self.setup()
        
    def setup(self):
        tmx_map = load_pygame(join("data", "maps", "world.tmx"))
        
        for x, y, image in tmx_map.get_layer_by_name("Main").tiles():
            Sprite((x * TILE_SIZE, y * TILE_SIZE), image, (self.all_sprites, self.collision_sprites))
            
        for x, y, image in tmx_map.get_layer_by_name("Decoration").tiles():
            Sprite((x * TILE_SIZE, y * TILE_SIZE), image, self.all_sprites)
        
        
    def run(self):
        while self.running:
            dt = self.clock.tick(FPS) / 1000
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    self.running = False
                    
            # update
            self.all_sprites.update(dt)
            
            # draw
            self.display_surface.fill(BG_COLOR)
            self.all_sprites.draw(self.display_surface)
            pygame.display.update()
        
        pygame.quit()
        
if __name__ == "__main__":
    game = Game()
    game.run()