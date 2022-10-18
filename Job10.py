from turtle import rt




#créer un fichier 
file_object = open("output.txt", "w")

#mettre le texte dedans
text = input("Ecrivez un text SVP ! ")
file_object.write(text)
file_object.close()

#ouvrir le fichier, mettre le chemin si pas dans le même dossier
file_reading = open("output.txt", "r")
data = file_reading.read()    #data est la variable qui contiendra le contenu (str) du fichier
print(data)
file_reading.close()