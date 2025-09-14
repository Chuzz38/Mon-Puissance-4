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
    """
    Le joueur 1 ou 2 a choisi la colonne col dans laquelle il a joué et renvoie 
    True si le coup est bien possible et False sinon (dans le cas où la colonne)
    est complète
    """
    for ligne in reversed(plateau):
        if ligne[col] == 0:
            ligne[col] = joueur
            return True
    return False
    

def ligne_coup(plateau, col):
    # Fonction qui renvoie la ligne en fonction de la colonne qui vient d'être jouée
    for i, ligne in enumerate(plateau):
        if ligne[col] != 0:
            return i


def est_gagnant(plateau, col, joueur):
    """
    Fonction qui renvoie le gagnant s'il y en a un avec le dernier coup il faut regarder
    horizontalement, verticalement et sur les diagonales.
    Fonction qui pourra sûrement être amélioré et rendu plus efficace/optimisé
    """
    total_joueur = 1
    ligne = ligne_coup(plateau, col)
    
    # On commence par tester horizontalement
    for i in range(1, 4):
        if (col+i) < 7 and plateau[ligne][col+i] == joueur :
            total_joueur += 1
        else:
            break
    for i in range(1, 4):
        if 0 <= (col-i) and plateau[ligne][col-i] == joueur:
            total_joueur += 1
        else:
            break
    if total_joueur >= 4:
        return True
    
    total_joueur = 1
    # On continue verticalement
    for i in range(1, 4):
        if (ligne+i) < 6 and plateau[ligne+i][col] == joueur:
            total_joueur += 1
        else:
            break
    
    for i in range(1, 4):
        if 0 <= (ligne-i) and plateau[ligne-i][col] == joueur:
            total_joueur += 1
        else:
            break
    if total_joueur >= 4:
        return True

    total_joueur = 1
    # On continue diagonale bas gauche - haut droit
    for i in range(1, 4):
        if 0 <= (col-i) and (ligne+i) < 6 and plateau[ligne+i][col-i] == joueur:
            total_joueur += 1
        else:
            break
    
    for i in range(1, 4):
        if 0 <= (ligne-i) and (col+i) < 7 and plateau[ligne-i][col+i] == joueur:
            total_joueur += 1
        else:
            break
    if total_joueur >= 4:
        return True

    total_joueur = 1
    # On continue diagonale bas droit - haut gauche
    for i in range(1, 4):
        if 0 <= (ligne-i) and 0 <= (col-i) and plateau[ligne-i][col-i] == joueur:
            total_joueur += 1
        else:
            break

    for i in range(1, 4):
        if (ligne+i) < 6 and (col+i) < 7 and plateau[ligne+i][col+i] == joueur:
            total_joueur += 1
        else:
            break
    if total_joueur >= 4:
        return True

    return False

# def main():
#     # Faire quelque chose pour demander si les joueurs veulent bien donner leur prénom
#     # Peut-être faire un bot avec lequel on peut jouer contre (plusieurs niveaux ?)

#     nb_coup = 0
#     joueur = 2
#     un_gagnant = False
#     col_est_correcte = True
#     plateau_jeu = initialiser_plateau()
#     while not un_gagnant:
#         # On change le joueur qui doit jouer
#         if joueur == 1:
#             joueur = 2
#         else:
#             joueur = 1
            
#         print("Voici le plateau de jeu :")
#         afficher_plateau(plateau_jeu)
#         col = input(f"Joueur {joueur}, choisissez la colonne entre 1 et 7 : ")
#         col_est_correcte = col_correcte(col)
#         while not col_est_correcte:
#             col = input(f"Joueur {joueur}, choisissez la colonne entre 1 et 7 : ")
#             col_est_correcte = col_correcte(col)

#         joue_coup(plateau_jeu, int(col)-1, joueur)
#         un_gagnant = est_gagnant(plateau_jeu, int(col)-1, joueur)
        
#         # On vérifie qu'on n'a pas rempli toute la grille
#         nb_coup += 1
#         if nb_coup == 42:
#             break
    
#     afficher_plateau(plateau_jeu)
#     if nb_coup == 42:
#         print("Bravo aux deux joueurs ! Egalité parfaite !")
#     elif joueur == 1:
#         print("Bravo joueur 1, tu as gagné !")
#     else:
#         print("Bravo joueur 2, tu as gagné !")

# main()
