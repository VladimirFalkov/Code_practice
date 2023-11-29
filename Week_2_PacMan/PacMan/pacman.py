import os
import pygame
from pygame.sprite import Group

from game_object import GameObject


class PacMan(GameObject):
    sprite_filename = "pacman"


class Wall(GameObject):
    sprite_filename = "wall"


def calculate_walls_coordinates(
    screen_width, screen_heights, wall_block_width, wall_block_height
):
    walls_coordinates = []
    horizontal_wall_block_ammount = screen_width // wall_block_width
    vertical_wall_block_ammount = screen_heights // wall_block_width

    for block_num in range(horizontal_wall_block_ammount):
        walls_coordinates.extend(
            [
                (block_num * wall_block_width, 0),
                (block_num * wall_block_width, screen_heights - wall_block_height),
            ]
        )

    for block_num in range(1, vertical_wall_block_ammount - 1):
        walls_coordinates.extend(
            [
                (0, block_num * wall_block_height),
                (screen_width - wall_block_width, block_num * wall_block_width),
            ]
        )
    for time in range(1, 7):
        for block_num in range(2 * time, vertical_wall_block_ammount - 2 * time):
            walls_coordinates.extend(
                [
                    (2 * time * wall_block_width, block_num * wall_block_height),
                    (
                        (horizontal_wall_block_ammount - 1 - 1 * time - time)
                        * wall_block_width,
                        block_num * wall_block_height,
                    ),
                ]
            )
    for block_num in range(2, horizontal_wall_block_ammount // 2 - 1):
        walls_coordinates.extend(
            [
                ((block_num) * wall_block_width, 2 * wall_block_height),
            ]
        )
    for block_num in range(
        horizontal_wall_block_ammount // 2 + 1, horizontal_wall_block_ammount - 2
    ):
        walls_coordinates.extend(
            [
                ((block_num) * wall_block_width, 2 * wall_block_height),
            ]
        )
        # for block_num in range(2 + 2, vertical_wall_block_ammount - 2 - 2):
        #     walls_coordinates.extend(
        #         [
        #             ((2 + 2) * wall_block_width, block_num * wall_block_height),
        #             (
        #                 (horizontal_wall_block_ammount - 3 - 2) * wall_block_width,
        #                 block_num * wall_block_height,
        #             ),
        #         ]
        #     )
        # for block_num in range(2 + 2 + 2, vertical_wall_block_ammount - 2 - 2 - 2):
        #     walls_coordinates.extend(
        #         [
        #             ((2 + 2 + 2) * wall_block_width, block_num * wall_block_height),
        #             (
        #                 (horizontal_wall_block_ammount - 3 - 2 - 2) * wall_block_width,
        #                 block_num * wall_block_height,
        #             ),
        #         ]
        #     )

        # for block_num in range(2 + 2 + 2 + 2, vertical_wall_block_ammount - 2 - 2 - 2):
        #     walls_coordinates.extend(
        #         [
        #             ((2 + 2 + 2 + 2) * wall_block_width, block_num * wall_block_height),
        #             (
        #                 (horizontal_wall_block_ammount - 3 - 2 - 2 - 2) * wall_block_width,
        #                 block_num * wall_block_height,
        #             ),
        #         ]
        #     )

        # for block_num in range(
        #     2 + 2 + 2 + 2 + 2, vertical_wall_block_ammount - 2 - 2 - 2 - 2
        # ):
        #     walls_coordinates.extend(
        #         [
        #             ((2 + 2 + 2 + 2 + 2) * wall_block_width, block_num * wall_block_height),
        #             (
        #                 (horizontal_wall_block_ammount - 3 - 2 - 2 - 2 - 2)
        #                 * wall_block_width,
        #                 block_num * wall_block_height,
        #             ),
        #         ]
        #     )
        # for block_num in range(
        #     2 + 2 + 2 + 2 + 2 + 2, vertical_wall_block_ammount - 2 - 2 - 2 - 2 - 2
        # ):
        #     walls_coordinates.extend(
        #         [
        #             (
        #                 (2 + 2 + 2 + 2 + 2 + 2) * wall_block_width,
        #                 block_num * wall_block_height,
        #             ),
        #             (
        #                 (horizontal_wall_block_ammount - 3 - 2 - 2 - 2 - 2 - 2)
        #                 * wall_block_width,
        #                 block_num * wall_block_height,
        #             ),
        #         ]
        #     )

    return walls_coordinates


def compose_context(screen):
    walls_coordinates = calculate_walls_coordinates(
        screen.get_width(), screen.get_height(), Wall.width, Wall.height
    )
    return {
        "pacman": PacMan(screen.get_width() // 2, screen.get_height() // 2),
        "walls": Group(*[Wall(x, y) for x, y, in walls_coordinates]),
    }


def draw_whole_screen(screen, context):
    screen.fill("gray")
    context["pacman"].draw(screen)
    context["walls"].draw(screen)


def main():
    pygame.init()

    screen = pygame.display.set_mode((1280, 1000))
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
