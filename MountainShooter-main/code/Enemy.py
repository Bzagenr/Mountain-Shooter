#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_HEIGHT
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        self.flow = -1  # Direção inicial: -1 para subir, 1 para descer
        self.spd = 0

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def move_enemy3(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        self.rect.centery += ENTITY_SPEED[self.name] * self.flow
        if self.rect.bottom >= WIN_HEIGHT:
            self.rect.bottom = WIN_HEIGHT
            self.flow = -1
            self.spd = ENTITY_SPEED[self.name]
        elif self.rect.top <= 0:
            self.rect.top = 0
            self.flow = 1
            self.spd = ENTITY_SPEED[self.name] * 2
        self.rect.centery += self.spd * self.flow

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
