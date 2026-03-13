import pygame
from circleshape import CircleShape
from shot import Shot
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED, SHOT_RADIUS, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN_SECONDS


class Player(CircleShape):
    color = "white"
    shot_limiter = 0
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

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

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def respawn(self, x, y):
        self.position.x = x
        self.position.y = y

    def update(self, dt):
        self.shot_limiter -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
            #print("Pressed a")
        if keys[pygame.K_d]:
            self.rotate(dt)
            #print("Pressed d")
        if keys[pygame.K_w]:
            self.move(dt)
            #print("Pressed w")
        if keys[pygame.K_s]:
            self.move(-dt)
            #print("Pressed s")
        if keys[pygame.K_SPACE]:
            self.shoot()
            #print("Pressed s")

    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rot_vector = unit_vector.rotate(self.rotation)
        rot_vector_speed = rot_vector * PLAYER_SPEED * dt
        self.position += rot_vector_speed

    def shoot(self):
        if self.shot_limiter > 0:
            #print("can't shoot")
            return
        else:
            #print("resetting shooter")
            self.shot_limiter = PLAYER_SHOOT_COOLDOWN_SECONDS
            #print("Allowing shooting")
            shot = Shot(self.position.x, self.position.y)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation)*PLAYER_SHOOT_SPEED