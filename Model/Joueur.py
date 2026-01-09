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