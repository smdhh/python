
utilisateur_correct = "sami"
max_tentatives = 3
tentatives = 0
while tentatives < max_tentatives:
    utilisateur = input("Veuillez donner votre nom d'utilisateur : ")
    if utilisateur == utilisateur_correct:
       print("Connexion réussie !!!")
       break
    else :
       tentatives +=1
       print(f"Connexion échouée. Tenatives restantes : {max_tentatives - tentatives}")

       if tentatives >= max_tentatives:
          print("Accès refusé.")
