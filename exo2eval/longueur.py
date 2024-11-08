def est_longueur_valide(mot_de_passe):
    valide="ok"
    if len(mot_de_passe)>=8:
        valide="ok"
        return True
    else:
        return False