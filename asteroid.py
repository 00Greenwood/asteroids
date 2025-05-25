from circleshape import CircleShape
from constants import *
import pygame
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        left = self.velocity.rotate(angle) * 1.2
        right = self.velocity.rotate(-angle) * 1.2
        radius = self.radius - ASTEROID_MIN_RADIUS
        Asteroid(self.position.x, self.position.y, radius).velocity = left
        Asteroid(self.position.x, self.position.y, radius).velocity = right

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
