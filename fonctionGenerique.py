def saisir(message):

    #Gestion des erreurs
    valeur_int = 0
    while valeur_int == 0:
        valeur_str = input(message)
        try:
            valeur_int = int(valeur_str) # si le cast fonctionne je passe à la suite :(else) et je saute except
        except: # si le cast ne fonctionne pas je lève une exception
            print("Vous n'avez pas saisi une valeur numérique")
        else:
            if valeur_int == 0: # si la valeur saisie est = zéro
                print("Vous avez saisi zéro")
            elif valeur_int < 0: # si la valeur saisie est négative
                print("Vous avez saisi une valeur négative")
                valeur_int = 0   #je réaffecte 0 à valeur_int pour revenir à la condition initiale

            elif "taille" in message:
                if valeur_int > 250:
                    print("Vous avez une taille trop elevée!")
                    valeur_int = 0

            elif "poids" in message:
                if valeur_int > 250:
                    print("Vous avez un poids trop elevé!")
                    valeur_int = 0
           
                
    return valeur_int

maTaille = saisir("Saisir votre taille: ")
monPoids = saisir("Saisir votre poids: ")

