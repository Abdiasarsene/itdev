"""Premier exercice"""
class Animal : 
    def parle(self):
        return("Ces animaux chantent")

# Création du premier enfant
class Chien(Animal):
    def parle(self):
        return("Ce chien aboie")

# Création du deuxième enfant
class Chat(Animal):
    def parle(self):
        return("Ce chat miaule")

"""Deuxième exercice"""
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
    
    def affiche_info(self):
        print("Je m\'appelle", self.nom, "et j\'ai ", self.age)

# Création de l'enfant 
class Etudiant(Personne):
    def __init__(self,nom, age, domaine_etude):
        super().__init__(nom, age)
        self.domaine_etude = domaine_etude
    
    def affiche_info(self):
        return super().affiche_info()


"""Troisième exercice"""
class Forme :
    def aire(self):
        return 0

# Création de la sous-classe "Carre"
class Carre(Forme) :
    def __init__(self, cote):
        self.cote = cote
    
    def aire(self):
        return self.cote**2


class Cercle(Forme) :
    def __init__(self,rayon):
        self.rayon = rayon
    
    def aire(self):
        return 3.14*self.rayon**2

class Oiseau :
    def voler(self):
        return("L'oiseau est dans le ciel")

class Avion :
    def voler(self):
        return ("L'avion vole dans les airs")

class HommeVolant(Oiseau, Avion) :
    def voler(self):
        return

"""Exercice 2 : Utiliser `super()` avec héritage multiple
Crée une classe `AppareilElectronique` avec un constructeur qui prend le nom de l'appareil en paramètre et affiche "Appareil activé : nom". Crée une deuxième classe `Smartphone` avec un constructeur qui affiche "Smartphone activé". Ensuite, crée une classe `AppareilConnecté` qui hérite de `AppareilElectronique` et `Smartphone`. Utilise `super()` pour appeler les constructeurs des deux classes parentes dans la bonne séquence.

**Objectif :** Comprendre comment utiliser `super()` dans un contexte d'héritage multiple.
"""
class  AppareilElectronique :
    def __init__(self, nom):
        print(f"Appareil electronique : {nom}")

class Smartphone :
    def __init__(self):
        print("Smartphone activé")

class AppareilConnecte (AppareilElectronique, Smartphone):
    def __init__(self, nom):
        super().__init__(self, nom)
        Smartphone.__init__(self)
        print('Appareil connecté activé')

"""Explication :
La classe AppareilConnectéhérite à la fois de AppareilElectroniqueet Smartphone.
Le constructeur de AppareilElectroniqueest appelé via super(), qui convient à l'ordre de résolution des méthodes (MRO).
Pour appeler également le constructeur de Smartphone, nous utilisons Smartphone.__init__(self)manuellement après l'appel de super(). Cela est nécessaire car super()dans un héritage multiple appelle uniquement la méthode de la première classe dans l'ordre de l'héritage."""



"""Exercice 3 : Gestion des collisions de méthodes
Crée une classe `Vehicule` avec une méthode `demarrer()` qui affiche "Le véhicule démarre". Crée une classe `Voiture` qui hérite de `Vehicule` et redéfinit la méthode `demarrer()` en affichant "La voiture démarre". Crée une classe `Moto` qui hérite également de `Vehicule` et redéfinit la méthode `demarrer()` en affichant "La moto démarre". Ensuite, crée une classe `VehiculeAmphibie` qui hérite à la fois de `Voiture` et `Moto`, et essaye d'appeler la méthode `demarrer()`.

**Objectif :** Apprendre à résoudre les conflits de méthode dans un cas d'héritage en diamant et à utiliser l'ordre de résolution des méthodes (MRO).
"""
class Vehicule : 
    def demarrer(self):
        print("Le vehicul démarre")

class voiture(Vehicule) :
    def demarrer(self):
        print("La voiture démarfre")

class Moto(Vehicule) :
    def demarrer(self):
        print("La moto démarre")

