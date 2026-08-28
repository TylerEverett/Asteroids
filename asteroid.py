import pygame
import random

from circleshape import CircleShape
from logger import log_event
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)


    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        # Override the update() method so that it moves in a straight line at constant speed. 
        # On each frame, it should add (self.velocity * dt) to its position (get self.velocity from its parent class, CircleShape).
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
        
        if(self.radius <= ASTEROID_MIN_RADIUS):
            return
        
        log_event("asteroid_split")
        
        angle = random.uniform(20, 50)
        pos_velocity = self.velocity.rotate(angle)
        neg_velocity = self.velocity.rotate(-angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        pos_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        pos_asteroid.velocity = pos_velocity * 1.2
        neg_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        neg_asteroid.velocity = neg_velocity * 1.2
