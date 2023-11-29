import os
import pygame

from game_object import GameObject


class PacMan(GameObject):
    sprite_filename = "pacman"


def compose_context(screen):
    return {
        "pacman": PacMan(screen.get_width() // 2, screen.get_height() // 2),
    }


def draw_whole_screen(screen, context):
    screen.fill("gray")
    context["pacman"].draw(screen)


def main():
    pygame.init()

    screen = pygame.display.set_mode((1280, 960))
    clock = pygame.time.Clock()
    running = True
    player_speed = 3
    dt = 0

    context = compose_context(screen)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_whole_screen(screen, context)
        pygame.display.flip()

        keys = pygame.key.get_pressed()
        old_player_topleft = context["pacman"].rect.topleft
        if keys[pygame.K_w]:
            context["pacman"].rect = context["pacman"].rect.move(0, -1 * player_speed)
        if keys[pygame.K_s]:
            context["pacman"].rect = context["pacman"].rect.move(0, player_speed)
        if keys[pygame.K_a]:
            context["pacman"].rect = context["pacman"].rect.move(-1 * player_speed, 0)
        if keys[pygame.K_d]:
            context["pacman"].rect = context["pacman"].rect.move(player_speed, 0)

    pygame.quit()


if __name__ == "__main__":
    main()
