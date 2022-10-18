file_reading = open("data.txt", "r")
content = file_reading.read()    #content est la variable qui contiendra le contenu (str) du fichier
file_reading.close()
#print(content) #=> vérifie qu'on lit bien le fichier et qu'il n'a plus les points et virgules
words = content.split() # découpe le texte selon les espaces
print('Number of words in text file :', len(words))  