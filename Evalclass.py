class DispositifEclairage:

    def __init__(self, nom, etat=False):
        self.nom = nom
        self.etat = etat

    def allumer(self):
        self.etat = True
        print(f"{self.nom} est allumé.")

    def eteindre(self):
        self.etat = False
        print(f"{self.nom} est éteint.")

    def afficher_informations(self):
        etat_ = "Allumé" if self.etat else "Éteint"
        print(f"Dispositif : {self.nom} | État : {etat_}")

class AmpouleIntelligente(DispositifEclairage):
    def __init__(self, nom, intensite=50, etat=False):
        super().__init__(nom, etat)
        self.intensite = intensite 

    def regler_intensite(self, intensite):

        if 0 <= intensite <= 100:
            self.intensite = intensite
            print(f"L'intensité de {self.nom} a été réglée à {self.intensite}%.")
        else:
            print("Il y a une erreur, l'intensité doit être entre 0 et 100.")

    def afficher_informations(self):
        super().afficher_informations()
        print(f"Intensité : {self.intensite}%")

class BandeLEDIntelligente(DispositifEclairage):
    def __init__(self, nom, couleur="Blanc", etat=False):
        super().__init__(nom, etat)
        self.couleur = couleur  

    def changer_couleur(self, couleur):
        self.couleur = couleur
        print(f"La couleur de {self.nom} a été changé en {self.couleur}.")

    def afficher_informations(self):
        super().afficher_informations()
        print(f"Couleur : {self.couleur}")


class SystemeEclairage:
    def __init__(self):
        self.dispositifs = []

    def ajouter_dispositif(self, dispositif):
        self.dispositifs.append(dispositif)
        print(f"{dispositif.nom} a bien été ajouté.")

    def afficher_tous_dispositifs(self):
        print("\n====== Informations sur le système d'éclairage ======")
        for dispositif in self.dispositifs:
            dispositif.afficher_informations()

def main():
    ampoule = AmpouleIntelligente("Ampoule du salon intelligente", intensite=65)
    bande_led = BandeLEDIntelligente("Bande LED cuisine led", couleur="Violet")
    lampe_generique = DispositifEclairage("Lampe générique")
    systeme = SystemeEclairage()
    systeme.ajouter_dispositif(ampoule)
    systeme.ajouter_dispositif(bande_led)
    systeme.ajouter_dispositif(lampe_generique)

    ampoule.allumer()
    ampoule.regler_intensite(75)

    bande_led.allumer()
    bande_led.changer_couleur("Verte")

    lampe_generique.eteindre()
    systeme.afficher_tous_dispositifs()


if __name__ == "__main__":
    main()