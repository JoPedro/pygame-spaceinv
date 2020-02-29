"""This is a recreation of the Space Invaders game using PyGame"""
# pylint: disable=C

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
score = 0

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
    enemy_x_change.append(0.1)
    enemy_y_change.append(40)

# Bullet
bullet_img = pygame.image.load("img/bullet.png")
bullet_x = 0
bullet_y = 480
bullet_y_change = 2
# Ready - Bullet is not visible
# Fire - Bullet is moving
bullet_state = "ready"

MOVEEVENT, t = pygame.USEREVENT, 500
pygame.time.set_timer(MOVEEVENT, t)

def player(pos_x, pos_y):
    screen.blit(player_img, (pos_x, pos_y))

def enemy(pos_x, pos_y, i):
    screen.blit(enemy_img[i], (pos_x, pos_y))

def fire_bullet(pos_x, pos_y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (pos_x + 16, pos_y + 10))

def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    dist = math.sqrt((math.pow(enemy_x - bullet_x, 2)) + (math.pow(enemy_y - bullet_y, 2)))
    if dist < 27:
        return True
    else:
        return False

# Main Game loop
running = True
while running:
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
                player_x_change = -0.5
            if event.key == pygame.K_RIGHT:
                player_x_change = 0.5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    # Current x coordinate of spaceship
                    bullet_x = player_x
                    bullet_state = "fire"

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0 

        #Enemies movement
        #if event.type == MOVEEVENT: # called every 't' milliseconds
        # paste enemies movements

                #if enemy_y[i] > 50:
                    #if t > 50: t -= 50 * ((enemy_y[i] - 50)//40)
                    #pygame.time.set_timer(MOVEEVENT, t)
                    #enemy_x_change[i] = 1
                    #enemy_y[i] += enemy_y_change[i]                       

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
            enemy_x_change[i] = 0.1
            enemy_y[i] += enemy_y_change[i]
        elif enemy_x[i] >= 735:
            enemy_x_change[i] = -0.1
            enemy_y[i] += enemy_y_change[i]

        # Collision test
        collision = is_collision(enemy_x[i], enemy_y[i], bullet_x, bullet_y)

        if collision:
            bullet_y = 480
            bullet_state = "ready"
            score += 1
            print(score)
            enemy_x[i] = random.randint(0, 735)
            enemy_y[i] = random.randint(50, 150)

        enemy(enemy_x[i], enemy_y[i], i)

    pygame.display.update()
