import time
import math

taille = float(input("Votre taille (en cm) ?\n"))
taille = taille / 100
poids = float(input("Votre poids (en kg) ?\n"))
age = float(input("Votre âge (ans) ?\n"))

genre = ""

while (genre == "") :

    choixGenre = (str(input("\nEntrez :\n    -H si vous êtes un homme\n    -F si vous êtes une femme :  "))).upper()

    time.sleep(1)

    if choixGenre == "H" :
        genre = 1
    
    elif choixGenre == "F" :
        genre = 2


metabolismeBase = float(0)
niveauActivitePhysique = float(0)
resultat = float(0)

while (niveauActivitePhysique == 0) :

    choixActivitePhysique = int(input("\n\nEntrez : \n    - 1 si vous bougez peu \n    - 2 si vous êtes régulier \n    - 3 si vous êtes sportif \n    - 4 si vous êtes un grand sportif :  "))

    time.sleep(1)
    
    if choixActivitePhysique == 1 :

        niveauActivitePhysique = 1.2


    elif choixActivitePhysique == 2 :

        niveauActivitePhysique = 1.375


    elif choixActivitePhysique == 3 :

        niveauActivitePhysique = 1.55


    elif choixActivitePhysique == 4 :

        niveauActivitePhysique = 1.725



    
"""
metabolismeBase = 0.276 + 0.0573 * poids + 2.073 * taille - 0.0285 * age
metabolismeBase = float(metabolismeBase)


resultat = (niveauActivitePhysique * metabolismeBase * 0.239) * 1000
"""

if genre == 1 :

    resultat = 665 + (13.75 * poids) + (5 * taille) - (6.77 * age)
    resultat *= niveauActivitePhysique
    resultat = math.ceil(resultat)

elif genre == 2 :

    resultat = 655 + (9.56 * poids) + (1.85 * taille) - (4.67 * age)
    resultat *= niveauActivitePhysique
    resultat = math.ceil(resultat)

print("\n Votre besoin calorique correspond à  : ", resultat , " kcal \n")


glucides = math.ceil(resultat / 22.8)
proteines = math.ceil(resultat / 12.3)
lipides = math.ceil(resultat / 25.7)

print("     La quantité de glucides qu'il vous faut est : " , glucides, "g." )
print("     La quantité de protéines qu'il vous faut est : ", proteines, "g.")
print("     La quantité de lipides qu'il vous faut est : ", lipides, "g.")

print("\n\n Nous vous suggérons quelques repas-types sur une journée :  ")
time.sleep(1)
print("\nPetit déjeûner :   Smoothie bowl aux fruits rouges : \n\n  -Calories : 363 kcal \n  -Lipides : 10g \n  -Protéines 26g \n  -Glucides : 30g")
time.sleep(1)
print("\nDéjeûner :   Gratin de riz et de courgettes rapées : \n\n  -Calories : 386 kcal \n  -Lipides : 15,3g \n  -Protéines 11,5g \n  -Glucides : 34,4g")
time.sleep(1)
print("\nGoûter :   Une part de clafoutis maison : \n\n  -Calories : 123 kcal \n  -Lipides : 3g \n  -Protéines 6g \n  -Glucides : 29g")
time.sleep(1)
print("\nDîner :   Salade de courgettes et nectarines : \n\n  -Calories : 437 kcal \n  -Lipides : 31g \n  -Protéines 13g \n  -Glucides : 32g")

time.sleep(15)