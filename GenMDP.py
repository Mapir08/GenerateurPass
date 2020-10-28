#! /usr/bin/python3
# -*- coding: utf-8 -*-

from tkinter import *
import string
from random import randint, choice


def genere_pass():
    password_min = 8
    password_max = 8
    all_chars = string.ascii_letters + string.digits + "!?/@"
    password = "".join(choice(all_chars) for x in range(randint(password_min, password_max)))
    pass_entry.delete(0, END)
    pass_entry.insert(0, password)


# création de la fenetre
window = Tk()
window.title("Générateur de mot de passe, by MAPIR")
window.geometry("600x250")
window.minsize(600, 250)
window.maxsize(600, 250)
#window.iconbitmap("logo.ico")
window.config(background='#4065A4')

# création des frames
# frame contenant image et frame1
frame = Frame(window, bg='#4065A4')
frame.pack(expand=YES)
# frame d'affichage et visu de l'appli
frame1 = Frame(frame, bg='#4065A4')
frame1.grid(row=0, column=1, padx=30)

# création d'une image
width = 200
height = 170
#image = PhotoImage(file="pass.png").subsample(4) #problème avec l'affichage de la photo
canvas = Canvas(frame, width=width, height=height, highlightthickness=0, bg='#4065A4')
#canvas.create_image(width / 2, height / 2, image=image)  # width et height /2 pour avoir le point centrale
canvas.grid(row=0, column=0)

# création des différents champs
# titre
label_title = Label(frame1, text="Générateur de MDP", font=("Helvetica", 25), bg='#4065A4', fg="#2B446C")
label_title.pack()
# sous titre
label_subtitle = Label(frame1, text="by MAPIR", font=("Arial", 14, "italic"), bg='#4065A4', fg="#324E7C")
label_subtitle.pack()
# champs de texte / Entré
pass_entry = Entry(frame1, justify=CENTER, font=("Helvetica", 25), bg='#4065A4', fg="white", highlightthickness=0)
pass_entry.pack()
# bouton
button = Button(frame1, width=10, activeforeground="orange", text="Générer", font=("Helvetica", 18), fg="#2B446C",
                highlightthickness=0, command=genere_pass)
button.pack(pady=10)

# création d'une barre de menu
menu_bar = Menu(window)
# créer un premier menu
file_menu = Menu(menu_bar)
file_menu.add_command(labe="Générer", command=genere_pass)
file_menu.add_command(labe="Quitter", command=window.quit)
menu_bar.add_cascade(label="Fichier", menu=file_menu)
# configurer la fenetre pour ajouter le menu_bar
window.config(menu=menu_bar)

# on lance une boucle de maintien, pour afficher la fenetre
window.mainloop()
