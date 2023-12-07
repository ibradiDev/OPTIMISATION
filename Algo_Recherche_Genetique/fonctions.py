import pprint
import random


def initialiser_population(nbre_individus: int, nbre_reines: int = 8) -> list:
    """Génère de façon aléatoire une solution de base comme solution optimale"""
    population = []
    for _ in range(nbre_individus):
        individu = random.sample(range(1, nbre_reines + 1), nbre_reines)
        population.append(individu)
    return population


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


def mutation(individu: list) -> list:
    genes = random.sample(individu, 2)
    index_gene_1, gene_1 = individu.index(genes[0]), genes[0]
    index_gene_2, gene_2 = individu.index(genes[1]), genes[1]

    individu[index_gene_1], individu[index_gene_2] = gene_2, gene_1
    return individu


def croisement(parents: list) -> list:
    enfants = []
    for i in range(0, len(parents), 2):
        parent_1, parent_2 = parents[i], parents[i + 1]
        enfant1 = parent_1[:4] + parent_2[4:]
        enfant2 = parent_1[4:] + parent_2[:4]
        enfants.extend([enfant1, enfant2])

    return enfants


def selection_des_meilleurs(population: list, nbre_de_selection: int):
    # grandes_liste = population.copy()
    meilleurs = []
    for _ in range(len(population)):
        tournament = random.sample(population, 3)
        meilleur = min(tournament, key=lambda x: conflits(x))
        meilleurs.append(meilleur)

    return meilleurs[nbre_de_selection:]


def meilleur_parent(parents: list) -> list:
    """Retourne le meilleur des voisins"""
    return min(parents, key=lambda x: conflits(x))


def meilleur_des_individus(population: list) -> list:
    """Retourne le meilleur des individus"""
    return min(population, key=lambda x: conflits(x))


def factoriel(k):
    if k <= 0:
        return 1
    return k * factoriel(k - 1)


def c_n_k(n, k):
    return factoriel(n) / (factoriel(k) * factoriel((n - k)))
