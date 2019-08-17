from tkinter import *
# Creation de la fenetre avec TK
fen = Tk()

# Ajouter le titre de la fenetre
fen.title('Fenetre Examen')

# Creation des labels
text1 = Label(fen, text='ENREGISTREMENT DES EMPLOYES')
text1.grid(row=0, column=2)

text2= Label(fen, text='Nom')
text2.grid(row=3, column=0)

text3= Label(fen, text='Prenom')
text3.grid(row=4, column=0)

text3= Label(fen, text='NIF')
text3.grid(row=5, column=0)

# Creation des inputs
entre1= Entry(fen)
entre1.grid(row=3, column=2)

entre2 = Entry(fen)
entre2.grid(row=4, column=2)

entre3 = Entry(fen)
entre3.grid(row=5, column=2)


# Creation du boutton
bouton1= Button(fen, text='FERMER', command=fen.destroy)
bouton1.grid(row=6, column=2)

fen.mainloop()




