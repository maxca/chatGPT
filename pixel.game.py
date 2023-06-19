import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen size
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

# Set up the colors
background_color = (0, 0, 0)   # Black
snake_color = (0, 255, 0)       # Green
food_color = (255, 0, 0)        # Red

# Set up the snake position and initial direction
snake_pos = [[100, 50], [90, 50], [80, 50]]
snake_direction = 'RIGHT'

# Set up the food position
food_pos = [random.randrange(1, screen_width // 10) * 10,
            random.randrange(1, screen_height // 10) * 10]

# Set up the game clock
clock = pygame.time.Clock()

# Set up the game loop
game_over = False
while not game_over:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Check for arrow key presses to change the snake's direction
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake_direction != 'DOWN':
        snake_direction = 'UP'
    elif keys[pygame.K_DOWN] and snake_direction != 'UP':
        snake_direction = 'DOWN'
    elif keys[pygame.K_LEFT] and snake_direction != 'RIGHT':
        snake_direction = 'LEFT'
    elif keys[pygame.K_RIGHT] and snake_direction != 'LEFT':
        snake_direction = 'RIGHT'

    # Update the snake's position based on the direction
    if snake_direction == 'UP':
        snake_pos[0][1] -= 10
    elif snake_direction == 'DOWN':
        snake_pos[0][1] += 10
    elif snake_direction == 'LEFT':
        snake_pos[0][0] -= 10
    elif snake_direction == 'RIGHT':
        snake_pos[0][0] += 10

    # Check for collision with the food
    if snake_pos[0] == food_pos:
        # Generate new food position
        food_pos = [random.randrange(1, screen_width // 10) * 10,
                    random.randrange(1, screen_height // 10) * 10]
        # Increase the length of the snake
        snake_pos.append([0, 0])

    # Check for collision with the walls or the snake's own body
    if (snake_pos[0][0] < 0 or snake_pos[0][0] >= screen_width
            or snake_pos[0][1] < 0 or snake_pos[0][1] >= screen_height):
        game_over = True
    for block in snake_pos[1:]:
        if block == snake_pos[0]:
            game_over = True

    # Clear the screen
    screen.fill(background_color)

    # Draw the snake
    for block in snake_pos:
        pygame.draw.rect(screen, snake_color, pygame.Rect(block[0], block[1], 10, 10))

    # Draw the food
    pygame.draw.rect(screen, food_color, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Update the display
    pygame.display.update()

    # Set the game speed
    clock.tick(10)  # Adjust this value to change the snake's speed

# Quit the game
pygame.quit()
