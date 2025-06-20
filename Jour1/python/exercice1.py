number = int(input("Entrez un nombre : "))

if number % 2 == 0:
    result = "Pair !"
else:
    result = "Impair !"

with open("resultat.txt", "w") as f:
    f.write(result)

print("Résultat enregistré dans resultat.txt")
