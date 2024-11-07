def verif(mdp="admin123"):
    tentative=0
    for i in range(3):
        Saisir = input ("Veuillez entrer le mot de passe :")
        if mdp==Saisir:
            print ("Acces autorise !!")
            break
        else:
            print ("Mot de passe incorrect. Veuillez réessayer !")
            tentative+=1
            if tentative==3:
                print("Alerte, compte bloque!!!!!!!!!!!!")
                break  
verif()

