def coordonnéeGPS(latitude,longitude ):
    if -90 <= latitude <= 90 :
        print (f"La latitude est : {latitude}")
    else :
        print (" La latitude est incorrecte")
    if -180 <= longitude <= 180:
        print (f"La longitude est : {longitude}")
    else :
        print (" La longitude est incorrecte")
coordonnéeGPS(56,18)