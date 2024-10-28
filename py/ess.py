"""Define a class Animal with a method speak().

Define another class Dog that inherits from Animal and overrides the speak() method."""

class Animal :
    def speak(self) :
        pass

class Dog :
    def speak(self):
        pass

"""Héritage des attributs :

Définir une classe Person avec les attributs name et age.

Créer une sous-classe Student qui ajoute un attribut student_id."""

class Person :
    def __init__(self, name, age) :
        self.name = name
        self.age = age    
    
    def afiiche_age(self):
        print("Mon nom est : ", self.name)

class Student(Person) :
    def  __init__(self, name, age, student_id) :
        super().__init__(self, name, age)
    
    pass


"""Définir une classe Vehicle avec une méthode description() qui affiche "Ceci est un véhicule".

Créer une sous-classe Car qui redéfinit description() pour afficher "Ceci est une voiture"."""

class Vehicule : 
    def decription(self):
        print("Ceci est un véhicule")

class  Car(Vehicule):
    def description(self):
        print('Ceci est une voiture')

"""Créer une classe Employee avec une méthode get_details() pour afficher le nom et le salaire.

Créer une sous-classe Manager qui ajoute un attribut department et utilise super() pour inclure la méthode parente dans get_details()."""

class Employee : 
    def __init__(self, nom, salaire) :
        self.nom = nom
        self.salaire = salaire
    
    def get_detail(self):
        return self.nom, self.salaire

class Manager (Employee):
    def __init__(self, nom, salaire, departement) :
        super().__init__(self, nom, salaire)
        self.departement = departement
    
    def get_detail(self):
        super().get_detail()
        return self.departement

"""Héritage multiple :

Définir les classes Class1 avec une méthode method1() et Class2 avec une méthode method2().

Créer une sous-classe DerivedClass qui hérite à la fois de Class1 et Class2, et inclut les méthodes des deux."""

class Class1 :
    def method1(self):
        pass

class Class2 :
    def method2(self):
        pass

class DrivedClass (Class1, Class2) :
    def method3(self):
        super().method1() 
        Class2.method2()
        pass


