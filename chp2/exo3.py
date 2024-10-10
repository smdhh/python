from random import randint
essais = 0
while True :

    nb1 = randint(1,20)
    nb2 = randint(1,20)
    essais += 1
    print(f"Essai {essais}: Nombre 1 = {nb1}, Nombre 2 = {nb2}")
    
    if nb1 == nb2:
        print(f"Félicitations! Les deux nombres sont égaux ({nb1}).")
        break
    else:
        reponse = input("Les nombres sont différents. Voulez-vous rejouer (o/n) ? ").lower()
        if reponse != 'o':
            print(f"Vous avez effectué {essais} essai(s). Au revoir !")
            break



