import pygame
from jeu import Jeu
from fleche import Fleche
from bouton import Bouton
from dialogue import Dialogue

pygame.init()
pygame.mixer.init()

#Fenêtre du jeu
icone = pygame.image.load('assets/icone.png')
pygame.display.set_caption("Chamanyan's Terror")
pygame.display.set_icon(icone)

#Chargement d'images
noirci = pygame.image.load('assets/noirci.png')
ecran = pygame.display.set_mode((720,580))
bg = pygame.image.load('assets/bg/accueil.png')
space = pygame.image.load('assets/espace.png')
jouer = Bouton('assets/jouer.png')
jouer.rect.x, jouer.rect.y = 240,300
option = Bouton('assets/options.png')
option.rect.x, option.rect.y = 270,400
logo = pygame.image.load('assets/logo.png')
OPTIONS = pygame.image.load('assets/interface_options.png')

#Sons
pygame.mixer.music.load('assets/sons/Nyan_Cat.ogg')
pygame.mixer.music.play(20,0)
pygame.mixer.music.set_volume(0.5)
caramell = pygame.mixer.Sound('assets/sons/Caramelldansen.ogg')
pas =pygame.mixer.Sound('assets/sons/pas.ogg')
pas.set_volume(0.3)
clavier = pygame.mixer.Sound('assets/sons/clavier.ogg')
clavier.set_volume(0.5)
Nya_Arigato = pygame.mixer.Sound('assets/sons/nya-arigato.ogg')
Nya_Arigato.set_volume(0.2)
Nya = pygame.mixer.Sound("assets/sons/nya.ogg")
Nya.set_volume(0.2)

#variables
jeu = Jeu(ecran)
horloge = pygame.time.Clock()

#Dialogues
dialogue = Dialogue(ecran)
marche = None
scene = 1

running = True
while running:
    horloge.tick(30)

    #vérifier si le jeu a commencé
    if marche == 4:
        jeu.maj(ecran,option,evenement,marche)
    elif jeu.option:
        jeu.options(ecran,evenement)
    elif not jeu.joue:
        #Images
        ecran.blit(bg,(0,0))
        ecran.blit(jouer.image,jouer.rect)
        ecran.blit(logo,(10,30))
        ecran.blit(option.image,option.rect)

    #mise à jour de l'écran
    pygame.display.flip()

    for evenement in pygame.event.get():
        #Fermeture du jeu
        if (evenement.type == pygame.QUIT):
            running = False
            pygame.quit()

        elif (evenement.type == pygame.MOUSEBUTTONDOWN):
            #vérifier si la souris est en collision avec "Jouer"
            if jouer.rect.collidepoint(evenement.pos):
                jeu.joue = True
            elif (option.rect.collidepoint(evenement.pos)):
                jeu.option = True
            elif (jeu.bouton_jouer.rect.collidepoint(evenement.pos)):
                jeu.Nyatacha.jouer = True
                pygame.mixer.music.rewind()
                pygame.mixer.music.set_volume(0.2)

        #touche maintenue ?

        elif (evenement.type == pygame.KEYDOWN):
            if jeu.joueur.rect.colliderect(jeu.Nyatacha.rect):
                ecran.blit(space,(500,500))
            if jeu.joueur.rect.colliderect(jeu.pc.rect) and (jeu.pc.parle != True):
                ecran.blit(space,(500,500))

            if evenement.key == pygame.K_SPACE and jeu.joueur.rect.colliderect(jeu.Nyatacha.rect):
                if jeu.joueur.score==0:
                    jeu.Nyatacha.parle = True
                    marche = False
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load('assets/sons/Caramelldansen.ogg')
                    pygame.mixer.music.play()
                    pygame.mixer.music.set_volume(0.025)
                    jeu.joueur.rect.x = 500

            elif evenement.key == pygame.K_SPACE and jeu.joueur.rect.colliderect(jeu.pc.rect):
                clavier.play()
                if jeu.joueur.score==0:
                    jeu.pc.parle = True
                else:
                        if marche==4:
                            ecran.blit(noirci,(0,0))
                            ecran.blit(noirci,(0,0))
                            ecran.blit(noirci,(0,0))
                            marche=dialogue.fin(evenement,marche)
                        else:
                             pygame.display.set_mode((720,580))
                             marche=dialogue.finfini(evenement,marche)

            jeu.appuye[evenement.key] = True
            if not jeu.Nyatacha.jouer and not jeu.Nyatacha.parle and jeu.joue and marche == 4 and jeu.appuye.get(pygame.K_LEFT) or jeu.appuye.get(pygame.K_RIGHT) or jeu.appuye.get(pygame.K_UP) or jeu.appuye.get(pygame.K_DOWN):
                pas.play()
            else:
                Nya_Arigato.play()
        elif (evenement.type == pygame.KEYUP):
            jeu.appuye[evenement.key] = False

        if jeu.joueur.score >=3000:
            dialogue.scene3(evenement,marche)
            if dialogue.marche == 5:
                jeu.Nyatacha.win = True
        elif jeu.Nyatacha.win and (not jeu.joueur.rect.colliderect(jeu.pc.rect) and (evenement.type == pygame.KEYDOWN) or (evenement.type == pygame.MOUSEBUTTONDOWN)):
            if marche!=4 and jeu.Nyatacha.parle and marche!=1000 :
                marche=dialogue.scene2(evenement,marche)
                Nya.play()
            elif jeu.joue and marche != 4:
                marche=dialogue.scene1(evenement,marche)