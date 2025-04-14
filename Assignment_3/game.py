import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
width, height = 600, 400
block_size = 20
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('🐍 Snake Game')

# Colors
black = (0, 0, 0)
green = (0, 255, 0)
red   = (255, 0, 0)
white = (255, 255, 255)

# Clock
clock = pygame.time.Clock()
speed = 5  # Difficulty

# Font
font = pygame.font.SysFont('comicsansms', 30)

def draw_snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, green, [block[0], block[1], block_size, block_size])

def draw_food(x, y):
    pygame.draw.rect(screen, red, [x, y, block_size, block_size])

def show_score(score):
    value = font.render(f"Score: {score}", True, white)
    screen.blit(value, [10, 10])

def message(text, color, y_offset=0):
    msg = font.render(text, True, color)
    rect = msg.get_rect(center=(width // 2, height // 2 + y_offset))
    screen.blit(msg, rect)

def game_loop():
    x = width // 2
    y = height // 2
    dx = block_size
    dy = 0

    snake = []
    snake_length = 1

    food_x = round(random.randrange(0, width - block_size) / block_size) * block_size
    food_y = round(random.randrange(0, height - block_size) / block_size) * block_size

    score = 0
    game_over = False
    game_close = False

    while not game_over:

        while game_close:
            screen.fill(black)
            message("Game Over", red, -30)
            message("Press R to Restart or Q to Quit", white, 20)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx == 0:
                    dx = -block_size
                    dy = 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx = block_size
                    dy = 0
                elif event.key == pygame.K_UP and dy == 0:
                    dx = 0
                    dy = -block_size
                elif event.key == pygame.K_DOWN and dy == 0:
                    dx = 0
                    dy = block_size

        x += dx
        y += dy

        # Hit wall?
        if x < 0 or x >= width or y < 0 or y >= height:
            game_close = True

        screen.fill(black)
        draw_food(food_x, food_y)

        snake_head = [x, y]
        snake.append(snake_head)

        if len(snake) > snake_length:
            del snake[0]

        # Hit self?
        for block in snake[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(snake)
        show_score(score)

        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - block_size) / block_size) * block_size
            food_y = round(random.randrange(0, height - block_size) / block_size) * block_size
            snake_length += 1
            score += 10

        clock.tick(speed)

    pygame.quit()
    quit()

game_loop()
