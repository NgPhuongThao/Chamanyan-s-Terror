import pygame

class Dialogue:
    def __init__(self,ecran):
        self.scene=False
        self.ecran = ecran
        self.couleur = (255,255,255)
        self.font = pygame.font.SysFont('Comic Sans Ms',20)
        self.marche = 4
        self.nyat=pygame.image.load('assets/nyatacha/nyatacha.png')

    def texte(self,texte,nombre):
        if nombre==1:
            self.ecran = pygame.display.set_mode((720,580))
            image_texte = self.font.render(texte,True,self.couleur)
            self.ecran.blit(image_texte,(10,410))
        elif nombre==2:
            image_texte = self.font.render(texte,True,self.couleur)
            self.ecran.blit(image_texte,(30,450))


    def scene1(self,evenement,marche):
        if (marche==None ):
            self.texte("... J'ai faim...",1)
            return 1
        elif evenement.type==pygame.KEYDOWN and evenement.key==pygame.K_SPACE and marche==1 :
            self.texte("Vous dirigez votre main vers le paquet de Chamanyan",1)
            return 2
        elif (evenement.type==pygame.KEYDOWN and evenement.key==pygame.K_SPACE and marche==2):
            self.texte("Tiens, je n'ai plus de Chamanyans... Où sont-ils ?",1)
            return 3
        elif evenement.type==pygame.KEYDOWN and evenement.key==pygame.K_SPACE and marche==3:
            return 4

    def scene2(self,evenement,marche):
        if evenement.type==pygame.KEYDOWN and evenement.key==pygame.K_SPACE and marche==False:
            self.texte("Ah ! Nyatacha ! C'est toi qui... !",1)
            self.ecran.blit(self.nyat,(300,10))
            return 1
        elif evenement.type==pygame.KEYDOWN and evenement.key==pygame.K_SPACE and marche==1:
            self.texte("*nom nom* Quoi ? Tu veux danser ?!",1)
            self.ecran.blit(self.nyat,(300,10))
            return 2
        elif evenement.type==pygame.KEYDOWN and evenement.key==pygame.K_SPACE and marche==2 :
            self.couleur=(90,202,215)
            self.texte("Nyatacha:",1)
            self.couleur=(255,255,255)
            self.texte("Appuie sur les flèches directionnelles lorsqu'elles",2)
            image_texte = self.font.render("passent sur la ligne rouge et dansons ensemble !",True,self.couleur)
            self.ecran.blit(image_texte,(30,470))
            self.ecran.blit(self.nyat,(300,10))
            return 3
        elif evenement.type==pygame.KEYDOWN and evenement.key==pygame.K_SPACE and marche==3:
            return 4

    def scene3(self,evenement , marche):
        if self.marche==4:
            self.couleur=(90,202,215)
            self.texte("Nyatacha:",1)
            self.couleur=(255,255,255)
            image_texte = self.font.render("Ah ! Tu m'as battue !",True,self.couleur)
            self.ecran.blit(image_texte,(30,450))
            self.ecran.blit(self.nyat,(300,10))
            self.marche = 0
        elif evenement.type==pygame.KEYDOWN and evenement.key==pygame.K_SPACE and self.marche==0:
            self.texte("Huff, huff... Bon, tu me rends mon paquet de Chamanyans ?",2)
            self.ecran.blit(self.nyat,(300,10))
            self.marche = 1
        elif evenement.type==pygame.KEYDOWN and evenement.key==pygame.K_SPACE and self.marche ==1:
            self.couleur=(90,202,215)
            self.texte("Nyatacha:",1)
            self.couleur=(255,255,255)
            image_texte = self.font.render("Tiens ! ",True,self.couleur)
            self.ecran.blit(image_texte,(30,450))
            self.ecran.blit(self.nyat,(300,10))
            self.marche = 2
        elif evenement.type==pygame.KEYDOWN and evenement.key==pygame.K_SPACE and self.marche ==2:
            self.texte("Mais il est vide ?!",1)
            self.ecran.blit(self.nyat,(300,10))
            self.marche = 3
        elif evenement.type==pygame.KEYDOWN and evenement.key==pygame.K_SPACE and self.marche ==3 :
            self.couleur=(90,202,215)
            self.texte("Nyatacha:",1)
            self.couleur=(255,255,255)
            image_texte = self.font.render("J'ai mis à jour le pc le plus à droite si tu  devrais aller voire ?",True,self.couleur)
            self.ecran.blit(image_texte,(30,450))
            self.ecran.blit(self.nyat,(300,10))
            self.marche = 6
        elif evenement.type==pygame.KEYDOWN and evenement.key==pygame.K_SPACE and self.marche==6:
            self.marche = 5

    def renyat(self,evenement,marche):
        if evenement.type==pygame.KEYDOWN and evenement.key==pygame.K_SPACE and self.marche == 10:
            self.marche = 11
        elif evenement.type==pygame.KEYDOWN and evenement.key==pygame.K_SPACE and self.marche==5:
            self.couleur=(90,202,215)
            self.texte("Nyatacha:",1)
            self.couleur=(255,255,255)
            image_texte = self.font.render("Vas-y ! Va voir l'ordinateur à tout droite !",True,self.couleur)
            self.ecran.blit(image_texte,(30,450))
            self.marche=10

    def fin(self,evenement , marche):
        if evenement.type==pygame.KEYDOWN and evenement.key==pygame.K_SPACE and self.marche==5 :
            image_texte = self.font.render("Programmation :",True,self.couleur)
            self.ecran.blit(image_texte,(10,100))
            image_texte = self.font.render("Cheffe de projet : Phuong Thao NGUYEN :",True,self.couleur)
            self.ecran.blit(image_texte,(40,130))
            image_texte = self.font.render("Développeur: Julien BONNAFE",True,self.couleur)
            self.ecran.blit(image_texte,(40,160))
            image_texte = self.font.render("Graphisme :",True,self.couleur)
            self.ecran.blit(image_texte,(10,200))
            image_texte = self.font.render("Concept Designer:  Garance BRIOIS",True,self.couleur)
            self.ecran.blit(image_texte,(40,230))
            image_texte = self.font.render("Co-Illustratrice: Phuong Thao NGUYEN",True,self.couleur)
            self.ecran.blit(image_texte,(40,260))
            image_texte = self.font.render("Sound Designer : ",True,self.couleur)
            self.ecran.blit(image_texte,(10,310))
            image_texte = self.font.render("Julien BONNAFE (désolé pour vos oreilles)",True,self.couleur)
            self.ecran.blit(image_texte,(40,340))
            image_texte = self.font.render("Scénaristes :",True,self.couleur)
            self.ecran.blit(image_texte,(10,390))
            image_texte = self.font.render("Phuong Thao NGUYEN",True,self.couleur)
            self.ecran.blit(image_texte,(40,420))
            image_texte = self.font.render("David CAGE n'a pas travaillé sur ce projet.",True,self.couleur)
            self.ecran.blit(image_texte,(40,450))
            image_texte = self.font.render("Crédits: ComicDabCorporation",True,self.couleur)
            self.ecran.blit(image_texte,(200,40))
            image_texte = self.font.render("Pressez une dernière fois espace.",True,self.couleur)
            self.ecran.blit(image_texte,(200,550))
            return 50
        elif evenement.type==pygame.KEYDOWN and evenement.key==pygame.K_SPACE and marche==50 :
            return 1000

    def finfini(self,evenement , marche):
        if evenement.type==pygame.KEYDOWN and evenement.key==pygame.K_SPACE:
             self.font = pygame.font.SysFont('Comic Sans Ms',60)
             image_texte = self.font.render("FIN DE LA DEMO",True,self.couleur)
             self.ecran.blit(image_texte,(120,170))
             self.font = pygame.font.SysFont('Comic Sans Ms',20)
             image_texte = self.font.render("Remerciements :",True,self.couleur)
             self.ecran.blit(image_texte,(60,270))
             image_texte = self.font.render("On vous remercie pour cette incroyable année.",True,self.couleur)
             self.ecran.blit(image_texte,(80,300))
             image_texte = self.font.render("Vous nous avez beaucoup apporté, au plaisir de vous revoir un jour.",True,self.couleur)
             self.ecran.blit(image_texte,(80,330))
             self.font = pygame.font.SysFont('Comic Sans Ms',10)
             image_texte = self.font.render("Avouez, c'était mieux que Assassin's Creed.",True,self.couleur)
             self.ecran.blit(image_texte,(80,450))
             return 1000

