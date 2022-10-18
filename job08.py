largeur = input("Donnez un nombre pour la largeur ")
largeur = int(largeur)
hauteur = input("Donnez un nombre pour la hauteur")
hauteur = int(hauteur)

largeur_carac = largeur - 2
largeur_carac = int(largeur_carac)
tiret = "-" 
espace = " "
i=1
larg_tiret = tiret*largeur_carac
larg_espace = espace*largeur_carac
#print(tiret*10)                     <= for test
while i <= hauteur:
    if i == 1 or i == hauteur:
        print("|", larg_tiret, "|")
        i += 1
    else:
        print("|", larg_espace, "|")
        i += 1
