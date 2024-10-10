# from random import randint
# nb1 = randint(1,100)
# nb2 = randint(1,100)
# print (nb1)
# print (nb2)

# calculordi= nb1 + nb2
# calculutilisateur = int(input("Quel est le résultat de la somme des deux chiffres ?"))
# if calculutilisateur == calculordi:
#     print ("Bravo !!")
# else  :
#     print (" Veuillez réessayer ou quitter !")

from random import randint
nb1 = randint(1,100)
nb2 = randint(1,100)
print (nb1)
print (nb2)

calculordi= nb1 + nb2
print("Resultat = ",calculordi)
continuer = "o"
while continuer=="o":
    calculutilisateur = int(input(f"Quel est le résultat de la somme des deux chiffres {nb1} {nb2}?: "))
    if calculutilisateur == calculordi:
        print ("Bravo !!")
        continuer=""
    else  :
       print (" faux ")
       continuer=input ("appuyez sur o pour continuer ou autre pour quitter ")
       
    

        