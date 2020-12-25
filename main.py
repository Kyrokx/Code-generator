import string
from random import randint, choice
from tkinter import *

# Fonction pour génerer un mot de passe
def password():
    global label_input
    password_min = 6
    password_max = 12

    all_chars = string.ascii_letters + string.punctuation + string.digits

    password = "".join(choice(all_chars)
                       for x in range(randint(password_min, password_max)))
    label_input.delete(0, END)
    label_input.insert(0, password)


# Demarrer la fenêtre
def start_window():
    global password
    global label_input
    window = Tk()
    window.iconbitmap('assets/laptop.ico')
    window.title("Génerateur de code ")
    window.minsize(670, 350)
    window.maxsize(680, 360)
    window.configure(bg="#6E8DE8")

    # La frame
    frame = Frame(window, bg="#6E8DE8")

    # Text de Bienvenue
    label_text = Label(window, text="Bienvenue sur le générateur de code !👋🏿\nFait par : Kyrokx#7573",
                       font=("Arial", 15), bg="#6E8DE8", fg="#372D2D")
    label_text.pack(expand=NO)

    # Text "Mot De Passe"
    text = Label(frame, text="Mot De Passe", font=(
        "Helvetica", 20), bg="#6E8DE8", fg="black")
    text.pack()

    # Champ d'enter
    label_input = Entry(frame, font=("Helvetica", 20),
                        bg="#6E8DE8", fg="black")
    label_input.pack()

    # Button "Générer"
    generate_texte = Button(frame, text="Générer", font=(
        "Helvetica", 20), bg="#6E8DE8", fg="black", command=password)
    generate_texte.pack(fill=X)

    # Demarrer la frame et la fenetre
    frame.pack(expand=YES)
    window.mainloop()


if __name__ == '__main__':
    start_window()
