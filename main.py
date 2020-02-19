"""This is a recreation of the Space Invaders game using PyGame"""
import pygame

# PyGame initialization
pygame.init()

def main():
    """This function calls the main program"""

    # Screen creation
    screen = pygame.display.set_mode((800, 600))

    # Title and Icon
    pygame.display.set_caption("Space Invaders")
    icon = pygame.image.load("img/ufo.png")
    pygame.display.set_icon(icon)

    # Player
    player_img = pygame.image.load("img/ship.png")
    player_x = 370
    player_y = 480

    def player():
        screen.blit(player_img, (player_x, player_y))

    # Main Game loop
    running = True
    while running:
        # RGB Screen Background color
        screen.fill((67, 81, 122))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player()
        pygame.display.update()

main()
