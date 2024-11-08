from special import contient_caractere_special
def contient_majuscules_et_minuscules(mot_de_passe):
    for caractere2 in mot_de_passe:
        if caractere2 in "AZERTYUIOPQSDFGHJKLMWXCVBNazertyuiopqsdfghjklmwxcvbn":
             valide="ok"
             return True
        else :
            return False