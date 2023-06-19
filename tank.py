import pygame
import random

# Initialize pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60
TANK_SIZE = 50
ENEMY_SIZE = 30
BULLET_SIZE = 10
PLAYER_SPEED = 5
ENEMY_SPEED = 3

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Create the game window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Tank Game")

# Game variables
player_x = WINDOW_WIDTH // 2 - TANK_SIZE // 2
player_y = WINDOW_HEIGHT - TANK_SIZE - 10
enemy_x = random.randint(0, WINDOW_WIDTH - ENEMY_SIZE)
enemy_y = random.randint(50, 150)
bullet_x = -BULLET_SIZE
bullet_y = -BULLET_SIZE
bullet_state = "ready"
score = 0
level = 1

# Game fonts
font = pygame.font.Font(None, 36)

# Create tank image
tank_img = pygame.Surface((TANK_SIZE, TANK_SIZE))
tank_img.fill(GREEN)

# Create enemy image
enemy_img = pygame.Surface((ENEMY_SIZE, ENEMY_SIZE))
enemy_img.fill(RED)

# Create bullet image
bullet_img = pygame.Surface((BULLET_SIZE, BULLET_SIZE))
bullet_img.fill(BLUE)

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x -= PLAYER_SPEED
            elif event.key == pygame.K_RIGHT:
                player_x += PLAYER_SPEED
            elif event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_x = player_x + TANK_SIZE // 2 - BULLET_SIZE // 2
                    bullet_y = player_y
                    bullet_state = "fire"

    # Game logic
    if bullet_state == "fire":
        bullet_y -= 10
        if bullet_y <= 0:
            bullet_state = "ready"

    if level == 1:
        if enemy_y > WINDOW_HEIGHT:
            enemy_x = random.randint(0, WINDOW_WIDTH - ENEMY_SIZE)
            enemy_y = random.randint(50, 150)
            score -= 1
        if (
            bullet_x >= enemy_x
            and bullet_x <= enemy_x + ENEMY_SIZE
            and bullet_y >= enemy_y
            and bullet_y <= enemy_y + ENEMY_SIZE
        ):
            bullet_state = "ready"
            score += 1
            enemy_x = random.randint(0, WINDOW_WIDTH - ENEMY_SIZE)
            enemy_y = random.randint(50, 150)

    # Drawing
    window.fill(BLACK)
    window.blit(tank_img, (player_x, player_y))
    window.blit(enemy_img, (enemy_x, enemy_y))
    window.blit(bullet_img, (bullet_x, bullet_y))

    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    window.blit(score_text, (10, 10))
    window.blit(level_text, (WINDOW_WIDTH - level_text.get_width() - 10, 10))

    pygame.display.flip()

    # Game over condition
    if score >= 5 and level == 1:
        level = 2
        enemy_x = random.randint(0, WINDOW_WIDTH - ENEMY_SIZE)
        enemy_y = random.randint(50, 150)
        score = 0
    elif score >= 10 and level == 2:
        level = 3
        enemy_x = random.randint(0, WINDOW_WIDTH - ENEMY_SIZE)
        enemy_y = random.randint(50, 150)
        score = 0
    elif score >= 15 and level == 3:
        running = False

    # FPS regulation
    pygame.time.Clock().tick(FPS)

# Quit the game
pygame.quit()
