import pygame
import depart

# pygame setup
pygame.init()
screen = pygame.display.set_mode((699, 600))
pygame.display.set_caption("My game")
image = pygame.image.load("grille2.png").convert_alpha()
pion_jaune = pygame.image.load("jaune.png").convert_alpha()
pion_rouge = pygame.image.load("rouge-bg.png").convert_alpha()
clock = pygame.time.Clock()

running = True
pressed = False

joueur = 1
egalite = False
a_un_gagnant = False
bon_coup = True
nb_coups = 0
plateau_jeu = depart.initialiser_plateau()

def afficher(plateau):
    for lig in range(6):
        for col in range(7):
            if plateau[lig][col] == 0:
                continue
            elif plateau[lig][col] == 1:
                screen.blit(pion_jaune, (col*100 + 5, lig*100 + 5))
            else:
                screen.blit(pion_rouge, (col*100 + 5, lig*100 + 5))

while running:
    screen.blit(image, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # RENDER YOUR GAME HERE
    if not pressed and pygame.mouse.get_pressed()[0] and not a_un_gagnant and not egalite:
        pressed = True
        pos = pygame.mouse.get_pos()
        col = pos[0]//100
        
    if pressed and not pygame.mouse.get_pressed()[0]:
        pressed = False
        bon_coup = depart.joue_coup(plateau_jeu, col, joueur)
        
        if bon_coup:
            nb_coups += 1
            if nb_coups == 42:
                egalite = True
            
            if depart.est_gagnant(plateau_jeu, col, joueur):
                a_un_gagnant = True
                if joueur == 1:
                    print("#######################")
                    print("# Bravo au joueur 1 ! #")
                    print("#######################")
                else:
                    print("#######################")
                    print("# Bravo au joueur 2 ! #")
                    print("#######################")
        
            if joueur == 1:
                joueur = 2
            else:
                joueur = 1
        
    
    afficher(plateau_jeu)
        
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()