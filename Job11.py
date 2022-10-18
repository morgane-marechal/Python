
file_reading = open("domains.xml", "r")
data = file_reading.read()    #data est la variable qui contiendra le contenu (str) du fichier
#print(data) => vérifie qu'on lit bien le fichier



import re
pattern = r"[a-z0-9\.\-+_]+\.[a-z]+"  # => définir une regex qui va reconnaitre les noms de domaine
domains_number = re.findall(pattern, data)   #email correspond aux noms de domaine recherché => cela va créer un array
#print(domains_number)  # => vérifie qu'on a bien un tableau
nbr = len(domains_number)
print(nbr)
# compter le nomre d'éléments du tableau
