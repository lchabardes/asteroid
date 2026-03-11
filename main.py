
import pygame
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS

def main():
    print(f"Starting Asteroids with pygame: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(x, y)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        for upd in updatable:
            upd.update(dt)
        for dra in drawable:
            dra.draw(screen)
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000
        log_state()
        #print(f"deltaTime: {dt}")

if __name__ == "__main__":
    main()

