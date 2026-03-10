import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        color = "white"

    # in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen): 
        triangle_coord = self.triangle()
        pygame.draw.polygon(screen, "white", triangle_coord, LINE_WIDTH)
        