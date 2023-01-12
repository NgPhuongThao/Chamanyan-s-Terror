import pygame
from dialogue import Dialogue
pygame.init()
ecran = pygame.display.set_mode((720,580))
marche=None
running = True
scene=None

dialogue = Dialogue(ecran)

while running:
    pygame.display.flip()

    for evenement in pygame.event.get():
        #Fermeture du jeu
        if (evenement.type == pygame.QUIT):
            running = False
            pygame.quit()

        elif ((evenement.type == pygame.KEYDOWN)or (evenement.type == pygame.MOUSEBUTTONDOWN)):
            if scene==None:
                marche=dialogue.scene1(evenement,marche)
                if marche == False:
                    scene=2
            if scene==2:
                marche=dialogue.scene2(evenement,marche)
                if marche == False:
                    scene=3
            if scene==3:
                marche=dialogue.scene3(evenement,marche)
                if marche == False:
                    scene=4

