__author__ = "François Audet"

import solution_v5
""" 
    Des modifications ont eu au lieu au niveau du code de base du professeurpour adapter avec le code mise au point
    avec 'solution_v5.py'.
"""


def affiche_croissant(arbre):
    noeud = arbre.min
    print("Ordre croissant :")
    while noeud != arbre.nil:
        print(noeud.k, end= ", ")
        noeud = noeud.succ
    print()

def affiche_decroissant(arbre):
    noeud = arbre.max
    print("Ordre decroissant :")
    while noeud != arbre.nil:
        print(noeud.k, end= ", ")
        noeud = noeud.pred
    print()

# Test du constructeur avec un tableau passe en argument
print("Test constructeur: Tableau(a) [4,7,12,15,3,5,14,18,16,17] ")
a = solution_v5.RN_arbre([4,7,12,15,3,5,14,18,16,17])
a.affiche()


print("\nrang 5: ", a.lire_rang(5).k)
print("rang 6: ", a.lire_rang(6).k)
print("rang 8: ", a.lire_rang(8).k)
print("rang 10: ", a.lire_rang(10).k)

print("rang de 3: ", a.determine_rang(3))
print("rang de 7: ", a.determine_rang(7))
print("rang de 14: ", a.determine_rang(14))
print("rang de 18: ", a.determine_rang(18))

affiche_croissant(a)
affiche_decroissant(a)

# suppression de 3, 12, 17, 18, 15, 16
a.supprimer(3)
a.affiche()

a.supprimer(12)
a.affiche()

affiche_croissant(a)
affiche_decroissant(a)

a.supprimer(17)
a.affiche()
a.supprimer(18)
a.affiche()
a.supprimer(15)
a.affiche()
a.supprimer(16)
a.affiche()

affiche_croissant(a)
affiche_decroissant(a)

#-------------------------------------------------------------------
print("\n\n--------------------------------------------------------")
print("Test constructeur: Tableau(b) [5,4,3,2,1,11,12,13,14,15] ")
b = solution_v5.RN_arbre([5,4,3,2,1,11,12,13,14,15])  # insertion avec affichage

b.affiche()

print("\nrang 5: ", b.lire_rang(8).k)
print("rang 4: ", b.lire_rang(4).k)
print("rang 3: ", b.lire_rang(10).k)
print("rang 2: ", b.lire_rang(6).k)

print("rang de 11: ", b.determine_rang(5))
print("rang de 12: ", b.determine_rang(4))
print("rang de 13: ", b.determine_rang(2))
print("rang de 14: ", b.determine_rang(14))
print("rang de 15: ", b.determine_rang(15))

#affiche_croissant(b)
#affiche_decroissant(b)

# suppression de 5, 3, 1, 4, 15, 13
b.supprimer(5)
b.affiche()

b.supprimer(3)
b.affiche()

affiche_croissant(b)
affiche_decroissant(b)

b.supprimer(1)
b.affiche()
b.supprimer(4)
b.affiche()
b.supprimer(15)
b.affiche()
b.supprimer(13)
b.affiche()

affiche_croissant(b)
affiche_decroissant(b)