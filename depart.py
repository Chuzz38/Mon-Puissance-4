# plateau = tableau de taille 6 lignes et 7 colonnes

def initialiser_plateau():
    # Initialise le plateau de jeu de 7 colonnes et de 6 lignes
    plateau = []
    for i in range(6):
        ligne = [0, 0, 0, 0, 0, 0, i]
        plateau.append(ligne)
    return plateau
            

def afficher_plateau(plateau):
    print(" -----------------------------")
    for x in range(6):
        for y in range(7):
            print(" |", plateau[x][y], end="")
        print(" |")
        print(" -----------------------------")
    print("   1   2   3   4   5   6   7")

def joue_coup(plateau, col, joueur):
    # Le joueur 1 ou 2 choisi la colonne dans laquelle il joue
    for ligne in reversed(plateau):
        if ligne[col-1] == 0:
            ligne[col-1] = joueur
            return

def un_gagnant(plateau_jeu, col):
    # Fonction qui renvoie le gagnant s'il y en a un avec le dernier coup
    
    # Si la dernière case a été atteinte et qu'il n'y a pas eu de gagnant dire qu'il y a eu égalité
    pass
    
def main():
    plateau_jeu = initialiser_plateau()
    afficher_plateau(plateau_jeu)

main()