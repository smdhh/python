# ip = input(f"Veuillez entrer votre adresse ip : ")
ip = "192.168.123"
octets = ip.split(".")
print (octets)
# ip2=".".join(octe)
# print(ip2)


if len(octets)!=4:
    print("Adresse ip valide !")
for element in octets :
    if not element.isdigit() or not (-1 < int(element ) < 256 ):
            print("adresse ip fausse")
            break
    else :
            print("adresse ip valide !")
            break


