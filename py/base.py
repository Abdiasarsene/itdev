"""Écris une boucle for qui affiche les nombres de 1 à 10"""

for nombre in range(1,11) :
    print(nombre)

"""Utilise une boucle while pour afficher les nombres pairs de 2 à 20."""

i = 2
while i <=20 :
    print(i)
    i+=2

"""Écris un programme qui demande à l'utilisateur de saisir un nombre et affiche si ce nombre est positif, négatif ou nul."""
# Demander à l'utilisateur de saisir un nombre
nombre = float(input("Saisissez un nombre : "))

# Vérifier si le nombre est positif, négatif ou nul
if nombre > 0:
    print("Le nombre est positif.")
elif nombre < 0:
    print("Le nombre est négatif.")
else:
    print("Le nombre est nul.")

"""Crée un programme qui demande à l'utilisateur son âge et affiche "Enfant" si l'âge est inférieur à 12 ans, "Adolescent" entre 12 et 18 ans, et "Adulte" au-delà de 18 ans."""
age = float(input('Quel est votre âge'))
if age < 12 :
    print("Enfant")
elif 12 <= age <12 :
    print('Adolescent')
else :
    print("Adulte")