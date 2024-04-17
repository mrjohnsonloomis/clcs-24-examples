import pygame, sys

# Global variables
screen_width = 1280
screen_height = 960

# Define colors
WHITE = (255, 255, 255)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('player_image.png'), (50,50))
        self.rect = self.image.get_rect()
        self.rect.center = [screen_width // 2, screen_height // 2]

    def handle_keys(self):
        """ Handles Keys """
        key = pygame.key.get_pressed()
        dist = 5 # distance moved in 1 frame
        if key[pygame.K_DOWN]: # down key
            self.rect.y += dist # move down
        elif key[pygame.K_UP]: # up key
            self.rect.y -= dist # move up
        if key[pygame.K_RIGHT]: # right key
            self.rect.x += dist # move right
        elif key[pygame.K_LEFT]: # left key
            self.rect.x -= dist # move left

    def update(self):
        self.handle_keys()

# General setup
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Simple Sprite Game')

# Instantiate player
player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update
    all_sprites.update()

    # Drawing
    screen.fill(WHITE)  # Clear screen with white background
    all_sprites.draw(screen)  # Draw all sprites

    # Updating the window
    pygame.display.flip()
    clock.tick(60)  # Maintain 60 frames per second
