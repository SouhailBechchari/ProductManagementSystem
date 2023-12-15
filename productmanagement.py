from abc import ABCMeta, abstractmethod

class Composition:
    def __init__(self, produit, quantite):
        self.__produit = produit
        self.__quantite = quantite

    @property
    def produit(self):
        return self.__produit

    @property
    def quantite(self):
        return self.__quantite
    
    @produit.setter
    def produit(self, value):
        self.__produit = value

    @quantite.setter
    def quantite(self, value):
        self.__quantite = value

    def __str__(self):
        return str(self.__dict__)

class Produit(metaclass=ABCMeta):
    def __init__(self, nom, code):
        self.__nom = nom
        self.__code = code

    @property
    def nom(self):
        return self.__nom

    @property
    def code(self):
        return self.__code
    
    @nom.setter
    def nom(self, value):
        self.__nom = value

    @code.setter
    def code(self, value):
        self.__code = value

    @abstractmethod
    def getPrixHT(self):
        pass
    
    def equals(self, other):
        return self.__code == other.__code

    def __str__(self):
        return str(self.__dict__)

class ProduitElementaire(Produit):
    def __init__(self, nom, code, prixAchat):
        super().__init__(nom, code)
        self.__prixAchat = float(prixAchat)

    def getPrixHT(self):
        return self.__prixAchat

    def equals(self, other):
        return self.__prixAchat == other.__prixAchat

    def __str__(self):
        return str(self.__dict__)

class ProduitCompose(ProduitElementaire):
    tauxTVA = "18%"

    def __init__(self, nom, code, prixAchat, fraisFabrication, listeConstituants=None):
        super().__init__(nom, code, prixAchat)
        self.__fraisFabrication = float(fraisFabrication)
        self.__listeConstituants = listeConstituants or []

    @property
    def fraisFabrication(self):
        return self.__fraisFabrication

    @property
    def listeConstituants(self):
        return self.__listeConstituants
    
    def __str__(self):
        return str(self.__dict__)

    def getPrixHT(self):
        total_prix_ht = sum(constituant.produit.getPrixHT() * constituant.quantite for constituant in self.__listeConstituants)
        total_prix_ht += self.__fraisFabrication
        return total_prix_ht


produitele1 = ProduitElementaire("Produit1", "65", "78")
produitele2 = ProduitElementaire("Produit2", "900", "999")
print(produitele1.equals(produitele2))
print(produitele1.__str__())
print(produitele2.__str__())
composition1 = Composition(produitele1, 2)
composition2 = Composition(produitele2, 3)
produit_compose = ProduitCompose("ProduitCompose1", "100", "0", "20.0", [composition1, composition2])

print(produitele1.getPrixHT())  
print(produit_compose.getPrixHT()) 
print(produitele1.equals(produitele2))
print(produitele1.__str__())
print(produitele2.__str__())
