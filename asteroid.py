import pygame
from constants import * 
import random
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x , y, radius):
        super().__init__(x , y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
            
        angle = random.uniform(20,50)

        first_velocity = self.velocity.rotate(angle)
        second_velocity = self.velocity.rotate(-angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = first_velocity * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = second_velocity * 1.2    