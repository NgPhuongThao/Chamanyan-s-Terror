import pygame

class PNJ(pygame.sprite.Sprite):
    def __init__(self, chemin):
        super().__init__()
        self.affection = 0
        self.passe = False
        self.image = pygame.image.load(chemin)
        self.rect = self.image.get_rect()
        self.parle = False
        self.jouer = False
        self.win = True