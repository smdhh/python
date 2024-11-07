from random import randint
def surveiller (seuil, essais) :
    tentative = 0
    
    for i in range(essais):
        debitRéseau = randint(50, 120)
        if debitRéseau <=seuil :
            print (f"{i+1 }:  Débit réseau {debitRéseau} Mbps est sous contrôle. ")
            tentative = 0 
          
        else :
            print (f"{i+1 }: Débit réseau {debitRéseau} Mbps dépasse le seuil de 100 Mbps.")
            tentative +=1
            i+=1
        if tentative == 3 :
            print ("Une alerte a été détectée, le débit est trop élevé !!!!")
            break
                
surveiller (100,10)


