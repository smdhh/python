from MajetMin import contient_majuscules_et_minuscules
def contient_chiffres(mot_de_passe):
    for caractere3 in mot_de_passe:
        if caractere3 in "1234567890":
             valide="ok"
             return True
        else :
            return False