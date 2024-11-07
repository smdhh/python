

def traiter(taille, poids):

 
    imc = poids/((taille/100)*(taille/100))
    if imc<18.5:
        print("Vous avez un imc :",imc,"\nVous êtes une persone maigre !")
    elif 18.5<=imc<25:
        print("Vous avez un imc :",imc,"\nVous êtes une personne a corpulence normale !")
    elif 25<=imc<30:
        print("Vous avez un imc :",imc,"\nVous êtes une personne en surpoids !")
    elif 30<=imc<35:
        print("Vous avez un imc :",imc,"\nVous êtes une personne en obésité modérée!")
    elif 35<=imc<40:
        print("Vous avez un imc :",imc,"\nVous êtes une personne en obésité sévère!")
    else :
        print("Vous avez un imc :",imc,"\nVous êtes une personne en obésité morbide")
   
   
# traiter(1.80,81)