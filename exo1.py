def est_segment_valide(segment):
    valide = None
    if segment.isdigit():
        nombre = int(segment)
        if -1 < nombre < 256:
            valide=True 
    else :
        valide=False
    return valide
# test = est_segment_valide("88")
# print (test)
def est_ip_valide(ip):
    valide= False
    octets = ip.split(".")
    if len(octets) == 4:
        for octet in octets:
            if not est_segment_valide(octet):
                valide =  False
                break
            else:
                valide = True
    else:
        valide =  False
    return valide
# test = est_ip_valide("192.172.134.22")
# print(test)
def saisir_ip():
   while True:
      saisie = input("Saisir l'adresse IP: ")
      if est_ip_valide(saisie):
         print("Adresse IP valide")
         break
      else:
         print("Attention !!!! Adresse IP invalide")
saisir_ip()
