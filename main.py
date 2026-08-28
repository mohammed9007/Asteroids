import sys

import pygame

from asteroid import *
from asteroidfield import *

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_event, log_state
from player import *


def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable  = pygame.sprite.Group()
    asteroids  = pygame.sprite.Group()
    
    AsteroidField.containers = updatable
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
 
    clock = pygame.time.Clock()
    
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field1 = AsteroidField()
    
    dt = 0.0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        
       
            
        updatable.update(dt)
        for asteroid in asteroids:
            if player1.collideds_with(asteroid):
               log_event("player_hit")
               print("Game over!")
               sys.exit()

        screen.fill("black")
        
        for draw in drawable:
            draw.draw(screen)
        pygame.display.flip()
   
        dt = clock.tick(60) / 1000  
        log_state()


if __name__ == "__main__":
    main()
