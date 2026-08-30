import pygame
import random

from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt: float) -> None:
        self.position   += self.velocity * dt
    
    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return "this was a small asteroid and we're done"
        else:
            log_event("asteroid_split")
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            astroid_smaller1 = Asteroid(self.position.x, self.position.y , new_radius)
            astroid_smaller2 = Asteroid(self.position.x, self.position.y , new_radius)  
            astroid_smaller1.velocity.rotate(random.uniform(20,50))
            astroid_smaller2.velocity.rotate(-(random.uniform(20,50)))
            astroid_smaller1.velocity = -self.velocity * 1.2
            astroid_smaller2.velocity = self.velocity * 1.2
            self.kill()