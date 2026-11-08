import pygame
from random import randint
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init();
class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.circle(self.image, color, [self.image.get_width()//2, self.image.get_height()//2], 17)

        self.velocity = [randint(-4, 8), randint(-8, 8)]
        

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        pass
        
    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8, 8)
        pass
