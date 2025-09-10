# Implémentation du jeu du puissance 4 en python (non orienté objet)

def initialiser_plateau():
    # Initialise le plateau de jeu de 7 colonnes et de 6 lignes
    plateau = []
    for _ in range(6):
        ligne = [0, 0, 0, 0, 0, 0, 0]
        plateau.append(ligne)
    return plateau
            

def afficher_plateau(plateau):
    print(" -----------------------------")
    for x in range(6):
        for y in range(7):
            if plateau[x][y] == 0:
                carac = "."
            elif plateau[x][y] == 1:
                carac = "●"
            else:
                carac = "○"
            print(" |", carac, end="")
        print(" |")
        print(" -----------------------------")
    print("   1   2   3   4   5   6   7")

def joue_coup(plateau, col, joueur):
    # Le joueur 1 ou 2 choisi la colonne dans laquelle il joue
    for ligne in reversed(plateau):
        if ligne[col-1] == 0:
            ligne[col-1] = joueur
            return

def col_correcte(col):
    if "1" <= col <= "7"
        return True
    else:
        return False

def un_gagnant(plateau_jeu, col):
    # Fonction qui renvoie le gagnant s'il y en a un avec le dernier coup
    # Si la dernière case a été atteinte et qu'il n'y a pas eu de gagnant dire qu'il y a eu égalité
    # le tableau contient soit des 0, des 1 ou des 2
    return True

def main():
    # Faire quelque chose pour demander si les joueurs veulent bien donner leur prénom
    # Peut-être faire un bot avec lequel on peut jouer contre (plusieurs niveaux ?)

    joueur = 1
    partie_en_cours = True
    plateau_jeu = initialiser_plateau()
    col_est_correcte = True
    while partie_en_cours:
        print("Voici le plateau de jeu :")
        afficher_plateau(plateau_jeu)
        col = input(f"Joueur {joueur}, choisissez la colonne entre 1 et 7 : ")
        col_est_correcte = col_correcte(col)
        while not col_est_correcte:
            col = input(f"Joueur {joueur}, choisissez la colonne entre 1 et 7 : ")
            col_est_correcte = col_correcte(col)
        # Faire quelque chose pour vérifier la validité de col

        joue_coup(plateau_jeu, col, joueur)
        
        # On change le joueur qui doit jouer
        if joueur == 1:
            joueur = 2
        else:
            joueur = 1

main()
