# Model/Joueur.py

from Model.CustomTypes import *
from Model.Image import *
from Model.Cellule import *
from Model.Bloc import *
from Model.Suggestion import *
from Model.Nonogram import *
from Model.Position import *


def isVuCellJoueur(image: PlayerImage, pos: Position) -> bool:
    """
    Fonction permettant de savoir si la cellule sélectionnée par le joueur a déjà été découverte

    :param image: image du joueur
    :param pos: position de la cellule
    :return: True si la cellule a déjà été découverte, False sinon
    """
    decouv = False
    cell = getCellImage(image, pos)
    if isVuCellule(cell) == True:
        decouv = True
    return decouv

def isCouleurCorrecteImage(image: ModelImage, pos: Position, couleur: int) -> bool:
    """
    Fonction permettant de savoir si la couleur choisit par le joueur est correcte

    :param image: image à trouver
    :param pos: position de la cellule sélectionnée
    :param couleur: couleur choisit par le joueur
    :return: True si la couleur est correcte, False sinon
    """
    cell = getCellImage(image, pos)
    couleurCorrecte = getCouleurCellule(cell)
    bonneCouleur = False
    if couleur == couleurCorrecte:
        bonneCouleur = True
    return bonneCouleur

def isLigneNonVueImage(image: PlayerImage, ligne: int = 0) -> bool:
    """
    Fonction permettant de déterminer si la ligne donnée en paramètre a été découverte ou non

    :param image: image du joueur
    :param ligne: ligne choisit
    :return: True si non Découverte, False sinon
    """
    nonVue = True
    col = 0
    while col < len(image[ligne]) and nonVue:
            cellule = image[ligne][col]
            if isVuCellule(cellule):
                nonVue = False
            else:
                col += 1
    return nonVue

def isColonneNonVueImage(image: PlayerImage, col: int = 0) -> bool:
    """
    Fonction permettant de déterminer si la colonne donnée en paramètre a été découverte ou non

    :param image: image du joueur
    :param col: colonne choisit
    :return: True si non Découverte, False sinon
    """
    nonVue = True
    ligne = 0
    while ligne <len(image) and nonVue:
        cellule = image[ligne][col]
        if isVuCellule(cellule):
            nonVue = False
        else:
            ligne += 1
    return nonVue


def appliquerMonoRecouvrementLigne(image: PlayerImage, ligne: int, blocs: LstBlocs) -> LstSuggestions:
    """
    Fonction permettant d'obtenir une liste de suggestion pour une ligne donnée en appliquant le principe de recouvrement

    :param image: image du joueur
    :param ligne: ligne choisit
    :param blocs: liste des blocs de la ligne
    :return: une liste des suggestions
    """
    suggestions = []
    if isLigneNonVueImage(image, ligne):
        nb_colonnes = len(image[ligne])
        positionsDebut = []
        cumulDeb = 0
        i = 0
        while i < len(blocs):
            positionsDebut.append(cumulDeb)
            cumulDeb += getNombreBloc(blocs[i]) + 1
            i += 1
        positionsFin = []
        cumulFin = nb_colonnes
        i = len(blocs) - 1
        while i >= 0:
            taille = getNombreBloc(blocs[i])
            cumulFin -= taille
            positionsFin.append(cumulFin)
            cumulFin -= 1
            i -= 1
        i = 0
        while i < len(blocs):
            gauche = positionsDebut[i]
            droite = positionsFin[i]
            taille = getNombreBloc(blocs[i])
            couleur = getCouleurBloc(blocs[i])
            col = droite
            while col < gauche + taille:
                pos = construirePosition()
                setLignePosition(pos, ligne)
                setColonnePosition(pos, col)
                if not isVuCellJoueur(image, pos):
                    suggestions.append(construireSuggestion(pos, couleur))
                col += 1
            i += 1
    return suggestions


def appliquerMonoRecouvrementColonne(image: PlayerImage, colonne: int, blocs: LstBlocs) -> LstSuggestions:
    """
    Fonction permettant d'obtenir une liste de suggestion pour une colonne donnée en appliquant le principe de recouvrement

    :param image: image du joueur
    :param col: colonne choisit
    :param blocs: liste des blocs de la ligne
    :return: une liste des suggestions
    """
    suggestions = []
    if isColonneNonVueImage(image, colonne):
        nb_lignes = len(image)
        positionsDebut= []
        cumulDeb = 0
        i = 0
        while i < len(blocs):
            positionsDebut.append(cumulDeb)
            cumulDeb += getNombreBloc(blocs[i]) + 1
            i += 1
        positionsFin = []
        cumulFin = nb_lignes
        i = len(blocs) - 1
        while i >= 0:
            taille = getNombreBloc(blocs[i])
            cumulFin -= taille
            positionsFin.insert(0, cumulFin)
            cumulFin -= 1
            i -= 1
        i = 0
        while i < len(blocs):
            gauche = positionsDebut[i]
            droite = positionsFin[i]
            taille = getNombreBloc(blocs[i])
            couleur = getCouleurBloc(blocs[i])
            ligne = droite
            while ligne < gauche + taille:
                # Création de la position (Ligne variable, Colonne fixe)
                pos = construirePosition()
                setLignePosition(pos, ligne)
                setColonnePosition(pos, colonne)

                # On ajoute la suggestion si la cellule n'est pas déjà découverte
                if not isVuCellJoueur(image, pos):
                    suggestions.append(construireSuggestion(pos, couleur))
                ligne += 1
            i += 1
    return suggestions


