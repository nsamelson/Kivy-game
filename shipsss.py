import random
import os

compteur = 0  # Initialisation du compteur

ship = [" "," "," "," "," "," "]
ship[1] = 5  #Porte-avion (5 cases)
ship[2] = 4  #Croiseur (4 cases)
ship[3] = 2  #torpilleur (2 cases)
ship[4] = 3  #Sous-marin 1 (3 cases)   #s
ship[5] = 3  #Sous-marin 2 ( cases)    #m """
Alpha =["A","B","C","D","E","F","G","H","I","J"]





tir_colonne = ""
tir_ligne = ""

Grille = [["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],  # installation du tableau
          ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
          ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
          ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
          ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
          ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
          ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
          ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
          ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
          ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]]


def generate_full_random_grid():
    randomGrille = [["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],  # installation du tableau
                    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]]

    tableaux = [5, 4, 3, 3, 2]
    tab_Check = [["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                 ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                 ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                 ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                 ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                 ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                 ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                 ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                 ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                 ["0", "0", "0", "0", "0", "0", "0", "0", "0", "1"]]
    test = ""  # Permet d'eliminer les valeurs où les bateaux ne peuvent pas être placé
    test_2 = ""
    Nope = ""
    for b in range(0, 5):
        for i in range(9):
            for j in range(9):
                if randomGrille[i][j] != "0":
                    tab_Check[i][j] = "1"

        Nope = " wrong "
        while Nope != " good ":
            orientation = random.randint(1, 2)  # Orientation: 1 = horizontal, 2 = vertical
            orientation = 1
            if orientation == 1:
                test = tableaux[b]
                test_2 = test
                x = 9
                y = 9
                w = 9 - (tableaux[b])
                while tab_Check[x][y] != "0":
                    x = random.randint(0, w)
                    y = random.randint(0, 9)

                while test_2 != 0:
                    for i in range(tableaux[b]):
                        if randomGrille[x + i][y] == "0":
                            test_2 = test_2 - 1
                        else:
                            test_2 = test
                            for j in range(tableaux[b]):
                                randomGrille[x + j][y] = "0"
                                print(" impossible ")
                                Nope = False
                for i in range(tableaux[b]):
                    randomGrille[x + i][y] = b + 1
                Nope = " good "

            if orientation == 2:
                test = tableaux[b]
                test_2 = test
                w = 9 - (tableaux[b])
                x = random.randint(0, 9)
                y = random.randint(0, w)
                while test_2 != 0:
                    for i in range(tableaux[b]):
                        if randomGrille[x][y + i] == "0":
                            test_2 = test_2 - 1
                        else:
                            test_2 = test
                            for j in range(tableaux[b]):
                                randomGrille[x][y + j] = "0"
                                print(" impossible ")
                                Nope = False
                Nope = " good "
                for i in range(tableaux[b]):
                    randomGrille[x][y + i] = b + 1
                    # print( randomGrille )
    return randomGrille

full_random = True



if full_random : # si on appuie sur Random, le placement est full random. A adapter avec le notation de Nico.
     chosen_grille_1 = generate_full_random_grid()
     chosen_grille_2 = generate_full_random_grid()

def get_ships_random():
    Carrier = []
    Cruiser = []
    Submarine1 = []
    Submarine2 = []
    Torpedo = []
    Ships=[Carrier, Cruiser, Submarine1, Submarine2, Torpedo]
    for line in chosen_grille_1:
        print(line)
        for col in line:
            if col == 5:
                Torpedo.append(Alpha[chosen_grille_1.index(line)]+str(line.index(col) + 1))
            if col ==4:
                Submarine1.append(Alpha[chosen_grille_1.index(line)] + str(line.index(col) + 1))
            if col== 3:
                Submarine2.append(Alpha[chosen_grille_1.index(line)] + str(line.index(col) + 1))
            if col ==2:
                Cruiser.append(Alpha[chosen_grille_1.index(line)] + str(line.index(col) + 1))
            if col ==1:
                Carrier.append(Alpha[chosen_grille_1.index(line)] + str(line.index(col) + 1))
    print(Ships)

get_ships_random()
