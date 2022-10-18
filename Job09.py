hauteur = input("Donnez un nombre pour la hauteur du triangle ")
hauteur = int(hauteur)
base_carac = "_"
left_side = "/"
right_side = "\ "

espace = " "

#base=hauteur*2
i=1


while i <= hauteur:
    if i == 1:
        print(espace*(hauteur-i)+left_side+right_side)
        i+=1
    elif i == hauteur:
        print(espace*(hauteur-i)+left_side+base_carac*((i-1)*2)+right_side)
        i+=1
    else:
        print(espace*(hauteur-i)+left_side+espace*((i-1)*2)+right_side)
        i+=1
   
    
    
#