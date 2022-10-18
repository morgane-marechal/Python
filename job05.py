number1 = input("Donnez un nombre ")
print("Tu as as choisis le nombre: ", number1)
number1 = int(number1)
number2 = input("Donnez un autre nombre : ")
print("Tu as as choisis comme second nombre:  ", number2)
number2 = int(number2)


if number1 < number2:
    for i in range(number1, number2):
        if i == number1 or i == number2: 
            print("Ce sont des valeurs égales")
        else:
            print("Valeur: ", i)
    print("Ce sont des valeurs égales")
else:
    for i in range(number1, number2, -1):
        if i == number1 or i == number2: 
            print("Ce sont des valeurs égales")
        else:
            print("Valeur: ", i)
    print("Ce sont des valeurs égales")