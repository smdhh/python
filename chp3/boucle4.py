clef = input("Veuillez entrer une clef wifi :")
verifie = len(clef)
if 8 <= verifie <= 63 and clef.isalnum() :
    print("Votre clef est valide")
else :
    print("clef non valide")

