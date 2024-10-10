ip = input ("Veuillez entrez votre adresse ip : ")
octets = ip.split(".")
ip_valide=[]

for octet in octets:
    try:
        octet_int = int(octet)
    except:
        print(f"{octet} n'est pas une valeur correcte")
    else:
        if 0 <= int(octet) <= 255:
            if len(octets) != 4:
                print("Il faut 4 octets dans une @ IP")
                break
            else:
                
                ip_valide.append(octet)
                
        else:     
            print(f"{octet} n'est pas compris entre 0 et 255")
      


if len(ip_valide)==4:
    print(f"Adresse ip {ip} est valide")
