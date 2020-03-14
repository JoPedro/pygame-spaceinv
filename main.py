"""This is a recreation of the Space Invaders game using PyGame"""

import random
import math
import pygame

# PyGame initialization
pygame.init()

# Screen creation
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('img/background.png')

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("img/ufo.png")
pygame.display.set_icon(icon)

# Score
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
text_x = 10
text_y = 10

def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

# Clock and FPS
clock = pygame.time.Clock()
dt = clock.tick(60)

# Player
player_img = pygame.image.load("img/ship.png")
player_x = 370
player_y = 480
player_x_change = 0

# Enemies
n_enemies = 6
enemy_img, enemy_x, enemy_y, enemy_x_change, enemy_y_change = [], [], [], [], []

for i in range(n_enemies):
    enemy_img.append(pygame.image.load("img/alien1.png"))
    enemy_x.append(random.randint(0, 735))
    enemy_y.append(random.randint(50, 150))
    enemy_x_change.append(0.1 * dt)
    enemy_y_change.append(40)

# Bullet
bullet_img = pygame.image.load("img/bullet.png")
bullet_x = 0
bullet_y = 480
bullet_y_change = 2 * dt
# Ready - Bullet is not visible
# Fire - Bullet is moving
bullet_state = "ready"

# MOVEEVENT, t = pygame.USEREVENT, 500
# pygame.time.set_timer(MOVEEVENT, t)

def player(x, y):
    screen.blit(player_img, (x, y))

def enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y + 10))

def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    dist = math.sqrt((math.pow(enemy_x - bullet_x, 2)) + (math.pow(enemy_y - bullet_y, 2)))
    if dist < 27:
        return True
    else:
        return False

# Main Game loop
running = True
while running:
    # Frame Tick
    dt = clock.tick(60)

    # RGB Screen Background color
    screen.fill((67, 81, 122))
    # Background Image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Keystroke direction check
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -0.5 * dt
            if event.key == pygame.K_RIGHT:
                player_x_change = 0.5 * dt
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    # Current x coordinate of spaceship
                    bullet_x = player_x
                    bullet_state = "fire"

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0                  

    # Spaceship movement
    player_x += player_x_change

    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736        

    # Bullet movement
    if bullet_y <= -32:
        bullet_y = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    player(player_x, player_y)

    for i in range(n_enemies):
        enemy_x[i] += enemy_x_change[i]

        if enemy_x[i] <= 0:
            enemy_x_change[i] = 0.1 * dt
            enemy_y[i] += enemy_y_change[i]
        elif enemy_x[i] >= 735:
            enemy_x_change[i] = -0.1 * dt
            enemy_y[i] += enemy_y_change[i]

        # Collision test
        collision = is_collision(enemy_x[i], enemy_y[i], bullet_x, bullet_y)

        if collision:
            bullet_y = 480
            bullet_state = "ready"
            score_value += 1
            enemy_x[i] = random.randint(0, 735)
            enemy_y[i] = random.randint(50, 150)

        enemy(enemy_x[i], enemy_y[i], i)

    show_score(text_x, text_y)
    pygame.display.update()
