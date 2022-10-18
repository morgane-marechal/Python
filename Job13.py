nb_letter = input("Donnez un nombre entier: ")
nb_letter = int(nb_letter)
file_reading = open("data.txt", "r")
content = file_reading.read()    #content est la variable qui contiendra le contenu (str) du fichier
#print(data) => vérifie qu'on lit bien le fichier
file_reading.close()



words = content.split()
#print(words) #words = content.split() # découpe le texte selon les espaces pour avoir le nb de emots
#print(content.replace("!#$%^&*().,)?;:", ''))
content = content.replace('.', '')
content = content.replace(',', '')
content = content.replace(';', '')
content = content.replace('?', '')
content = content.replace('!', '')
content = content.replace('$', '')

#print(content) #=> pour vérifier suppression des points et virgules

def countWordlen(words):
    count = 0
    for i in words: # loop over the items of the list
        if len(i) == nb_letter: # if the len the items (words) equals nb_letter increment count by 1
            count = count + 1
    return count

words_with_spe_length = countWordlen(words)
print(words_with_spe_length)


