import numpy as np
import tkinter as tk


print("\nInformation:\nLes lignes, comme les colonnes, vont de 0 a n-1;\n   ")

#....................................................................................................................................

class morpion: 
    croix=1
    cercle=2
    niveau=int(input("Les niveaux vont de 1 à 10\nQuel niveau voulez vous? "))
    vide=0

#....................................................................................................................................

def tableau_du_morpion():   #Création du tableau du jeu
    n=niveau_du_jeu(morpion.niveau)
    tableau=np.full((n,n), morpion.vide)
    return tableau

#....................................................................................................................................

def niveau_du_jeu(niveau):  #Définition des niveaux du jeu
    n=3
    if (morpion.niveau==0):
        n=n
    else:
        n=morpion.niveau+2
    return n

#....................................................................................................................................

tableau=tableau_du_morpion()

#....................................................................................................................................

def jeu_morpion(joueur, ligne, colonne):  #Fonction définissant l'affection des pions pour chaque case en fonction du joueur
    if (joueur==1):
        if (tableau[ligne][colonne]==0):
            tableau[ligne][colonne]=morpion.croix
        else:
            print("\nCette case a déja été utilisé;\nVeuillez choisir une autre case\n")
    if (joueur==2):
        if (tableau[ligne][colonne]==0):
            tableau[ligne][colonne]=morpion.cercle
        else:
            print("\nCette case a déja été utilisé;\nVeuillez choisir une autre case\n")
    return  tableau, ligne, colonne, print(tableau)

#..................................................................................................................................

def gagne(tableau, joueur, ligne, colonne):  #Fonction définissant les conditions pour qu'un joueur gagne
    c=0
    l=0
    d=0
    a_d=0
    n=len(tableau)
    for i in range(n):
        if tableau[ligne][colonne]==tableau[i][colonne]:
            c+=1
        if tableau[ligne][colonne]==tableau[ligne][i]:
            l+=1
        if tableau[ligne][colonne]==tableau[i][i]:
            d+=1
        if tableau[ligne][colonne]==tableau[n-i-1][i]:
            a_d+=1
    if c==n or l==n or d==n or a_d==n:
        return ("Fin \nLe joueur " + str(joueur) +" a gagné")
    else:
        return False
                
            

#Déroulement du jeu sur la console

joueur=1
print(tableau)
print("\nJoueur "+ str(joueur))
ligne=int(input("sur quelle ligne placez vous votre pion: "))
colonne=int(input("sur quelle colonne placez vous votre pion: "))
jeu_morpion(joueur, ligne, colonne)

while gagne(tableau, joueur, ligne, colonne)==False:
    if joueur==1:
        joueur=2
        print("\nC'est le tour du joueur numéro " + str(joueur))
        ligne=int(input("sur quelle ligne placez vous votre pion: "))
        colonne=int(input("sur quelle colonne placez vous votre pion: "))
        if tableau[ligne][colonne]==0:
            jeu_morpion(joueur, ligne, colonne) 
        else:
            joueur=1
            jeu_morpion(joueur, ligne, colonne)
    else:
        joueur=1
        print("\nC'est le tour du joueur numéro " + str(joueur))
        ligne=int(input("sur quelle ligne placez vous votre pion: "))
        colonne=int(input("sur quelle colonne placez vous votre pion: "))
        if tableau[ligne][colonne]==0:
            jeu_morpion(joueur, ligne, colonne) 
        else:
            joueur=2
            jeu_morpion(joueur, ligne, colonne)


else: 
   print(gagne(tableau, joueur, ligne, colonne))