def appliquerMonoRecouvrement(image: PlayerImage, blocsLignes: LstLstBlocs, blocsColonnes: LstLstBlocs) -> LstSuggestions:
    """
    Fonction permettant d'appliquer le principe de recouvrement sur chaque ligne et colonne d'une image pour obtenir une liste de suggestions

    :param image: image du joueur
    :param blocsLignes: liste des blocs de chaque ligne
    :param blocsColonnes: liste des blocs de chaque colonne
    :return: une liste des suggestions de l'image
    """
    suggestionsTotal = []
    taille = len(image)
    i = 0
    while i < taille:
        suggestions_ligne = appliquerMonoRecouvrementLigne(image, i, blocsLignes[i])
        k = 0
        while k < len(suggestions_ligne):
            suggestionsTotal.append(suggestions_ligne[k])
            k += 1
        i += 1
    j = 0
    while j < taille:
        suggestions_colonne = appliquerMonoRecouvrementColonne(image, j, blocsColonnes[j])
        k = 0
        while k < len(suggestions_colonne):
            suggestionsTotal.append(suggestions_colonne[k])
            k += 1
        j += 1
    return suggestionsTotal


def isRangeeVide(rangee: Rangee) -> bool:
    """
    Fonction permettant de déterminer si une rangée est vide

    :param rangee: rangee choisit
    :return: True si la rangee est vide, False sinon
    """
    vide = True
    i = 0
    # On parcourt la rangée tant qu'on n'a pas trouvé de cellule vue
    while i < len(rangee) and vide:
        if isVuCellule(rangee[i]):
            vide = False
        i += 1

    return vide

def isRangeeDecouverte(rangee: Rangee) -> bool:
    """
    Fonction permettant de savoir si une rangee est découverte

    :param rangee: rangee concernée
    :return: True si la rangee est découverte, False sinon
    """
    vu = True
    i = 0
    while isVuCellule(rangee[i]) and i < len(rangee):
        i += 1
    if not isVuCellule(rangee[i]):
        vu = False
    return vu


def appliquerMonoGlueBordRangee(rangee: Rangee, blocs: LstBlocs) -> LstIndexCouleurs:
    """
    Fonction appliquant le principe de glue des bords sur une rangee donnée

    :param rangee: rangee concernée
    :param blocs: liste des blocs de la rangee
    :return: une liste de tuple avec l'index et couleurs des suggestions trouvées
    """
    suggestions = []
    if len(blocs) > 0 and not isRangeeVide(rangee) and not isRangeeDecouverte(rangee):
        i = 0
        cellVu = False
        while i < len(rangee) and not cellVu:
            if isVuCellule(rangee[i]):
                cellVu = True
            else:
                i += 1
        if cellVu:
            celluleVue = rangee[i]
            premierBloc = blocs[0]
            tailleBloc = getNombreBloc(premierBloc)
            couleurBloc = getCouleurBloc(premierBloc)
            if getCouleurCellule(celluleVue) != 0 and i < tailleBloc:
                k = 0
                while k < tailleBloc:
                    if not isVuCellule(rangee[k]):
                        suggestions.append((k, couleurBloc))
                    k += 1
                if tailleBloc < len(rangee):
                    if not isVuCellule(rangee[tailleBloc]):
                        suggestions.append((tailleBloc, 0))
    return suggestions

def indexCouleursToSuggestions(indexCouleurs: LstIndexCouleurs, ligCol: int, isLigne: bool) -> LstSuggestions:
    """
    Fonction permettant de construire une liste de suggestions à partir d'une liste de tuple d'index et couleurs

    :param indexCouleurs: liste d'index
    :param ligCol: numéro de ligne / colonne
    :param isLigne: Savoir si ligCol concerne une ligne ou non
    :return: une liste de suggestions avec leurs positions
    """
    suggestions = []
    position = construirePosition()
    if isLigne:
        ligne = ligCol
        setLignePosition(position, ligne)
        for i in range(len(indexCouleurs)):
            setColonnePosition(position, indexCouleurs[i][0])
            suggestions.append(construireSuggestion(position, indexCouleurs[i][1]))
    else:
        col = ligCol
        setColonnePosition(position, col)
        for i in range(len(indexCouleurs)):
            setLignePosition(position, indexCouleurs[i][0])
            suggestions.append(construireSuggestion(position, indexCouleurs[i][1]))
    return suggestions

def getLigneImage(image: PlayerImage, li: int) -> Rangee:
    """
    Fonction permettant d'obtenir la rangée d'une ligne donnée dans une image

    :param image: image du joueur
    :param li: ligne choisit
    :return: la rangée de la ligne choisit
    """
    ligneImage = image[li]
    return ligneImage

