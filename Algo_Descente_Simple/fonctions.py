import random


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


def voisinage(solution: list):
    """Génère des solutions voisines à la solution optimale actuelle"""

    s1, s2, s3 = solution.copy(), solution.copy(), solution.copy()
    # Choisir des reines de façon aléatoire et définir leurs nouvelles positions
    r1, r11, nouvelle_pos_r1, nouvelle_pos_r11 = (
        random.randint(0, len(solution) - 1),
        random.randint(1, len(solution) - 1),
        random.randint(1, len(solution) - 1),
        random.randint(1, len(solution) - 1),
    )
    r2, r22, nouvelle_pos_r2, nouvelle_pos_r22 = (
        random.randint(0, len(solution) - 1),
        random.randint(1, len(solution) - 1),
        random.randint(1, len(solution) - 1),
        random.randint(1, len(solution) - 1),
    )
    r3, r33, nouvelle_pos_r3, nouvelle_pos_r33 = (
        random.randint(0, len(solution) - 1),
        random.randint(1, len(solution) - 1),
        random.randint(1, len(solution) - 1),
        random.randint(1, len(solution) - 1),
    )
    # Déplacer les reines choisi aux nouvelles positions
    s1[r1], s1[r11], s2[r2], s2[r22], s3[r3], s3[r33] = (
        nouvelle_pos_r1,
        nouvelle_pos_r11,
        nouvelle_pos_r2,
        nouvelle_pos_r22,
        nouvelle_pos_r3,
        nouvelle_pos_r33,
    )

    return s1, s2, s3
