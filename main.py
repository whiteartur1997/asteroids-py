import sys

import pygame
from asteroid import Asteroid
from constants import  SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000
        screen.fill("black")
        updatable.update(dt)
        for thing in drawable:
            thing.draw(screen)
        for asteroid in asteroids:
            for shot in shots:
                collision_detected = asteroid.collides_with(shot)  
                if collision_detected:
                    log_event("asteroid_shot")
                    shot.kill() 
                    asteroid.split() 
        for asteroid in asteroids:
            collision_detected = asteroid.collides_with(player)
            if collision_detected:
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        pygame.display.flip()


if __name__ == "__main__":
    main()
