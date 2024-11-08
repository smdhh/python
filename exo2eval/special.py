from longueur import est_longueur_valide
def contient_caractere_special(mot_de_passe):
    for caractere1 in mot_de_passe:
        if caractere1 in "@#$%&":
             valide="ok"
             return True
        else :
            return False