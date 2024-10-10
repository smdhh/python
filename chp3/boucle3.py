mdp = input("Veuillez donner le mot de passe : ")


max_tentatives = 3
tentatives = 0



while tentatives < max_tentatives:

    mdpp = input("Veuillez donner le bon mot de passe : ")

    
    if mdp == mdpp:
       print("Connexion réussie !!!")
       break
    else :
       tentatives +=1
       print(f"Connexion échouée. Tenatives restantes : {max_tentatives - tentatives}")

       if tentatives >= max_tentatives:
          print("Accès refusé.")
