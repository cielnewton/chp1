maChaine = ""                             # 1 : Création d'une chaine vide
print(type(maChaine))                     # 2 : Affichage du type de la variable maChaine
maChaine = str()                          # 3 : Autre méthode de création d'une chaine vide
print(type(maChaine))                     # 4 : Affichage du type de la variable maChaine
maChaine = "Bonjour les BTS CIEL !"       # 5 : Affectation d'une chaîne à la variable maChaine
print(type(maChaine))                     # 6 : Affichage du type de la variable maChaine
print(maChaine)                           # 7 : Affichage du contenu de la variable maChaine
print(maChaine.upper())                   # 8 : Mettre en majuscules le contenu de la variable maChaine
print(maChaine.lower())                   # 9 : Mettre en minuscules le contenu de la variable maChaine
print(maChaine.capitalize())              # 10 : Mettre en majuscule la première lettre de la variable
print(maChaine.title())                   # 11 : Mettre en majuscule la première lettre de chaque mot
print(len(maChaine))                      # 12 : Afficher la longueur (le nombre de caractères) de la variable
print(maChaine[6])                        # 13 : Afficher le 6ème caractère de la variable
print(maChaine[:7])                       # 14 : Afficher les caractères du 1er au 6ème
print("#######################")          # 15 : Affichage des # pour séparer les sections

uneChaine = "Python"                      # 17 : Affectation de la variable uneChaine à "Python"
for element in uneChaine:                 # 18 : Parcourir la variable uneChaine caractère par caractère
    print(element)                        # 19 : Afficher les caractères un par un
print("#######################")          # 20 : Affichage des # pour séparer les sections

i = 0                                     # 22 : Création et initialisation de la variable i
while i < len(uneChaine):                 # 23 : Tant que i est à la longueur de la chaîne
    print(uneChaine[i])                   # 24 : Affiche le caractère à la position i (Premier = 0)
    i += 1                                # 25 : Incrémenter la variable d'itération i
print("#######################")          # 26 : Affichage des # pour séparer les sections

suffixe = "Joursoir"                      # 28 : Création d'une variable et lui affecter "Joursoir"
debut = "Bon"                             # 29 : Création d'une variable et lui affecter "Bon"
salutation = debut + suffixe[:4]          # 30 : Concaténation de debut avec les 4 premiers caractères de suffixe
print(salutation)                         # 31 : Affichage du contenu de la variable salutation
salutation = debut + suffixe[-4:]         # 32 : Concaténation de debut avec la partie finale de suffixe
print(salutation)                         # 33 : Affichage du contenu de la variable salutation
salutation = debut + suffixe[:-5]         # 34 : Concaténation de debut avec une partie jusqu'au 4ème caractère de suffixe
print(salutation)                         # 35 : Affichage du contenu de la variable salutation
maChaine = "Bonjour tout le monde"
print(maChaine.startswith("Bonjour"))     # 37:  Résultat : True
print(maChaine.endswith("monde"))         # 38:  Résultat : True
print(maChaine.isalpha())                 # 39:  Résultat : True
print(maChaine.isdigit())                 # 40:  Résultat : False
print(maChaine.isalnum())                 # 41:  Résultat : False
maChaine = "42"
print(maChaine.zfill(5))                  # 43:  Résultat : "00042"
maChaine = "Bonjour tout tout le monde"
print(maChaine.count("tout"))             # 45:  Résultat : 2 Compte le nom d'occurence




