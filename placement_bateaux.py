# Fichier de stockage des choix
# Lecture de Fichier
# Fonction qui me permet d'avoir un full random 
# If / Else 

import random
import os

compteur = 0 #Initialisation du compteur
ship = [" "," "," "," "," "," "]
ship[1] = 5  #Porte-avion (5 cases)
ship[2] = 4  #Croiseur (4 cases)
ship[3] = 2  #torpilleur (2 cases)
ship[4] = 3  #Sous-marin 1 (3 cases)   #s
ship[5] = 3  #Sous-marin 2 ( cases)    #m 

#
#
#
#
#FIND THE SHIP POS : Grille[0][3] means A4


tir_colonne = ""
tir_ligne = ""
                 
Grille =[["0","0","0","0","0","0","0","0","0","0"],     # installation du tableau 
        ["0","0","0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0","0","0"]]

def generate_full_random_grid() :    
     randomGrille =[["0","0","0","0","0","0","0","0","0","0"],     # installation du tableau 
                   ["0","0","0","0","0","0","0","0","0","0"],
                   ["0","0","0","0","0","0","0","0","0","0"],
                   ["0","0","0","0","0","0","0","0","0","0"],
                   ["0","0","0","0","0","0","0","0","0","0"],
                   ["0","0","0","0","0","0","0","0","0","0"],
                   ["0","0","0","0","0","0","0","0","0","0"],
                   ["0","0","0","0","0","0","0","0","0","0"],
                   ["0","0","0","0","0","0","0","0","0","0"],
                   ["0","0","0","0","0","0","0","0","0","0"]]

     tableaux =[5,4,3,3,2]
     tab_Check = [["0","0","0","0","0","0","0","0","0","0"],   
                 ["0","0","0","0","0","0","0","0","0","0"],
                 ["0","0","0","0","0","0","0","0","0","0"],
                 ["0","0","0","0","0","0","0","0","0","0"],
                 ["0","0","0","0","0","0","0","0","0","0"],
                 ["0","0","0","0","0","0","0","0","0","0"],
                 ["0","0","0","0","0","0","0","0","0","0"],
                 ["0","0","0","0","0","0","0","0","0","0"],
                 ["0","0","0","0","0","0","0","0","0","0"],
                 ["0","0","0","0","0","0","0","0","0","1"]]
     test = ""                                                    #Permet d'eliminer les valeurs où les bateaux ne peuvent pas être placé
     test_2 = ""
     Nope = ""
     for b in range(0,5) :
                for i in range(9) :
                    for j in range(9) :
                        if randomGrille[i][j]!= "0" :
                            tab_Check[i][j]= "1"
                
                Nope = " wrong "
                while Nope != " good " :
                    orientation = random.randint(1,2)           #Orientation: 1 = horizontal, 2 = vertical
                    orientation = 1
                    if orientation == 1 :             
                        test = tableaux[b]
                        test_2 = test
                        x = 9
                        y = 9  
                        w = 9 - (tableaux[b])
                        while tab_Check [x][y]!= "0" :
                            x = random.randint (0,w)
                            y = random.randint (0,9)
                    
                        while test_2 != 0 :
                            for i in range(tableaux[b]) :
                                if randomGrille[x+i][y] == "0" :
                                    test_2 = test_2-1
                                else :
                                    test_2 = test
                                    for j in range(tableaux[b]) :
                                         randomGrille [x+j][y]= "0"
                                         print ( " impossible ")
                                         Nope = False
                        for i in range(tableaux[b]):
                            randomGrille [x+i][y] = b+1
                        Nope = " good "
                        
                    if orientation == 2 :
                        test = tableaux[b]
                        test_2 = test
                        w = 9 - (tableaux[b])
                        x = random.randint(0,9)
                        y = random.randint(0,w)
                        while test_2 !=0 :
                            for i in range (tableaux[b]) :
                                if randomGrille[x][y+i] == "0" :
                                    test_2 = test_2-1
                                else :
                                    test_2 = test
                                    for j in range (tableaux[b]) :
                                        randomGrille[x][y+j] = "0"
                                        print (" impossible ")
                                        Nope = False
                        Nope = " good "
                        for i in range(tableaux[b]) :
                            randomGrille[x][y+i] = b+1 
     #print( randomGrille )
     return randomGrille

def retrieve_default_files( path_to_folder ) :
    Files = []
    #print( path_to_folder )
    for r, d, f in os.walk( path_to_folder ) :
        for file in f :
                if '.txt' in file :
                    Files.append( file)
    
    print ( Files )        
    return Files

def load_file(file_name) : 
    Grille =[["0","0","0","0","0","0","0","0","0","0"],   
            ["0","0","0","0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0","0","0","0"]]
    position = ['p','c','t','s','m']
    try :
        file = open(file_name)
        Result = file.readlines() # pour lire ligne par ligne 
        file.close()
        ligne = 0 

        for line in Result : 
            # print (str(ligne) + line) 
            if ligne > 0 and ligne < 11 :  # les lignes 0 et 11 sont inutiles car ne font pas partie de la grille 
                colonne = 0 
                for col in line : 
                    #print( str(ligne) + '.' + str(colonne) + col )
                    if colonne > 0 and colonne < 11 and col != ' ' : 
                        #print(position.index(col) + 1 )
                        Grille[ligne-1][colonne-1] = str(position.index(col) + 1)
                    colonne += 1 
            ligne += 1 
            # print( str(colonne) + col )
    except FileNotFoundError:
        print('Le fichier est introuvable')
    except IOError:
        print("Erreur d'entrée/sortie")
    # print(Result) 
    return Grille 
    

#A changer sur chaque ordinateur
path_to_default_folder ='/Users/jimdecoster/Desktop/INFO-Projet/placement de Bateaux'


full_random = False


if full_random : # si on appuie sur Random, le placement est full random. A adapter avec le notation de Nico.  
     chosen_grille_1 = generate_full_random_grid()
     chosen_grille_2 = generate_full_random_grid()

     
else : # si on appuie sur Random from directory, le programme ira chercher aléatoirement un placement parmis une liste de choix stocké dans un fichier  
    list_default_files = retrieve_default_files(path_to_default_folder)
    chosen_file_1 = random.choice(list_default_files) #Player 1
    print(path_to_default_folder + '/' + chosen_file_1)
    chosen_grille_1 = load_file(path_to_default_folder + '/' + chosen_file_1) 

    chosen_file_2 = random.choice(list_default_files) #Player 2 
    print(path_to_default_folder + '/' + chosen_file_2)
    chosen_grille_2 = load_file(path_to_default_folder + '/' + chosen_file_2) 



print(chosen_grille_1) # a remplacer par l'adaptation kivy
print(chosen_grille_2)


# Je n'ai ps trop compris si je devais remplacer par "P1 Carrier" ou "P2 Carrier" ou non étant donné que dans notre discussion Messenger, tu as dit que tu disais une connerie. Je préfère te laisser cadapter le nom de ce qu'il faut en fonction de tes besoins histoire de ne rien faire déconner.
