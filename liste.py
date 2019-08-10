import os

# Verifier le repertoire on est
rep_cour = os.getcwd()
print("Repertory: ")
print(rep_cour)

# Ecriture en mode append (ajout) du fichier Mon fichier
obfichier=open('Mon fichier', 'a')
obfichier.write('Il faut bien conprendre le programme Python.\n')
obfichier.write("C'est facile de programmer en Python\n")
obfichier.write("Il faut utiliser les fonctions en bien.\n")
obfichier.close()

# Lecture du fichier Mon fichier
obfichier=open('Mon fichier','r')
read=obfichier.read()
print(read)


