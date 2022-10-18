age = input("Bonjour, quel âge as-tu ? ")
print("Tu as " + age + " ans.")
age = int(age)
if age < 18:
    print("Tu es mineur !")
else:
    print("Tu es majeur !")
