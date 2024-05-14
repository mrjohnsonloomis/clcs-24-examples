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

class Laser(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.image = pygame.transform.scale(pygame.image.load('laser.png'), (10,10))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = self.player.rect.topright
    
    def update(self):
        self.rect.x += 5

        if self.rect.right > screen_width:
            self.kill()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('player_image.png'), (90,90))
        self.rect = self.image.get_rect()
        self.rect.center = [screen_width // 2, screen_height]
        self.mask = pygame.mask.from_surface(self.image)
        self.dist = 5
        self.on_ground = True
        self.on_platform = False
    def handle_keys(self):
        """Handles Keys and ground status"""
        key = pygame.key.get_pressed()
        # Check ground status
        if self.rect.bottom >= screen_height & self.on_platform == False:
            self.on_ground = True
            self.rect.bottom = screen_height
        else:
            self.on_ground = False
            self.rect.y += self.dist/2  # move down (simulate gravity)

        if key[pygame.K_DOWN]:  # down key
            if self.rect.bottom < screen_height:  # Prevent moving down into the ground
                self.rect.y += self.dist  # move down
        elif key[pygame.K_UP]:  # up key
            if self.on_ground:  # Only jump if on the ground
                self.rect.y -= self.dist * 10  # jump up (compensate for gravity)
                self.on_ground = False  # Set on_ground to False as it jumps

        if key[pygame.K_RIGHT]:  # right key
            self.rect.x += self.dist  # move right
        elif key[pygame.K_LEFT]:  # left key
            self.rect.x -= self.dist  # move left

        # Screen boundary checks
        if self.rect.right >= screen_width:
            self.rect.right = screen_width
        elif self.rect.left < 0:
            self.rect.left = 0

        
    def update(self):
        self.handle_keys()

class Platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('platform.jpg'), (250,90))
        self.rect = self.image.get_rect()
        self.rect.center = [screen_width // 2, screen_height]
        self.mask = pygame.mask.from_surface(self.image)

# General setup
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Simple Sprite Game')

# Instantiate player and background
player = Player()
laser = Laser(player)
bg1 = Background(0)
bg2 = Background(1)

bg_group = pygame.sprite.Group(bg1, bg2)
player_group = pygame.sprite.Group()
laser_group = pygame.sprite.Group(laser)
plat_group = pygame.sprite.Group(Platform())
player_group.add(player)


all_sprites = pygame.sprite.Group(player)


def display_text(screen, message, position, font='Arial', size=48, color=(255, 255, 255)):
    """
    Display text on the given Pygame screen.

    Argumentss:
    screen: The Pygame display surface to draw on. (req)
    message: The string of text to display. (req)
    position: A tuple (x, y) representing where to center the text on the screen. (req)
    font: The name of the font to use. (default)
    size: The size of the font. (default)
    color: A tuple (r, g, b) representing the color of the text. (default = white)

    """
    # Initialize font
    font = pygame.font.SysFont(font, size)
    
    # Render the text
    message = str(message)
    text_surface = font.render(message, True, color)
    
    # Create a rectangle for positioning
    text_rect = text_surface.get_rect()
    text_rect.center = position
    
    # Blit the text onto the screen
    screen.blit(text_surface, text_rect)

def platform_check(player, platform):
    # Calculate offset
    offset_x = platform.rect.x - player.rect.x
    offset_y = platform.rect.y - player.rect.y

    # Check for collision
    if player.mask.overlap(platform.mask, (offset_x, offset_y)):
        player.rect.bottom = platform.rect.top
        player.on_ground = True

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
                display_text(screen, 'Game over!', (screen_width/2, screen_height/2))
                pygame.quit()
                sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                laser = Laser(player)
                laser_group.add(laser)

    # Check for collisions
    #check_collisions(player_group)
    platform_check(player, plat_group.sprites()[0])      
    # Update
    bg_group.update()
    all_sprites.update()
    laser_group.update()

    # Drawing
    screen.fill(WHITE)  # Clear screen with white background
    bg_group.draw(screen)
    all_sprites.draw(screen)  # Draw all sprites
    #plat_group.draw(screen)
    laser_group.draw(screen)
    display_text(screen, f'Lives: {lives}', (150,100))

    # Updating the window
    pygame.display.flip()
    clock.tick(60)  # Maintain 60 frames per second
