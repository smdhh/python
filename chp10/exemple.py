
class EquipementReseau:
    def __init__(self, nom: str, adresse_ip: str):
        self.nom = nom
        self.adresse_ip = adresse_ip

    def afficher_info(self):
        return f"Nom: {self.nom}, Adresse IP: {self.adresse_ip}"

class ConnexionReseau:
    def __init__(self, equipement1: EquipementReseau, equipement2: EquipementReseau, type_connexion: str):
        self.equipement1 = equipement1
        self.equipement2 = equipement2
        self.type_connexion = type_connexion

    def afficher_details(self):
        print("Détails de la connexion :")
        print("Équipement 1 :")
        print(self.equipement1.afficher_info())
        print("Équipement 2 :")
        print(self.equipement2.afficher_info())
        print(f"Type de connexion : {self.type_connexion}")

equipement1 = EquipementReseau("Switch01", "192.168.1.1")
equipement2 = EquipementReseau("Router01", "192.168.1.254")
connexion = ConnexionReseau(equipement1, equipement2, "Ethernet")
connexion.afficher_details()