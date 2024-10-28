"""Écris un programme qui affiche tous les nombres de 1 à 50. Pour les multiples de 3, affiche "Fizz", et pour les multiples de 5, affiche "Buzz". Pour les multiples de 3 et 5, affiche "FizzBuzz"."""
# Résultat de l'exo
for nombre in range(1, 51) :
    if nombre % 3 == 0 and nombre % 5 == 0 :
        print('FIZZBUZZ')
    elif nombre % 3 == 0 :
        print('FIZZ')
    elif nombre % 5 == 0 :
        print('BUZZ')
    else : 
        print('Damnit')

""" Écris une fonction inverse_liste qui prend une liste en entrée et retourne la liste inversée."""
# Résultat de l'exo
def inverse_liste(liste):
    """Retourne la liste inversée."""
    return liste[::-1]
# Exemple d'utilisation
ma_liste = [1, 2, 3, 4, 5]
print(inverse_liste(ma_liste))  # Affiche [5, 4, 3, 2, 1]

"""Crée une fonction somme_liste qui prend une liste de nombres et retourne la somme des éléments de la liste."""
# Résultat de l'exo
def somme_liste(list):
    return sum(list)

"""Écris une fonction est_palindrome qui vérifie si une chaîne de caractères est un palindrome (se lit de la même façon dans les deux sens).
"""
# Résultat de l'exo
def est_palindrome(chaine):
    """Vérifie si une chaîne de caractères est un palindrome."""
    chaine = chaine.replace(" ", "").lower()  # Supprime les espaces et met en minuscules
    return chaine == chaine[::-1]

# Exemple d'utilisation
print(est_palindrome("Eve"))  # Affiche True
print(est_palindrome("Bonjour"))  # Affiche False


"""
Crée une fonction longueur_mots qui prend une phrase et retourne une liste contenant la longueur de chaque mot de la phrase."""