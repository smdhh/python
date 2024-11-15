def nettoyer_texte(texte):
    valide = True
    if texte.isalpha() and texte.lower():
        return texte
test = nettoyer_texte("AezrYGYfRCYfc")
print(test)
        
    