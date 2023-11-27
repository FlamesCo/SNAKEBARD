import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up the display
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Snake')

# Define the snake
snake = [(250, 250), (250, 240), (250, 230)]
direction = 'RIGHT'

# Define the food
food = (400, 300)

# Set up the clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if direction != 'RIGHT':
                    direction = 'LEFT'
            if event.key == pygame.K_RIGHT:
                if direction != 'LEFT':
                    direction = 'RIGHT'
            if event.key == pygame.K_UP:
                if direction != 'DOWN':
                    direction = 'UP'
            if event.key == pygame.K_DOWN:
                if direction != 'UP':
                    direction = 'DOWN'

    # Move the snake
    if direction == 'RIGHT':
        snake.insert(0, (snake[0][0] + 10, snake[0][1]))
    if direction == 'LEFT':
        snake.insert(0, (snake[0][0] - 10, snake[0][1]))
    if direction == 'UP':
        snake.insert(0, (snake[0][0], snake[0][1] - 10))
    if direction == 'DOWN':
        snake.insert(0, (snake[0][0], snake[0][1] + 10))

    # Check if the snake has eaten the food
    if snake[0] == food:
        snake.append(snake[-1])
        food = (random.randrange(10, 79) * 10, random.randrange(6, 59) * 10)

    # Check if the snake has hit itself
    for body_part in snake[1:]:
        if snake[0] == body_part:
            running = False
        # Check if the snake has hit the wall
        if snake[0][0] < 0 or snake[0][0] > 790 or snake[0][1] < 0 or snake[0][1] > 590:
            running = False

        # Fill the screen with black
        screen.fill(BLACK)

        # Draw the snake
        for body_part in snake:
            pygame.draw.rect(screen, GREEN, pygame.Rect(body_part[0], body_part[1], 10, 10))

        # Draw the food
        pygame.draw.rect(screen, RED, pygame.Rect(food[0], food[1], 10, 10))

        # Update the display
        pygame.display.flip()

        # Set thepygame.quit()
