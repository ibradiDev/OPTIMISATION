from pprint import pprint
from fonctions import *


if __name__ == "__main__":
    taille_population = 100
    population = initialiser_population(taille_population)
    proba_de_mutation = 0.6
    iteration = 0

    print(f"\tPopulation initiale: ")
    pprint.pprint(population)

    while True:
        iteration += 1
        # parents = population
        enfants = croisement(population)

        population.extend(enfants)

        for i in range(len(population)):
            r = random.uniform(0, 1)
            if r > proba_de_mutation:
                individu_mute = mutation(population[i])
                population[i] = individu_mute

        meilleurs_individus = selection_des_meilleurs(population, taille_population)
        meilleur_des_meilleurs = meilleur_des_individus(meilleurs_individus)

        if conflits(meilleur_des_meilleurs) == 0:
            print(
                "\n******************************************************************************"
            )
            print(
                f"\t     Solution optimale trouvée:  {meilleur_des_meilleurs}  ==>  Conflits = {conflits(meilleur_des_meilleurs)}"
            )
            print(f"\tNombre d'itérations effectuées:  {iteration}")
            print(
                "******************************************************************************\n"
            )
            break
        else:
            population = meilleurs_individus
            print(
                f"\nObjectif pas encore atteint!, itérations effectuées : {iteration}"
            )
            print(
                f"\tMeilleur de la population actuelle:  {meilleur_des_meilleurs}  ==>  Conflits = {conflits(meilleur_des_meilleurs)}"
            )
