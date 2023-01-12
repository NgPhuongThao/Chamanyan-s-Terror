import pygame
from joueur import Joueur
from bouton import Bouton
from PNJ import PNJ
from fleche import Fleche
import random
pygame.mixer.init()

class Jeu:
    def __init__(self,ecran):
        #générer un joueur
        self.joueur = Joueur()
        self.Nyatacha = PNJ('assets/nyatacha_pixel.png')
        self.pc = PNJ('assets/pc.png')
        self.pc.rect.x,self.pc.rect.y = 500,90

        self.appuye = {
        }
        self.joue = False
        self.option = False
        self.bouton_jouer = Bouton('assets/jouer.png')

        self.all_fleches = pygame.sprite.Group()
        self.compteur = 0
        self.fleches ={
            "f_g" : (0,'assets/nyatacha_rythm/fleche_gauche_touche.png',10),
            "f_h" : (1,'assets/nyatacha_rythm/fleche_haut_touche.png',110),
            "f_d" : (2,'assets/nyatacha_rythm/fleche_droite_touche.png',310),
            "f_b" : (3,'assets/nyatacha_rythm/fleche_bas_touche.png',210)
            }
        for j in range(300):
            self.compteur = j
            a = random.randint(0,3)
            b = random.randint(0,1)
            for i in self.fleches:
                if a == self.fleches[i][0]:
                    f = Fleche(self.fleches[i][1])
                    f.rect.x = self.fleches[i][2]
                    f.rect.y = f.rect.y + 170*(j-b)
                    self.all_fleches.add(f)
        self.fleche_compteur=300


    def maj(self,ecran,option,evenement,marche):
        if self.option:
            self.options(ecran,evenement)
        elif self.Nyatacha.parle:
            self.nyatacha_rythm(ecran,evenement)
        elif self.pc.parle:
            croix = pygame.image.load("assets/croix.png")
            croix_rect = croix.get_rect()
            croix_rect.x,croix_rect.y = 600,5
            ecran_pc = pygame.image.load('assets/ecran_pc.png')
            noirci = pygame.image.load('assets/noirci.png')

            ecran.blit(noirci,(0,0))
            ecran.blit(ecran_pc,(5,5))
            ecran.blit(croix,croix_rect)

            if evenement.type == pygame.MOUSEBUTTONDOWN and croix_rect.collidepoint(evenement.pos):
                self.pc.parle = False
        elif self.Nyatacha.win:
            #Images
            self.Nyatacha.image = pygame.image.load('assets/nyatacha_pixel.png')
            self.Nyatacha.rect.x, self.Nyatacha.rect.y = 80,300
            bg = pygame.image.load('assets/bg/salle_info.png')
            ecran.blit(bg,(0,0))
            ecran.blit(self.pc.image,self.pc.rect)
            ecran.blit(self.joueur.image,self.joueur.rect)
            ecran.blit(self.Nyatacha.image, self.Nyatacha.rect)

            if (self.appuye.get(pygame.K_RIGHT) and (self.joueur.rect.x + self.joueur.rect.width < ecran.get_width()-10)):
                self.joueur.droite()
            elif self.appuye.get(pygame.K_LEFT) and (self.joueur.rect.x > 50):
                self.joueur.gauche()
            elif self.appuye.get(pygame.K_UP)and (self.joueur.rect.y > 50):
                self.joueur.haut()
            elif(self.appuye.get(pygame.K_DOWN))and (self.joueur.rect.y + self.joueur.rect.height < ecran.get_height()-5):
                self.joueur.bas()

        option.rect.x, option.rect.y = 0,0
        ecran.blit(option.image,option.rect)

        #mise à jour de l'écran

        pygame.display.flip()

    def options(self,ecran,evenement):
        #Images
        interface_options = pygame.image.load('assets/interface_options.png')
        quitter=Bouton('assets/quitter.png')
        quitter.rect.x, quitter.rect.y = 360,400

        ecran.blit(interface_options,(150,110))
        ecran.blit(quitter.image,quitter.rect)

        if (evenement.type == pygame.MOUSEBUTTONDOWN):
            if (quitter.rect.collidepoint(evenement.pos)):
                self.option=False

        pygame.display.flip()

    def nyatacha_rythm(self,ecran,evenement):
        #Chargement des images
        bg = pygame.image.load('assets/bg/nyatacha_rythm.png')
        barre = pygame.image.load("assets/nyatacha_rythm/barre.png")
        noirci = pygame.image.load('assets/noirci.png')
        espace = pygame.image.load('assets/espace.png')
        self.Nyatacha.win = False

        #placement des sprites
        ecran.blit(bg,(0,0))
        ecran.blit(barre,(20,280))

        #Le Jeu
        if self.Nyatacha.jouer == False:
            ecran.blit(noirci,(0,0))
            self.bouton_jouer.rect.x, self.bouton_jouer.rect.y = 240,220
            ecran.blit(self.bouton_jouer.image,self.bouton_jouer.rect)
        elif self.joueur.score>=3000:
            pygame.mixer.music.stop()
            pygame.mixer.music.load('assets/sons/Nyan_Cat.ogg')
            pygame.mixer.music.play(20,0)
            pygame.mixer.music.set_volume(0.5)
            self.Nyatacha.parle = False
        else:
            self.compteur += 1
            for fleche in self.all_fleches:
                fleche.defilement(self.compteur)
                if fleche.rect.y < 240:
                    self.all_fleches.remove(fleche)
                if evenement.type == pygame.KEYDOWN and fleche.rect.y < 320:
                    if evenement.key == pygame.K_LEFT and fleche.rect.x == 10:
                        self.joueur.score += int((400 - fleche.rect.y)/10)
                    if evenement.key == pygame.K_RIGHT and fleche.rect.x == 310:
                        self.joueur.score += int((400 - fleche.rect.y)/10)
                    if evenement.key == pygame.K_UP and fleche.rect.x == 110:
                        self.joueur.score += int((400 - fleche.rect.y)/10)
                    if evenement.key == pygame.K_DOWN and fleche.rect.x == 210:
                        self.joueur.score += int((400 - fleche.rect.y)/10)
            font = pygame.font.SysFont('Comic Sans Ms',60)
            texte=('{}'.format(str(self.joueur.score)))
            scoree=font.render(texte,True,(255,255,255))
            ecran.blit(scoree,(200,50))

            self.Nyatacha.image = pygame.image.load('assets/nyatacha/nyatacha_rythm1.png')
            self.Nyatacha.rect.x,self.Nyatacha.rect.y = 200,20
            ecran.blit(self.Nyatacha.image,self.Nyatacha.rect)

            self.all_fleches.draw(ecran)