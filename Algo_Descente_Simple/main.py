from fonctions import *


if __name__ == "__main__":
    # Choix d'une solution s aléatoire et ses voisines s1, s2, s3
    s = solution_initiale()
    s1, s2, s3 = voisinage(s)

    print(f"\nSolution initiale s = {s}\tConflits = {conflits(s)}")

    while True:
        print(f"\t Solution voisine s1 = {s1}\tConflits = {conflits(s1)}")
        print(f"\t Solution voisine s2 = {s2}\tConflits = {conflits(s2)}")
        print(f"\t Solution voisine s3 = {s3}\tConflits = {conflits(s3)}")

        if (
            conflits(s1) < conflits(s)
            and conflits(s1) <= conflits(s2)
            and conflits(s1) <= conflits(s3)
        ):
            s = s1
            s1, s2, s3 = voisinage(s)

        elif (
            conflits(s2) < conflits(s)
            and conflits(s2) <= conflits(s1)
            and conflits(s2) <= conflits(s3)
        ):
            s = s2
            s1, s2, s3 = voisinage(s)

        elif (
            conflits(s3) < conflits(s)
            and conflits(s3) <= conflits(s1)
            and conflits(s3) <= conflits(s2)
        ):
            s = s3
            s1, s2, s3 = voisinage(s)
        else:
            print(
                "\n************************************************************************"
            )
            print(f"\tSolution optimale s = {s}\tConflits = {conflits(s)}")
            print(
                "************************************************************************\n"
            )
            break  # Mettre fin au le programme

        print(f"\nNouvelle solution optimale s = {s}\tConflits = {conflits(s)}")
