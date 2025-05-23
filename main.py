import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    print("Starting Asteroids!")

    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (bullets, updateable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 

        updateable.update(dt)

        for asteroid in asteroids:
            if asteroid.isColliding(player):
                sys.exit("Game over!")
            for asteroid in asteroids:
                for bullet in bullets:
                    if bullet.isColliding(asteroid):
                        bullet.kill()
                        asteroid.split()
        
        
        
        screen.fill("black")
        
        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 fps
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
