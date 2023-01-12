import pygame
import random

class Fleche(pygame.sprite.Sprite):
    def __init__(self,chemin):
        super().__init__()
        self.image = pygame.image.load(chemin)
        self.rect = self.image.get_rect()
        self.vitesse = 15
        self.rect.y = 800

    def defilement(self,compteur):
        if compteur in [20,100,250]:
            self.vitesse = self.vitesse * 1.75
        self.rect.y -= self.vitesse

