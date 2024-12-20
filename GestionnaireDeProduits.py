class Produit:
    def __init__(self, nom, prix, quantite):
        self.nom = nom
        self.prix = prix
        self.quantite = quantite

    def __str__(self):
        return f"Produit: {self.nom} | Prix: {self.prix}TND | Quantité: {self.quantite}"

class Rayon:
    def __init__(self, categorie):
        self.categorie = categorie
        self.produits = []

    def ajouterProd(self, produit):
        self.produits.append(produit)

    def suppProd(self, nom_produit):
        for produit in self.produits:
            if produit.nom == nom_produit:
                self.produits.remove(produit)
                return True
        return False

    def affRayon(self):
        if len(self.produits)==0:
            return f"Le rayon {self.categorie} est vide."
        else:
            res=f"Rayon {self.categorie}:\n"
            for produit in self.produits:
                    res+=str(produit)+"\n"
            return res
        


class Stock:
    def __init__(self):
        self.rayons = []

    def ajouterRay(self, rayon):
        self.rayons.append(rayon)

    def findRay(self, categorie):
        for rayon in self.rayons:
            if rayon.categorie == categorie:
                return rayon
        return None

    def afficheS(self):
        if not self.rayons:
            return "Le stock est vide."
        return "\n\n".join(rayon.affRayon() for rayon in self.rayons)

    def findProd(self, prod):
        resultats = []
        for rayon in self.rayons:
            for produit in rayon.produits:
                if prod.lower() in produit.nom.lower():
                    resultats.append((rayon.categorie, produit))
        if not resultats:
            return "Aucun produit trouvé."
        return "\n".join(f"Rayon: {cat}, {prod}" for cat, prod in resultats)

def menu():
    stock = Stock()
    while True:
        print("\nMenu :")
        print("1. Ajouter un rayon")
        print("2. Ajouter un produit")
        print("3. Afficher le contenu d'un rayon")
        print("4. Supprimer un produit d'un rayon")
        print("5. Afficher la totalité du stock")
        print("6. Rechercher un produit par nom")
        print("7. Quitter")
        
        choix = input("Choisissez une option : ")
        
        if choix == "1":
            categorie = input("Entrez la catégorie du rayon : ")
            stock.ajouterRay(Rayon(categorie))
            print(f"Rayon {categorie} ajouté avec succès.")
        
        elif choix == "2":
            categorie = input("Entrez la catégorie du rayon pour ajouter le produit : ")
            rayon=stock.findRay(categorie);
            if rayon:
                nom = input("Entrez le nom du produit : ")
                prix = float(input("Entrez le prix du produit : "))
                quantite = int(input("Entrez la quantité du produit : "))
                rayon.ajouterProd(Produit(nom, prix, quantite))
                print(f"Produit {nom} ajouté au rayon {categorie}.")
            else:
                print(f"Rayon {categorie} introuvable.")
        
        elif choix == "3":
            categorie = input("Entrez la catégorie du rayon : ")
            rayon = stock.findRay(categorie)
            if rayon:
                print(rayon.affRayon())
            else:
                print(f"Rayon {categorie} introuvable.")
        
        elif choix == "4":
            categorie = input("Entrez la catégorie du rayon : ")
            rayon = stock.findRay(categorie)
            if rayon:
                nom_produit = input("Entrez le nom du produit à supprimer : ")
                if rayon.suppProd(nom_produit):
                    print(f"Produit {nom_produit} supprimé.")
                else:
                    print(f"Produit {nom_produit} introuvable.")
            else:
                print(f"Rayon {categorie} introuvable.")
        
        elif choix == "5":
            print(stock.afficheS())
        
        elif choix == "6":
            prod = input("Entrez le nom ou une partie du nom du produit  : ")
            print(stock.findProd(prod))
        
        elif choix == "7":
            print("Byee")
            break
        
        else:
            print("veuillez réessayer.")

#pp
menu()
