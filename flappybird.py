import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Colors
SKY_BLUE = (135, 206, 235)
GREEN = (0, 128, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Bird
bird_radius = 20
bird = pygame.Rect(WIDTH//4, HEIGHT//2, bird_radius*2, bird_radius*2)
bird_speed = 0
gravity = 0.5
flap_strength = -8

# Update the game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_speed = flap_strength
    
    # Bird movement
    bird_speed += gravity
    bird.y += bird_speed
    
    # Drawing
    screen.fill(SKY_BLUE)
    pygame.draw.ellipse(screen, RED, bird)
    pygame.draw.ellipse(screen, BLACK, bird, 2)  # Outline
    
    pygame.display.flip()
    clock.tick(60)