class VehiculeAmphibie(voiture, Moto):
    def demarrer(self):
        super().demarrer
        return Moto.demarrer


"""Explication :
La classe Vehiculecontient une méthode demarrer()qui affiche "Le véhicule démarre".
Les classes Voitureet Motohéritent de Vehiculeet redéfinissent la méthode demarrer().
La classe VehiculeAmphibiehérite à la fois de Voitureet Moto. Dans ce cas, lorsque vous appelez la méthode demarrer(), Python doit choisir laquelle des deux versions (celle de Voitureou celle de Moto) exécuter.
En Python, l'ordre de résolution des méthodes (MRO) détermine quelle méthode est appelée dans un cas d'héritage multiple. L'ordre est influencé par l'ordre dans lequel les classes parentes sont mentionnées dans la définition de la classe dérivée."""



"""Exercice 4 : Interface commune avec héritage multiple
Crée une classe `Forme2D` avec une méthode `aire()` qui renvoie `NotImplementedError`. Crée ensuite deux sous-classes : `Rectangle` et `Cercle`. `Rectangle` doit avoir des attributs `largeur` et `longueur`, et `Cercle` doit avoir un attribut `rayon`. Implémente la méthode `aire()` dans chaque classe pour calculer l'aire des formes correspondantes. Enfin, crée une classe `Objet3D` qui hérite de `Rectangle` et `Cercle`, et ajoute un attribut `hauteur`. Implémente une méthode `volume()` qui utilise la méthode `aire()` pour calculer le volume de l'objet.

**Objectif :** Combiner l'héritage multiple avec l'implémentation de méthodes partagées dans plusieurs classes et calculer des propriétés complexes.
"""

class Forme2D :
    def aire(self):
        return 'NotImplementedErro'

class Rectangle (Forme2D):
    largeur = 30
    longueur = 50
    def aire(self):
        return self.largeur*self.hauteur

class Cercle(Forme2D) :
    rayon =20
    def aire(self):
        return 3.14*self.rayon

class Objet3D (Rectangle, Cercle) :
    hauteur = 45
    def aire(self):
        return self.hauteur.aire()



"""Exercice 3 : Polymorphisme avec héritage
Crée une classe Formeavec une méthode aire()qui renvoie 0. Crée ensuite deux sous-classes, Carreet Cercle, qui héritent de Forme. Chaque sous-classe doit redéfinir la méthode aire()pour calculer l'aire du carré ou du cercle, en fonction des attributs coteou rayon."""

"""Résultat"""
class Forme : 
    def aire(self):
        return 0

class Carre(Forme) :
    def __ini__(self, cote):
        self.cote =cote
    def aire(self):
        return self.cote**2

class Cercle(Forme):
    def __init__(self, rayon):
        self.rayon = rayon
    def aire(self):
        return 3.14*self.rayon**2



"""Exercice 5 : Système de paiement avec héritage multiple
Crée une classe `Paiement` avec une méthode `effectuer_paiement()` qui affiche "Paiement effectué". Crée une classe `CarteBancaire` avec une méthode `debit()` qui affiche "Débit sur carte bancaire". Crée une classe `Cheque` avec une méthode `debit()` qui affiche "Débit sur compte via chèque". Crée une classe `Transaction` qui hérite de `Paiement`, `CarteBancaire` et `Cheque`. Implémente la méthode `debit()` dans la classe `Transaction` pour qu'elle choisisse si elle doit appeler la méthode `debit()` de `CarteBancaire` ou de `Cheque` en fonction du mode de paiement choisi.

**Objectif :** Gérer la surcharge de méthodes dans un cas d'héritage multiple où différentes implémentations de méthodes sont possibles selon des critères spécifiques.
"""

class Paiement:
    def effectuer_paiement(self):
        print('Paiement effectué')

class CarteBancaire :
    def debit(self):
        print("Débit sur carte bancaire")

class Cheque :
    def debit(self):
        print("Débit sur compte via chèque")

class Transaction (Paiement, CarteBancaire, Cheque):
    def debit(self):
        pass

