import pygame, sys, random

# Global variables
screen_width = 1280
screen_height = 860

# Custom events
lives = pygame.USEREVENT + 1

# Define colors
WHITE = (255, 255, 255)

class Background(pygame.sprite.Sprite):
    def __init__(self, which):
        super().__init__()
        self.image = pygame.image.load('background.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (which*self.rect.width, 0)
        self.speed = -3
        
    def update(self):
        self.rect.x += self.speed
        if self.rect.right < 0:
            self.rect.x += self.rect.width*2

class Rock(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('player_image.png'), (25,25))
        self.rect = self.image.get_rect()
        self.rect.topleft = [random.randint(0, screen_width), 0]  
    
    def update(self):
        self.rect.y += 5
        if self.rect.top > screen_height:
            self.rect.bottom = 0
            self.rect.topleft = [random.randint(0, screen_width), 0]

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('player_image.png'), (90,90))
        self.rect = self.image.get_rect()
        self.rect.center = [screen_width // 2, screen_height]

    def handle_keys(self):
        """Handles Keys and ground status"""
        key = pygame.key.get_pressed()
        dist = 5  # distance moved in 1 frame
        
        # Check ground status
        if self.rect.bottom >= screen_height:
            self.on_ground = True
            self.rect.bottom = screen_height
        else:
            self.on_ground = False
            self.rect.y += dist/2  # move down (simulate gravity)

        if key[pygame.K_DOWN]:  # down key
            if self.rect.bottom < screen_height:  # Prevent moving down into the ground
                self.rect.y += dist  # move down
        elif key[pygame.K_UP]:  # up key
            if self.on_ground:  # Only jump if on the ground
                self.rect.y -= dist * 10  # jump up (compensate for gravity)
                self.on_ground = False  # Set on_ground to False as it jumps

        if key[pygame.K_RIGHT]:  # right key
            self.rect.x += dist  # move right
        elif key[pygame.K_LEFT]:  # left key
            self.rect.x -= dist  # move left

        # Screen boundary checks
        if self.rect.right >= screen_width:
            self.rect.right = screen_width
        elif self.rect.left < 0:
            self.rect.left = 0

        
    def update(self):
        self.handle_keys()

# General setup
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Simple Sprite Game')

# Instantiate player and background
player = Player()
rock = Rock()
bg1 = Background(0)
bg2 = Background(1)

bg_group = pygame.sprite.Group(bg1, bg2)
player_group = pygame.sprite.Group()
rock_group = pygame.sprite.Group()
player_group.add(player)
rock_group.add(rock)

all_sprites = pygame.sprite.Group(player, rock)

'''# Function to check for collisions
def check_collisions(rock_group, player_group):
    for rock in rock_group:
        for player in player_group:
            if rock.rect.colliderect(player.rect):
                rock.rect.bottom = 0
                pygame.event.post(pygame.event.Event(lives))
'''
def check_collisions(rock_group, player_group): 
    for rock in rock_group:
        for player in player_group:
            if rock.rect.colliderect(player.rect):
                rock.rect.topleft = [random.randint(0, screen_width), 0]
                pygame.event.post(pygame.event.Event(lives))
lives = 3
# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == lives:
            print("Lives -1")
            lives -= 1
            if lives == 0:
                print("Game Over")
                pygame.quit()
                sys.exit()
    
    # Check for collisions
    check_collisions(rock_group, player_group)
            
    # Update
    bg_group.update()
    all_sprites.update()

    # Drawing
    screen.fill(WHITE)  # Clear screen with white background
    bg_group.draw(screen)
    all_sprites.draw(screen)  # Draw all sprites

    # Updating the window
    pygame.display.flip()
    clock.tick(60)  # Maintain 60 frames per second
