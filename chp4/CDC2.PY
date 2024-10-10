mac = input ("Veuillez entrez votre adresse mac : ")
octets = mac.split(":")
mac_valide=[]

for octet in octets:
    try:
        octet_int = int(octet)
    except:
        print(f"{octet} n'est pas une valeur correcte")
    else:
        if 0 <= int(octet) <= 6:
            if len(octets) != 6:
                print("Il faut 6 octets dans une @ MAC")
                break
            else:
                
                mac_valide.append(octet)
                
        else:     
            print(f"{octet} n'est pas compris entre 0 et 255")
      


if len(mac_valide)==4:
    print(f"Adresse ip {mac} est valide")