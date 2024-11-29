reseau = {
    1: {"source" : "192.168.0.1", "destination": "192.168.0.2", "type": "IPv4", "etat": "transmise" },
    2: {"source" : "192.168.0.3", "destination": "192.168.0.4", "type": "ARP", "etat": "perdue" },
   3: {"source" : "192.168.0.5", "destination": "192.168.0.6", "type": "IPv4", "etat": "transmise" },
}
def ajouter_trame(id, source, destination,type, etat, reseau):
    reseau[4] = {"source : "  "destination :" , "type :" "etat :",reseau}
    ajouter_trame(4,"1.1.1.1","192.168.1.6","ftp","PERDUE",reseau)
    print (ajouter_trame)
    if id in reseau:
        print("Erreur, l'ID existe deja")
def modifier_etat_trame(id,nouvel_etat,reseau):
    if id not in reseau:
        print("Erreur, l'id n'existe pas !")
    else :
        reseau[nouvel_etat] = "PERDUE"
        