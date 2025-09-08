continuer = True

while continuer:
    age = input("Quel âge avez-vous ? ")
    try:
        age = int(age)
    except:
        print("Vous n'avez pas saisi une valeur numérique")
    else:
        if age == 0:
            print("Vous avez saisi zéro")
        elif age > 30:
            print("Tro vieux")
        elif age < 0:
            print("Vous avez saisi une valeur négative")
        else:
            print(f"vous avez {age} ans")
            continuer = False
    
