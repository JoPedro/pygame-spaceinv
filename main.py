"""This is a recreation of the Space Invaders game using PyGame"""
# pylint: disable=C

import random
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

# Player
player_img = pygame.image.load("img/ship.png")
player_x = 370
player_y = 480
player_x_change = 0

# Enemy
enemy_img = pygame.image.load("img/alien1.png")
enemy_x = random.randint(0, 736)
enemy_y = random.randint(50, 150)
enemy_x_change = 10
enemy_y_change = 40

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

def enemy(pos_x, pos_y):
    screen.blit(enemy_img, (pos_x, pos_y))

def fire_bullet(pos_x, pos_y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (pos_x + 16, pos_y + 10))

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
                player_x_change = -1
            if event.key == pygame.K_RIGHT:
                player_x_change = 1
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    # Current x coordinate of spaceship
                    bullet_x = player_x
                    bullet_state = "fire"

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

        if event.type == MOVEEVENT: # called every 't' milliseconds
            # Enemy movement
            enemy_x += enemy_x_change

            if enemy_x <= 0:
                if t > 50: t -= 50
                pygame.time.set_timer(MOVEEVENT, t)
                enemy_x_change = 10
                enemy_y += enemy_y_change
            elif enemy_x >= 736:
                if t > 50: t -= 50
                pygame.time.set_timer(MOVEEVENT, t)
                enemy_x_change = -10
                enemy_y += enemy_y_change

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
    enemy(enemy_x, enemy_y)
    pygame.display.update()
