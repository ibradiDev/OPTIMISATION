import random
from math import exp


def solution_initiale(nbre_reines: int = 8) -> list:
    """Génère de façon aléatoire une solution de base comme solution optimale"""
    return [random.randint(1, nbre_reines) for _ in range(nbre_reines)]


def conflits(solution: list) -> int:
    """Retourne le nombre de conflits générés par une solution"""
    conflits = 0
    for i in range(len(solution)):
        for j in range(len(solution)):
            # Si des reines se trouvent dans la même colonne ou sur la même diagonale
            if i != j:
                if (solution[i] == solution[j]) or (
                    abs(solution[i] - solution[j]) == abs(i - j)
                ):
                    conflits += 1
    return conflits


def voisinage(solution: list, nombre_de_voisins: int = 3) -> list:
    """Génère un nombre de solutions voisines à la solution optimale actuelle"""
    voisins = []
    for _ in range(nombre_de_voisins):
        voisin = solution.copy()
        # Choisir et Déplacer façon aléatoire trois de mes reines
        r1, r2, r3, nouvelle_pos_r1, nouvelle_pos_r2, nouvelle_pos_r3 = (
            random.randint(0, len(solution) - 1),
            random.randint(0, len(solution) - 1),
            random.randint(0, len(solution) - 1),
            random.randint(1, len(solution)),
            random.randint(1, len(solution)),
            random.randint(1, len(solution)),
        )
        voisin[r1], voisin[r2], voisin[r3] = (
            nouvelle_pos_r1,
            nouvelle_pos_r2,
            nouvelle_pos_r3,
        )

        voisins.append(voisin)
    # Retourner le/les voisins généré(s)
    if nombre_de_voisins == 1:
        return voisins[0]
    return voisins


def meilleur_des_voisins(voisins: list) -> list:
    """Retourne le meilleur des voisins"""
    return min(voisins, key=lambda x: conflits(x))


def proba_metropolis(t, s, s1) -> float:
    """
    Calcule la probabilité selon le principe de Métroplis.

    Args:
        t (int): Température
        s (list): Solution optimale concidérée
        s1 (list): Solution voisine à s
    Returns:
        float: la valeur de la probabilité calculée
    """
    return exp((conflits(s) - conflits(s1)) / t)
