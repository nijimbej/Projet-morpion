import tkinter as tk
import tableau
drapeau = True

n=niveau_du_jeu(morpion.niveau)

##----- Définition des Fonctions -----##
def afficher(event) :
    """Cette fonction affiche en temps réel les coordonnées de la souris
    obtenues par « event.x » et « event.y ».
    La zone de texte est mise à jour grâce à la méthode .configure()."""
    global drapeau
    abscisse = event.x
    ordonnee = event.y
    l = (ordonnee-2)//100                    # Ligne du clic
    c = (abscisse-2)//100                    # Colonne du clic
    if drapeau:                              # drapeau == True
        dessin.create_line(100*c+8, 100*l+8, 100*c+96, 100*l+96, width = 5, fill = 'blue')
        dessin.create_line(100*c+8, 100*l+96, 100*c+96, 100*l+8, width = 5, fill = 'blue')
        message.configure(text='Aux ronds de jouer')
    else:
        dessin.create_oval(100*c+8, 100*l+8, 100*c+96, 100*l+96, width = 5, outline = 'red')
        message.configure(text='Aux croix de jouer')
    drapeau = not(drapeau)

window= tk.Tk()
window.title("Morpion")


message=tk.Label(window, text='Aux croix de jouer')
message.grid(row = 0, column = 0, columnspan=2, padx=3, pady=3, sticky = tk.W+tk.E)

button_quitter = tk.Button(window, text="Quitter", command=window.destroy)
button_quitter.grid(row = 2, column = 1, padx=3, pady=3, sticky = tk.S + tk.W + tk.E)

button_recommencer=tk.Button(window, text="Recommencer")
button_recommencer.grid(row = 2, column = 0, padx=3, pady=3, sticky= tk.S + tk.W + tk.E)


dessin=tk.Canvas(window, bg="white", width=301, height=301)
dessin.grid(row = 1, column = 0, columnspan = 2, padx=5, pady=5)

lignes = []
for i in range(n):
    lignes.append(dessin.create_line(0, 100*i+2, 303, 100*i+2, width=3))
    lignes.append(dessin.create_line(100*i+2, 0, 100*i+2, 303, width=3))

dessin.bind('<Button-1>', afficher)

window.mainloop()                      