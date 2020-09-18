# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np

#code RVB des couleurs présentent sur l'image finale
bleu = [31,19,180]
orange = [255,127,14]
vert = [44,160,44]

#liste des différentes positions que doit prendre le "T" orange
orangeChemin = np.array([
                [(1,0),(1,1),(2,1),(1,2)],
                [(1,1),(2,1),(3,1),(2,2)],
                [(1,2),(2,2),(3,2),(2,3)]])

    
#Créer un carré de la couleur en paramètredans la mtarice passé en paramètre, à la position (x,y) passée en paramètre
def carre(matrice, couleur, position):
    x = position[0] * 50 
    y = position[1] * 50
    matrice[y:y+50,x:x+50,:] = couleur
    
    
#Fonction permetttant de créer des formes carrées en fournissant une liste de coodonnées pour chaques carrés
def forme(matrice, chemin, couleur):
    for t in chemin:
        carre(matrice,couleur,t)

    
#assigne les modification d'image de chaque étapes, à la matrice passée en paramètre
def afficher(matrice,i):
    #fond gris
    matrice[:,:,:] = [127,127,127]
    #ligne bleue à gauche
    forme(render,[(0,0),(0,1),(0,2),(0,3)],bleu)
    forme(render,orangeChemin[i],orange)
    forme(render,[(3,3),(4,3),(4,2),(5,2)],vert)



#sélection de l'étape souhaitée
render = np.zeros((200,300,3), dtype=np.uint8)
choix = int(input("Saisir l'etape souhaitee ou 0 pour sortir: "));
while choix != 0:
    afficher(render,choix-1)
    plt.imshow(render)
    plt.show()
    choix = int(input("Saisir l'etape souhaitee ou 0 pour sortir: "))

print("Aurevoir, à la prochaine !")