def getLigneInverseImage(image: PlayerImage, li: int) -> Rangee:
    """
    Fonction permettant d'inverser la rangée d'une ligne dans une image

    :param image: image du joueur
    :param li: ligne choisit
    :return: la rangée inversée
    """
    ligneImage = image[li]
    ligneImage.reverse()
    return ligneImage

def getLstBlocsInverse(blocs: LstBlocs) -> LstBlocs:
    """
    Fonction permettant d'obtenir l'inverse d'une liste de blocs

    :param blocs: liste de blocs choisit
    :return: une liste de blocs étant l'inverse de la liste passée en paramètre
    """
    listeBlocs = blocs
    listeBlocs.reverse()
    return listeBlocs

def getColonneImage(image: PlayerImage, co: int) -> Rangee:
    """
    Fonction permettant d'obtenir la rangee de la colonne passé en paramètre dans une image

    :param image: image du joueur
    :param co: colonne choisit
    :return: la rangee de la colonne
    """
    colonne = []
    for i in range(len(image)):
        colonne.append(image[i][co])
    return colonne

def getColonneInverseImage(image: PlayerImage, co: int) -> Rangee:
    """
    Fonction permettant d'obtenir l'inverse de la rangee d'une colonne choisit

    :param image: image du joueur
    :param co: colonne choisit
    :return: la rangee inversée de la colonne
    """
    colonne = getColonneImage(image, co)
    colonne.reverse()
    return colonne

def getIndexInverseDeIndexCouleurs(idx_color: LstIndexCouleurs, dim: int) -> LstIndexCouleurs:
    """
    Fonction permettant d'obtenir une liste d'index et couleurs avec les index étant inversés en fonction de la dimension de l'image

    :param idx_color: liste de tuple (index, couleurs)
    :param dim: dimension de l'image
    :return: liste de tuple (index, couleurs) avec les nouveaux index
    """
    indexCouleursInv = []
    i = 0
    while i < len(idx_color):
        indexInverse = idx_color[i][0]
        couleur = idx_color[i][1]
        indexReel = (dim - 1) - indexInverse
        indexCouleursInv.append((indexReel, couleur))
        i += 1
    return indexCouleursInv


def appliquerMonoGlueBord(image: PlayerImage, blocsLignes: LstLstBlocs, blocsColonnes: LstLstBlocs) -> LstSuggestions:
    """
    Fonction permettant d'appliquer la technique Glue sur les bords pour les lignes, les lignes retournées, les colonnes et les colonnes retournées
    et d'obtenir une liste de suggestions sur toute l'image du joueur

    :param image: image du joueur
    :param blocsLignes: une liste avec les listes de chaque bloc de chaque ligne
    :param blocsColonnes: une liste avec les listes de chaque bloc de chaque colonne
    :return: une liste de suggestions sur l'ensemble de l'image
    """
    suggestions = []
    nbrLignes = len(image)
    nbrColonnes = len(image[0])
    ligne = 0
    while ligne < nbrLignes:
        blocsLigne = blocsLignes[ligne]
        rangeeDeb= getLigneImage(image, ligne)
        glueDeb = appliquerMonoGlueBordRangee(rangeeDeb, blocsLigne)
        j = 0
        while j < len(glueDeb):
            pos = construirePosition()
            setLignePosition(pos, ligne)
            setColonnePosition(pos, glueDeb[j][0])
            suggestions.append(construireSuggestion(pos, glueDeb[j][1]))
            j += 1

        rangeeFin = getLigneInverseImage(image, ligne)
        blocsInv = getLstBlocsInverse(blocsLigne)
        glueFinInverse = appliquerMonoGlueBordRangee(rangeeFin, blocsInv)
        glueFin = getIndexInverseDeIndexCouleurs(glueFinInverse, nbrColonnes)
        j = 0
        while j <len(glueFin):
            pos = construirePosition()
            setLignePosition(pos, ligne)
            setColonnePosition(pos, glueFin[j][0])
            suggestions.append(construireSuggestion(pos, glueFin[j][1]))
            j += 1
        ligne += 1
    col = 0
    while col < nbrColonnes:
        blocsColonne = blocsColonnes[col]
        rangeHaut = getColonneImage(image, col)
        glueHaut = appliquerMonoGlueBordRangee(rangeHaut, blocsColonne)
        j = 0
        while j < len(glueHaut):
            pos = construirePosition()
            setColonnePosition(pos, col)
            setLignePosition(pos, glueHaut[j][0])
            suggestions.append(construireSuggestion(pos, glueHaut[j][1]))
            j += 1

        rangeBasInv = getColonneInverseImage(image, col)
        blocsInv = getLstBlocsInverse(blocsColonne)
        glueBasInv = appliquerMonoGlueBordRangee(rangeBasInv, blocsInv)
        glueBas = getIndexInverseDeIndexCouleurs(glueBasInv, nbrLignes)
        j = 0
        while j < len(glueBas):
            pos = construirePosition()
            setColonnePosition(pos, col)
            setLignePosition(pos, glueBas[j][0])
            suggestions.append(construireSuggestion(pos, glueBas[j][1]))
            j += 1
        col += 1
    return suggestions