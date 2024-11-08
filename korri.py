def est_groupe_hex_valide(groupe):
  
  
  if len(groupe)==2:
    mac = ""
    octets = mac.split(":")
    for cara in groupe:
      if cara in "ABCDEFabcdef0123456789":
        return True
      else:
        return False
etat = est_groupe_hex_valide("A1")
print(etat)

def est_mac_valide(mac):
    continuer = True
    while continuer:
        valide = True
        if mac.count(":") == 5:
          octets = mac.split(":")
          return True
        else:
         return False
test = est_mac_valide("a1:a2:e4:e5:9a")
print(etat)
#def est_mac_valide(): 
    

#     continuer = True

# while continuer:
#     mac = input("Saisir l'adresse MAC: ")
#     valide = True
#     if mac.count(":") == 5:
#         octets = mac.split(":")
#         for octet in octets:
#             if len(octet) != 2:
#                 print("Chaque octet doit contenir 2 caractères")
#                 valide = False
#                 break
#             for caractere in octet:
#                 if caractere.lower() not in "abcdef0123456789":
#                     print(f"{caractere} n'est pas un caractère hexadécimal valide")
#                     valide = False
#                     break
#             if not valide:
#                 break
#     else:
#         print("Le nombre d'octets est incorrect")
#         valide = False

#     if valide:
#         print(f"{mac} est valide")
#         continuer = False
#     else:
#         print("Adresse MAC invalide, veuillez réessayer.")