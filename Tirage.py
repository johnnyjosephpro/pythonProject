import random

nombre_aleatoire = random.randint(1, 1000)

print(nombre_aleatoire)
premier_essai = input("Entrer un nombre aleatoire:")
resultat = premier_essai == nombre_aleatoire

if (resultat==False):
    premier_essai = input("Entrer un nombre aleatoire a nouveau:")
else :
    print("Vous avez gagner!")
