import pygame

class Joueur(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #self.nom = nom
        self.vitesse = 10
        self.inventaire = []
        self.image = pygame.image.load('assets/joueur/joueur.png')
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 50

        self.score = 0

    #def str(self):

    #def repr(self):

    def droite(self):
        self.rect.x += self.vitesse

    def gauche(self):
        self.rect.x -= self.vitesse

    def haut(self):
        self.rect.y -= self.vitesse

    def bas(self):
        self.rect.y += self.vitesse