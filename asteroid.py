import pygame

from circleshape import CircleShape 
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED

class Asteriod(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)


    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        # Override the update() method so that it moves in a straight line at constant speed. 
        # On each frame, it should add (self.velocity * dt) to its position (get self.velocity from its parent class, CircleShape).
        self.position += self.velocity * dt
