def detecter_mot_suspect(texte,mot_suspect):
    for caractere in texte :
        valide = True
        if caractere in "attaque" or "virus":
            valide = True 
        else :
            valide = False
    return valide
test = detecter_mot_suspect("vzqduvzv iyeqgdizoh lbcihbv","attaque, virus")
print (test)