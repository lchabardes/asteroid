
import pygame
import sys
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from gamestate import GameState
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
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(x, y)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    Shot.containers = (shots, updatable, drawable)

    score = GameState()
    font = pygame.font.Font(None, 36)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        score_text = f"Score: {score.get_score()}"
        lives_text = f"Lives: {score.get_lives()}"

        score_surf = font.render(score_text, True, (255, 255, 255))
        lives_surf = font.render(lives_text, True, (255, 255, 255))

        # Blit HUD
        screen.fill((0, 0, 0))
        screen.blit(score_surf, (10, 10))
        screen.blit(lives_surf, (10, 40))

        for upd in updatable:
            upd.update(dt)
        for ast in asteroids:
            if ast.collides_with(player):
                log_event("player_hit")
                score.hit_ast()
                player.respawn(x, y)
            for shot in shots:
                if ast.collides_with(shot):
                    log_event("asteroid_shot")
                    score.kill_ast()
                    ast.split()
                    shot.kill()
        for dra in drawable:
            dra.draw(screen)
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000
        log_state()
        #print(f"deltaTime: {dt}")

if __name__ == "__main__":
    main()

