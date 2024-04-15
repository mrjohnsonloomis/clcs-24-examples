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

    def update(self, keys_pressed):
        if keys_pressed[pygame.K_UP]:
            self.rect.y -= 5
        if keys_pressed[pygame.K_DOWN]:
            self.rect.y += 5
        if keys_pressed[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys_pressed[pygame.K_RIGHT]:
            self.rect.x += 5

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

    # Update player position based on keyboard inputs
    keys_pressed = pygame.key.get_pressed()
    player.update(keys_pressed)

    # Drawing
    screen.fill(WHITE)  # Clear screen with white background
    all_sprites.draw(screen)  # Draw all sprites

    # Updating the window
    pygame.display.flip()
    clock.tick(60)  # Maintain 60 frames per second
