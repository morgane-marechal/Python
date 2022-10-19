
#on part du principe qu'on va changer la mise en forme de la première chaîne de caractère qui est dans la variable input1
input1 = input("Taper des mots: ")
#onchoisit la mise en forme avec le deuxième input
input2 = input("Tapez l'un des mots suivant : upper, lower, title, clean  ")

#méthode avec des dictionnaires
lower_dictionnary = { " ": " ", "A": "a", "B": "b", "C": "c", "D": "d", "E": "e", "F": "f", "G": "g", "H": "h", "I": "i", "J": "j", "K": "k", "L": "l", "M": "m", "N": "n", "O": "o", "P": "p", "Q": "q", "R": "r", "S": "s", "T": "t", "U": "u", "V": "v", "W": "w", "X": "x", "Y": "y", "Z": "z", ".": ".", ",": ",", "?": "?", "!": "!", ":": ":", ";": ";", "/": "/" }
upper_dictionnary = { " ": " ", "a": "A", "b": "B", "c": "C", "d": "D", "e": "E", "f": "F", "g": "G", "h": "H", "i": "I", "j": "J", "k": "K", "l": "L", "m": "M", "n": "N", "o": "O", "p": "P", "q": "Q", "r": "R", "s": "S", "t": "T", "u": "U", "v": "V", "w": "W", "x": "X", "y": "Y", "z": "Z", ".": ".", ",": ",", "?": "?", "!": "!", ":": ":", ";": ";", "/": "/" }

#avec les dictionnaires
def myUpper_dictionnary():       
    for letter in input1: 
        #print(lettre)                                                  # => il faut itérer à travers chaque lettre de input1
        for key, value in upper_dictionnary.items():                    # =>  puis a traver les clé et les valeurs du tableau
            if letter == key:
                letter = value
                print(value, end="")
            elif letter == value:
                print(value,  end="")
            

def myLower_dictionnary():      
    for letter in input1:                                                   # => il faut itérer à travers chaque lettre de input1
        for key, value in lower_dictionnary.items():
            if letter == key:                                                   
                letter = value
                print(value, end="")
            elif letter == value:
                print(value, end="")                   
    
#fonction myUpper avec la methode replace
"""import re
def myUpper(): 
    s = input1
    for r in (("a", "A"), ("b", "B"), ("c", "C"), ("d", "D"), ("e", "E"), ("f", "F"), ("g", "G"), ("h", "H"), ("i", "I"), ("j", "J"), ("k", "K"), ("l", "L"), ("m", "M"), ("n", "N"), ("o", "O"), ("p", "P"), ("q", "Q"), ("r", "R"), ("s", "S"), ("t", "T"), ("u", "U"), ("v", "V"), ("w", "W"), ("x", "X"), ("y", "Y"), ("z", "Z") ):
        s = s.replace(*r)
    print(s)   
#myUpper()
"""
#avec methode split et join pour myClean
def myClean():
    quote = input1
    new_quote = ' '.join(quote.split())
    print(new_quote)

def myTitle():
    x=0
    print(x)
    while x<len(input1):
        print(x)
        if input1[0]:
            for key, value in upper_dictionnary.items():
                if input1[0] == key:
                    print(value, end="")    
                    x+=1 
                else:  
                    print(key, end="")    
                    x+=1      
               
        elif input1[x-1] == " ":
            for key, value in upper_dictionnary.items():
                if input1[x] == key:
                    print(value, end="")    
                    x+=1
                else:  
                    print(key, end="")    
                    x+=1         
                       
         
        else:
            for key, value in upper_dictionnary.items():
                if input1[x] == value:
                    print(key, end="")     
                    x+=1
                
                 
                       
   
    
    """
    for letter in input1:
        for key, value in upper_dictionnary.items():
            if [letter - 1] == " ":
                letter = value
                print(value, end="")
            elif letter == value:
                letter = key
                print(key, end="")
            else:
                letter = key
                print(key, end="")

"""
"""
import re
#regex = r"(\s)([a-z])"
regex = r'\[a-z]\w+'
replace = r'\[A-Z]\w+'
def myTitle():
    str = input1
    result = re.sub(regex, replace, str)
    print(result)
"""

if input2 == "upper":
    myUpper_dictionnary()
elif input2 == "lower":
    myLower_dictionnary()
elif input2 == "title":
    myTitle()
elif input2 == "clean":
    myClean()
else:
    print("Taper l'un des quatres mots suivant => upper, lower, title, clean  ")




