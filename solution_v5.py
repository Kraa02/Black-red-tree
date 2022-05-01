__author__ = 'Ilfrane CHERY', 'KRAIEM Amine', 'MWELLE OLLE WILLIAMS Otto James', 'LO Mohamed'

Rouge = 'Rouge'
Noir = 'Noir'

"""
    Note !!!: ERROR["NoneType object has no attribute"]
    Lors de l'exécution du code une erreur surgie de nulle part de type "NoneType object has no attribute".
    Des conditions ont été mises en place pour éviter que le problème ne se reproduise.
"""

##Definition de la classe noeud et caractéristiques du contructeur:
# Clé(k), Couleur(c),parent(p), gauche(g), droite(d), taille(t), pred(prédécesseur), succ(Succésseur)
class Noeud:
    def __init__(self, cle, color=Rouge, parent=None, gauche=None, droite=None, pred = None, succ = None):
        self.k = cle                                    # k: Clé du noeud
        self.p = parent                                 # p: parent du noeud
        self.g = gauche                                 # g: Enfant à gauche du parent(p)
        self.d = droite                                 # d: Enfant à droite du parent(p)
        self.c = color                                  # c: Couleur 'Noir' choisit par défaut comme décrit dans le bouquin.

        # Condiions: Voir note au dessus du code
        if (self.g is None) and (self.d is None):
            self.t = 1
        elif self.g is None and self.d is not None:
            self.t = self.d.t + 1
        elif self.d is None and self.g is not None:
            self.t = self.g.t + 1
        else:
            self.t = self.g.t + self.d.t + 1
        if self is None:
            self.t = 0
        self.pred = pred
        self.succ = succ

    # Affichage de noeud en référent au modèle utilisé dans le cours.
    def __str__(self):
        if (self == None):
            return "Nil"
        if (self.g == None and self.d == None):
            return "({}{} g:Nil d:Nil t:{})".format(self.k, self.c, self.t)
        elif self.g == None:
            return "({}{} g:Nil d:{} t:{})".format(self.k, self.c, self.d.k, self.t)
        elif self.d == None:
            return "({}{} g:{} d:Nil t:{})".format(self.k, self.c, self.g.k, self.t)
        else:
            return "({}{} g:{} d:{} t:{})".format(self.k, self.c, self.g.k, self.d.k, self.t)

