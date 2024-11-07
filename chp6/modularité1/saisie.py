

def saisir(message):
    
    valeur_int = 0
    while valeur_int == 0 :
        valeur_str = input(message)
       
        try:
           valeur_int = int(valeur_str) 
        except: 
            print("Vous n'avez pas saisi une valeur numérique")
        else:
            if valeur_int == 0:
                print("Vous avez saisi zéro")
            elif valeur_int < 0: 
                print("Vous avez saisi une valeur négative")
                valeur_int=0
            elif "taille" in message :
                if valeur_int > 250 :
                    print("Vous avez saisi une valeur trop élevée")
                    valeur_int = 0  
            elif "poids" in message:
                if valeur_int >250:
                    print (" Vous avez saisi un poids trop élevé")
                    valeur_int=0
           
    return int(valeur_int)
         