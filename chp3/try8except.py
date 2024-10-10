



condition_depart = ""

while condition_depart == "":
    note_str = input("Quel est votre note? : ")
    try:
        note_int = int(note_str) # si le cast fonctionne je passe à la suite :(else) et je saute except
    except: # si le cast ne fonctionne pas je lève une exception
        print("Vous n'avez pas saisi une valeur numérique")
    else:
        if not (0< note_int < 20): # si la valeur saisie est = zéro
            print("La note doit etre comrose entre 0 et 20")
        
        
        
        else: # si la valeur saisi est correcte (différente de zéro, n'est pas négative et une valeur numérique)
            print("Vous avez {} .".format(note_int))