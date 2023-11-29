import os
import pygame

from game_object import GameObject


class PacMan(GameObject):
    sprite_filename = "pacman"


def compose_context(screen):
    return {}
