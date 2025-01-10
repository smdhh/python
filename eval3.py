



reseau = {
    1: {"source": "192.168.0.1", "destination": "192.168.0.2", "type": "IPv4", "etat": "transmise"},
    2: {"source": "192.168.0.3", "destination": "192.168.0.4", "type": "ARP", "etat": "perdue"},
    3: {"source": "192.168.0.5", "destination": "192.168.0.6", "type": "IPv4", "etat": "transmise"},
}
def ajouter_trame(id, source, destination, type, etat, reseau):
    if id in reseau:
        print(f"Cette id : {id} est déja existante.")
    else:
        reseau[id] = {"source": source, "destination": destination, "type": type, "etat": etat}
        print(f"Cette Trame avec l'id {id} à bien été ajouté.")

def modifier_etat_trame(id, nouvel_etat, reseau):
    if id not in reseau:
        print(f"La trame avec cet id est déja existante.")
    else:
        reseau[id]["etat"] = nouvel_etat
        print(f"L'état de la trame avec l'id {id} a été modifié en '{nouvel_etat}'.")

def supprimer_trame(id, reseau):
    if id not in reseau:
        print(f"La trame {id} n'existe pas.")
    else:
        del reseau[id]
        print(f"Trame {id} est bien supprimée.")
def afficher_trames_par_type(type, reseau):
    trames = [f"l'id: {id}, Source: {infos['source']}, Destination: {infos['destination']}, Etat: {infos['etat']}"
                       for id, infos in reseau.items() if infos["type"] == type]
    if trames:
        print(f"Trame de type {type} :")
        for trame in trames:
            print(trame)
    else:
        print(f"Il y a aucune trame de ce type {type} qui a été trouvée.")
