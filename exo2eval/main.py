from Chiffres import contient_chiffres
from MajetMin import contient_majuscules_et_minuscules
from special import contient_caractere_special
from longueur import est_longueur_valide
def verifier_mot_de_passe():
    mdp = input("Saisissez votre de passe :") 
    if mdp :
        print ("Mot de passe sécurisé")
    else :
        print ("Mot de passe non sécurisé")

verifier_mot_de_passe("")

