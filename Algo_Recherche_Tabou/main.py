import random
from pprint import pprint

from fonctions import *

if __name__ == "__main__":
    s_initiale = solution_initiale()
    s_actuelle = s_initiale
    k = 0
    liste_tabou = []
    etat_persistant = 0

    print(
        f"     \nSolution initiale: s = {s_initiale}  ==>  Conflits = {conflits(s_initiale)}\n"
    )

    while True:
        k += 1
        voisins = voisinage(s_actuelle, 50)
        voisins_admissibles = []
        for voisin in voisins:
            if voisin not in liste_tabou:
                voisins_admissibles.append(voisin)

        meilleur_voisin = meilleur_des_voisins(voisins_admissibles)

        if conflits(meilleur_voisin) < conflits(s_actuelle):
            if len(liste_tabou) >= 6:
                liste_tabou.pop(0)

            liste_tabou.append(meilleur_voisin)
            s_actuelle = meilleur_voisin
            print(
                f"\t  Meilleur voisin autorisé = {meilleur_voisin}  ==>  Conflits = {conflits(meilleur_voisin)}"
            )
            print(
                f"\t  Nouvelle solution optimale = {meilleur_voisin}  ==>  Conflits = {conflits(meilleur_voisin)}\n"
            )
a = random.sample
            print(f"Liste tabou: ")
            pprint(liste_tabou)
            print(f"\n")

        else:
            etat_persistant += 1
            print(f"\n\t\t****************PERSISTANCE****************")
            print(f"Nombre d'itérations effectuées:  {k}")
            print(
                f"Solution optimale inchangée:  s = {s_actuelle}  ==>  Conflits = {conflits(s_actuelle)}"
            )
            print(f"Nombre de persistance : {etat_persistant}\n")

            if etat_persistant == 200:
                print(
                    "\n******************************************************************************"
                )
                print(
                    f"\t     Solution optimale trouvée:  s = {s_actuelle}  ==>  Conflits = {conflits(s_actuelle)}"
                )
                print(f"\tNombre d'itérations effectuées:  {k}")

                print(
                    f"\t\t  Solution persistante:  {s_actuelle}   ==>  Conflits = {conflits(s_actuelle)}"
                )
                print(
                    "******************************************************************************\n"
                )
                break

        if conflits(s_actuelle) == 0:
            print(
                "\n******************************************************************************"
            )
            print(
                f"\t     Solution optimale trouvée:  {s_actuelle}  ==>  Conflits = {conflits(s_actuelle)}"
            )
            print(f"\tNombre d'itérations effectuées:  {k}")
            print(
                "******************************************************************************\n"
            )
            break

        elif k == 1000:
            print(
                "\n******************************************************************************"
            )
            print(
                f"\t     Solution optimale trouvée:  s = {s_actuelle}  ==>  Conflits = {conflits(s_actuelle)}"
            )
            print(f"\tNombre d'itérations effectuées:  {k}")
            print(
                "******************************************************************************\n"
            )
            break
