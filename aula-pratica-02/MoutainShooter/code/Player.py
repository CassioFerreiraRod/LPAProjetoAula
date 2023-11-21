#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key

from code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, \
    PLAYER_KEY_RIGHT

from code.Entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ENTIRY_SPEED=None):
        preseed_key = pygame.key.get_pressed()
        if preseed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:  # Se a tecla para cima for pressionada
            self.rect.centery -= ENTITY_SPEED[self.name]

        if preseed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:  # Se a tecla para cima for pressionada
            self.rect.centery += ENTITY_SPEED[self.name]

        if preseed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:  # Se a tecla para cima for pressionada
            self.rect.centerx -= ENTITY_SPEED[self.name]

        if preseed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:  # Se a tecla para cima for pressionada
            self.rect.centerx += ENTITY_SPEED[self.name]
