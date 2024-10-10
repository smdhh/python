cleewifi = input(f"Veuillez entrer votre clee :")
Verifie = len(cleewifi)
if 7 < Verifie < 64 and cleewifi.isalnum():
    print(f"Clee valide")
else :
    print (f"Clee non valide")
