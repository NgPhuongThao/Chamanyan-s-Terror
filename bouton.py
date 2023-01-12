import pygame

class Bouton(pygame.sprite.Sprite):
    def __init__(self,chemin):
        super().__init__()
        self.image = pygame.image.load(chemin)
        self.rect = self.image.get_rect()
