from random import randint
def surveiller ( essais) :
    tentative = 0
    
    for i in range(essais):
        SSH = randint(0, 1) 
        if SSH == 0  :
            print (f"{i+1}: Connexion réussie ")
            tentative = 0 
          
        else :
            print (f"{i+1}: Connexion échouée !!")
            tentative +=1
            i+=1
        if  tentative== 3 :
            print (f"Erreur !! {tentative} connexions échouées consécutives au bout de la {i} ème tentatives. Compte bloqué !!!!")
            break
                
surveiller (10)


