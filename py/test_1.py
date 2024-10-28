class Rectangle:
    width = 5
    heiht = 2
    
    def class_area(self):
        return self.width * self.heiht

class Rectangle : 
    
    def __init__(self, length, width, color = 'red'):
        self.length = length
        self.width = width
        self.color = color
    
    def squared(self, length, width):
        print(length*width)

rectangle =Rectangle(10,3)
squared_rectangle = rectangle.squared
squared_rectangle

class InfoTito: 
    '''Définition d'une classe'''

    def __init__(self, nom, prenom, classe, moyenne_annuelle, note_math=None):
        self.nom = nom
        self.prenom = prenom
        self.classe = classe
        self.moyenne_annuelle = moyenne_annuelle
        self.note_math = note_math

# Instanciation de la classe avec des valeurs
etienne = InfoTito("Etienne", "Adri", "première", "null", None)

class Grandsoeur :
    
    def __init__(self, nom) :
        self.nom = nom
    
    def enfannt(self):
        print('Mon premier enfant s\'appelle', self.nom)

class Mes_enfants(Grandsoeur):
    
    def enfannt(self):
        print(self.nom, 'est mon premier enfant')
    pass

etienne = Grandsoeur('Etienne')
etienne.enfannt()


class Info :
    def __init__(self, nom, age):
        self.__nom = nom # Accès privé
        self._age = age # Accès protégé

class Ecole :
    def __init__(self, nombre_etudiant, nombre_administration, nombre_classe) :
        self.nombre_etudiant = nombre_etudiant
        self.nombre_administration = nombre_administration
        self.nombre.classe = nombre_classe
    
    def etudiant(self):
        f"Le nombre total d'étudiant est : {self.nombre_etudiant}"

class Administration :
    def __init__(self,nom_professeur, diplome, cours):
        self.nom_professeur = nom_professeur
        self.diplome = diplome
        self.cours = cours
    
    def professeurs(self) :
        f"Voici les professeurs que nous avons : {self.nom_professeur}"

class Classe(Ecole, Administration) :
    def __init__(self, nombre_etudiant, nombre_administration, nombre_classe,nom_professeur, diplome, cours) :
        super().__init__(self, nombre_etudiant, nombre_administration, nombre_classe)
        Administration.__init__(self,nom_professeur, diplome, cours)
        print(self.nombre_administration, self.cours)

class Maman : 
    def enfants (self):
        print("mes enfants")

class Papa :
    def enfants(self):
        print('mes enfants grandissent')

class Enfants(Maman, Papa) :
    def enfants(self):
        super().enfants()
        Papa.enfants()

class Pass :
    def Tien(self):
        pass

class Yaourt :
    def lait(self):
        pass

class Definition :
    def exemple (self):
        pass