# Définition classe implémentation arbre de recherche binaire Rouge-Noir
class RN_arbre:
    #Implémentaion du constructeur et initialisation de la racine de l'arbre ainsi que ses paramètres
    def __init__(self, T):
        self.nil = Noeud("Nil", Noir)
        self.nil.t = 0
        self.racine = self.nil
        self.min = self.nil
        self.max = self.nil
        for i in range (0, len(T)):
            self.arbre_inserer(Noeud(T[i], Noir, self.nil, self.nil, self.nil, self.nil, self.nil))


    # Définition de la fonction trouve_noeud: Retourne une clé(k) équivalent à i.
    def trouve_noeud(self, i):
        x = self.racine
        while x != self.nil and i != x.k:
            if i < x.k:
                x = x.g
            else:
                x = x.d
        return x

    ## Définition de la fonction arbre_inserer: Vérifie si k est un noeud pour effectuer une insertion [Reférence bouqin cours]
    """ Note:
        Une incrémentation se fera au fur et à mesure pour remplir les conditions de vérification avant de déterminer le noeud qui devra
        considérer comme racine de l'arbre. Pour ce faire l'arbre devra être vide en premier lieu pour que cette thérie tient route.
        Par la suite, les attributs succ, pred et les propriétés de la méthode insérer_correction_rn seront rétablit.
    """
    def arbre_inserer(self, i):
        if type(i) == int:
            self.arbre_inserer(Noeud(i, Noir, self.nil, self.nil, self.nil, self.nil, self.nil))
        else:
            y = self.nil
            x = self.racine
            while x != self.nil:
                x.t += 1    # Incrémentation
                y = x
                if i.k < x.k:
                    x = x.g
                else:
                    x = x.d
            i.p = y
            if y == self.nil:
                self.racine = i
            elif i.k < y.k:
                y.g = i
            else:
                y.d = i
            i.g = self.nil
            i.d = self.nil
            i.c = Rouge
            self.ajout_pred_succ(i)
            self.inserer_correction_rn(i)

    # Définition de la méthode de correction de couleur.
    """ Une procédure de correction de couleur se fera à ce niveau comme le décrit le livre.
        Un réagencement au niveau des couleurs aura lieu pour remettre de l'ordre là ou les couleurs ne semble pas correcte.
        Les conditions au point feront un tri par cas et ainsi répertorier la bonne couleur.
    """
    def inserer_correction_rn(self, z):
        while z.p.c == Rouge:
            if z.p == z.p.p.g:
                y = z.p.p.d
                if y.c == Rouge:
                    z.p.c = Noir
                    y.c = Noir
                    z.p.p.c = Rouge
                    z = z.p.p
                else:
                    if z == z.p.d:
                        z = z.p
                        self.rotation_gauche(z)
                    z.p.c = Noir
                    z.p.p.c = Rouge
                    self.rotation_droite(z.p.p)
            else:
                y = z.p.p.g
                if y.c == Rouge:
                    z.p.c = Noir
                    y.c = Noir
                    z.p.p.c = Rouge
                    z = z.p.p
                else:
                    if z == z.p.g:
                        z = z.p
                        self.rotation_droite(z)
                    z.p.c = Noir
                    z.p.p.c = Rouge
                    self.rotation_gauche(z.p.p)
        self.racine.c = Noir

    # Définition des fonctions:
    # 1) transplante_rn: Remplacement du sous-arbre du noeud u par le celui du noeud v.
    # 2) arbre_min: Retour la valeur minimale du sous-arbre
    # 3) supprime_rn: Effectue la suppression de k(i)
    # 4) supprimer_correction_rn: Correction de l'arbre après suppression de clé
    # 5) lire_rang: Retourne un élément de rang i dans l'arbre
    # 6) determine_rang : Retourne range de l'élément i
    # 7) rotation_gauche: Rotaion à gauche en x
    # 8) rotation_droite: Rotaion à gauche en x
    # 9) ajout_preced_succ: Rétablissement condition des attibuts prec et succ après ajout
    # 10) upprime_pred_succ: Rétablissement condition des attibuts prec et succ après suppression

    def transplante_rn(self, u, v):
        if u.p == self.nil:
            self.racine = v
        elif u == u.p.g:
            u.p.g = v
        else:
            u.p.d = v
        v.p = u.p

    def arbre_minimum(self, x):
        while x.g != self.nil:
            x = x.g
        return x


    def supprimer(self,i):
        z = self.trouve_noeud(i)
        if z == self.nil:
            print("Noeud non disponible avec k {} dans l'arbre.".format(i))
            return
        y = z
        print("Suppression noeud: k " + str(z.k))
        y_original_color = y.c
        if z.g == self.nil:
            x = z.d
            self.transplante_rn(z, z.d)
        elif z.d == self.nil:
            x = z.g
            self.transplante_rn(z, z.g)
        else:
            y = self.arbre_minimum(z.d)
            y_original_color = y.c
            x = y.d
            if y.p == z:
                x.p = y
            else:
                self.transplante_rn(y, y.d)
                y.d = z.d
                y.d.p = y
            self.transplante_rn(z, y)
            y.g = z.g
            y.g.p = y
            y.c = z.c
        size_path = y
        while size_path != self.racine:
            size_path.t -= 1
            size_path = size_path.p
        self.racine.t -= 1
        self.supprime_pred_succ(z)
        if y_original_color == Noir:
            self.supprimer_correction_rn(x)

    def supprimer_correction_rn(self, x):
        while x != self.racine and x.c == Noir:
            if x == x.p.g:
                w = x.p.d
                if w.c == Rouge:
                    w.c = Noir
                    x.p.c = Rouge
                    self.rotation_gauche(x.p)
                    w = x.p.d
                if w.g.c == Noir and w.d.c == Noir:
                    w.c = Rouge
                    x = x.p
                else:
                    if w.d.c == Noir:
                        w.g.c = Noir
                        w.c = Rouge
                        self.rotation_droite(w)
                        w = x.p.d
                    w.c = x.p.c
                    x.p.c = Noir
                    w.d.c = Noir
                    self.rotation_gauche(x.p)
                    x = self.racine
            else:
                w = x.p.g
                if w.c == Rouge:
                    w.c = Noir
                    x.p.c = Rouge
                    self.rotation_droite(x.p)
                    w = x.p.g
                if w.d.c == Noir and w.g.c == Noir:
                    w.c = Rouge
                    x = x.p
                else:
                    if w.g.c == Noir:
                        w.d.c = Noir
                        w.c = Rouge
                        self.rotation_gauche(w)
                        w = x.p.g
                    w.c = x.p.c
                    x.p.c = Noir
                    w.g.c = Noir
                    self.rotation_droite(x.p)
                    x = self.racine
        x.c = Noir

    def lire_rang(self,i):
        x = self.racine
        if x is None:
            print("Tableau vide")
            return
        r = x.g.t + 1
        # print("avant le while: " + str(r))
        while i != r:
            if i < r:
                x = x.g
                #  print("iteration. i < r. x = x.g  x = " + str(x))
                r = x.g.t + 1
            #  print("r = " + str(r) + " i = " + str(i))
            else:
                x = x.d
                # print("iteration. i >= r. x = x.d  x = " + str(x))
                i = i - r
                r = x.g.t + 1
            # print("r = " + str(r) + " i = " + str(i))
        return x

    def determine_rang(self, i):
        x = self.trouve_noeud(i)
        r = x.g.t + 1
        y = x
        while y != self.racine:
            if y == y.p.d:
                r = r + y.p.g.t + 1
            y = y.p
        return r

    def rotation_gauche(self, x):

        y = x.d
        x.d = y.g
        if y.g != self.nil:
            y.g.p = x
        y.p = x.p
        if x.p == self.nil:
            self.racine = y
        elif x == x.p.g:
            x.p.g = y
        else:
            x.p.d = y
        y.g = x
        x.p = y
        y.t = x.t
        x.t = x.g.t + x.d.t + 1

    def rotation_droite(self, x):
        y = x.g #definit y
        x.g = y.d
        if y.d != self.nil:
            y.d.p = x
        y.p = x.p
        if x.p == self.nil:
            self.racine = y
        elif x == x.p.d:
            x.p.d = y
        else:
            x.p.g = y
        y.d = x
        x.p = y
        y.t = x.t
        x.t = x.g.t + x.d.t + 1

    def ajout_pred_succ(self, x):
        if x == self.racine:
            self.min = x
            self.max = x
            return
        if x == x.p.g:
            if x.p.pred == self.nil:
                self.min = x
            else:
                x.p.pred.succ = x
            x.pred = x.p.pred
            x.p.pred = x
            x.succ = x.p
        else:   # symetrique
            if x.p.succ == self.nil:
                self.max = x
            else:
                x.p.succ.pred = x
            x.succ = x.p.succ
            x.p.succ = x
            x.pred = x.p

    def supprime_pred_succ(self, x):
        if x == self.racine:
            return
        if self.max == x:
            self.max = x.pred
            x.pred.succ = self.nil
        elif self.min == x:
            self.min = x.succ
            x.succ.pred = self.nil
        else:
            x.succ.pred = x.pred
            x.pred.succ = x.succ


    def parcours_infixe(self,x):
        if x != None:
            self.parcours_infixe(x.g)
            if x.k != "Nil":
                print(x)
            self.parcours_infixe(x.d)


    def affiche(self):
        print("Affichage arbre:")
        self.parcours_infixe(self.racine)
        print()

