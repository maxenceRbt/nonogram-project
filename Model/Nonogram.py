# Model/Nonogram.py
from Model.Bloc import *
from Model.Cellule import *
from Model.CustomTypes import ModelImage, LstBlocs, PlayerImage
from Model.Image import getCellImage, type_image_light
from Model.Joueur import *

def compterBlocsSurLigne(image: ModelImage, ligne: int = 0) -> LstBlocs:
    """
    Fonction permettant de compter les blocs sur la ligne

    :param image: image concernée
    :param ligne: ligne concernée
    :return: une liste des blocs sur la ligne
    :raise AssertionError: Si le premier paramètre n'est pas une image ou si le second n'est pas un entier
    """
    assert type_image_light(image) == True, "le premier paramètre n'est pas une image"
    assert type(ligne) == int, "le second paramètre n'est pas un entier"
    listeBlocs = []
    couleur = 0
    longueur = 0
    for cell in image[ligne]:
        couleurCell = getCouleurCellule(cell)
        if couleurCell != couleur:
            if couleur != 0:
                listeBlocs.append(construireBloc(longueur, couleur))
            couleur = couleurCell
            longueur = 1
        elif couleur != 0:
                longueur += 1
    if couleur != 0:
        listeBlocs.append(construireBloc(longueur, couleur))
    return listeBlocs

def getBlocsLignes(image: ModelImage) -> LstBlocs:
    """
    Fonction permettant d'obtenir les blocs pour chaque ligne d'une image donnée

    :param image: image concernée
    :return: une liste de liste des blocs pour chaque ligne
    :raise AssertionError: Si le paramètre n'est pas une image
    """
    assert type_image_light(image) == True, "le paramètre n'est pas une image"
    blocs = []
    for i in range(len(image)):
        blocLigne = compterBlocsSurLigne(image, i)
        blocs.append(blocLigne)
    return blocs

def compterBlocsSurColonne(image: ModelImage, colonne: int = 0) -> LstBlocs:
    """
    Fonction permettant de compter les blocs pour une colonne donnée, d'une image donnée

    :param image: image concernée
    :param colonne: colonne choisit
    :return: une liste des blocs sur la colonne
    :raise AssertionError: Si le premier paramètre n'est pas une image ou si le second n'est pas un entier
    """
    assert type_image_light(image) == True, "le premier paramètre n'est pas une image"
    assert type(colonne) == int, "le second paramètre n'est pas un entier"
    listeBlocs = []
    couleur = getCouleurCellule(image[0][colonne])
    longueur = 1
    for i in range(1, len(image)):
        couleurCell = getCouleurCellule(image[i][colonne])
        if couleurCell != couleur:
            if couleur != 0:
                listeBlocs.append(construireBloc(longueur, couleur))
            couleur = couleurCell
            longueur = 1
        else:
            if couleur != 0:
                longueur += 1
    if couleur != 0:
        listeBlocs.append(construireBloc(longueur, couleur))
    return listeBlocs

def getBlocsColonnes(image: ModelImage) -> LstBlocs:
    """
    Fonction permettant de compter les blocs sur chaque colonne d'une image donnée

    :param image: image concernée
    :return: Une liste de liste des blocs pour chaque colonne
    """
    assert type_image_light(image) == True, "Le paramètre n'est pas une image"
    blocs = []
    for j in range(len(image[0])):
        blocsColonne = compterBlocsSurColonne(image, j)
        blocs.append(blocsColonne)
    return blocs

def isVuImage(image: PlayerImage) -> bool:
    """
    Fonction permettant de savoir si toutes les cellules de l'image ont été découvertes par le joueur

    :param image: image du joueur
    :return: True si toutes les cellules sont découvertes, False sinon
    """
    vu = True
    i = 0
    while vu == True and i < len(image):
        j = 0
        while vu == True and j < len(image[i]):
            vu = isVuCellule(image[i][j])
            j += 1
        i += 1
    return vu

def reinitialiserImage(image: PlayerImage) -> None:
    """
    Fonction permettant de remettre toutes les cellules de l'image à l'état non-découvert

    :param image: image du joueur
    :return: None
    """
    for i in range(len(image)):
        for j in range(len(image[i])):
            setNonVuCellule(image[i][j])
    return None

def verifierBlocsLigneImage(image: PlayerImage, listeBloc: LstBlocs, ligne: int = 0) -> bool:
    """
    Fonction permettant de vérifier si les blocs sur une ligne donnée d'une image ont été découvert à gauche et à droite

    :param image: image du joueur
    :param listeBloc: liste des blocs
    :param ligne: ligne concernée
    :return: True si les blocs ont été découvert, False sinon
    """
    taille_ligne = len(image[ligne])
    etatModif = False
    idxCell = 0
    idxBloc = 0
    vu = True
    while vu and idxCell < taille_ligne and idxBloc < len(listeBloc):
        cell = image[ligne][idxCell]
        if not isVuCellule(cell):
            vu = False
        else:
            couleur = getCouleurCellule(cell)
            if couleur == 0:
                idxCell += 1
            else :
                bloc = listeBloc[idxBloc]
                if getCouleurBloc(bloc)  != couleur:
                    vu = False
                else :
                    taille = getNombreBloc(bloc)
                    complet = True
                    if idxCell + taille > taille_ligne:
                        complet = False
                    j = 0
                    while j < taille and complet:
                        if not isVuCellule(image[ligne][idxCell+j]) or getCouleurCellule(image[ligne][idxCell+j]) != couleur:
                            complet = False
                        j += 1
                    if complet:
                        if not isVuBloc(bloc):
                            setVuBloc(bloc, True)
                            etatModif = True
                        idxCell += taille
                        idxBloc += 1
                    else:
                        vu = False

    idxCell = taille_ligne - 1
    idxBloc = len(listeBloc) - 1
    vu = True
    while vu and idxCell >= 0 and idxBloc >= 0:
        cell = image[ligne][idxCell]
        if not isVuCellule(cell):
            vu = False
        else:
            couleur = getCouleurCellule(cell)
            if couleur == 0:
                idxCell -= 1
            else:
                bloc = listeBloc[idxBloc]
                if getCouleurBloc(bloc) != couleur:
                    vu = False
                else:
                    taille = getNombreBloc(bloc)
                    complet = True

                    if idxCell - taille + 1 < 0:
                        complet = False
                    j = 0
                    while j < taille and complet:
                        if not isVuCellule(image[ligne][idxCell-j]) or getCouleurCellule(image[ligne][idxCell-j]) != couleur:
                            complet = False
                        j += 1
                    if complet:
                        if not isVuBloc(bloc):
                            setVuBloc(bloc, True)
                            etatModif = True
                        idxCell -= taille
                        idxBloc -= 1
                    else:
                        vu = False
    return etatModif



def verifierBlocsColonneImage(image: PlayerImage, listeBloc: LstBlocs, colonne: int = 0) -> bool:
    """
    Fonction permettant de vérifier si les blocs sur une colonne donnée d'une image ont été découvert en haut et en bas

    :param image: image du joueur
    :param listeBloc: liste des blocs
    :param ligne: ligne concernée
    :return: True si les blocs ont été découvert, False sinon
    """
    taille_Col = len(image)
    etatModif = False
    idxCell = 0
    idxBloc = 0
    vu = True

    while vu and idxCell < taille_Col and idxBloc < len(listeBloc):
        cell = image[idxCell][colonne]
        if not isVuCellule(cell):
            vu = False
        else:
            couleur = getCouleurCellule(cell)
            if couleur == 0:
                idxCell += 1
            else:
                bloc = listeBloc[idxBloc]
                if getCouleurBloc(bloc) != couleur:
                    vu = False
                else:
                    taille = getNombreBloc(bloc)
                    complet = True
                    if idxCell + taille > taille_Col:
                        complet = False
                    j = 0
                    while j < taille and complet:
                        if not isVuCellule(image[idxCell+j][colonne]) or getCouleurCellule(image[idxCell+j][colonne]) != couleur:
                            complet = False
                        j += 1
                    if complet:
                        if not isVuBloc(bloc):
                            setVuBloc(bloc, True)
                            etatModif = True
                        idxCell += taille
                        idxBloc += 1
                    else:
                        vu = False
    idxcell = taille_Col - 1
    idxBloc = len(listeBloc) - 1
    vu = True
    while vu and idxcell >= 0 and idxBloc >= 0:
        cell = image[idxcell][colonne]
        if not isVuCellule(cell):
            vu = False
        else:
            couleur = getCouleurCellule(cell)
            if couleur == 0:
                idxcell -= 1
            else:
                bloc = listeBloc[idxBloc]
                if getCouleurBloc(bloc) != couleur:
                    vu = False
                else:
                    taille = getNombreBloc(bloc)
                    complet = True
                    if idxCell - taille + 1 < 0:
                        complet = False
                    j = 0
                    while j < taille and complet and idxCell < 0:
                        if not isVuCellule(image[idxCell - j][colonne]) or getCouleurCellule(image[idxCell - j][colonne]) != couleur:
                            complet = False
                        j += 1
                    if complet:
                        if not isVuBloc(bloc):
                            setVuBloc(bloc, True)
                            etatModif = True
                        idxCell -= taille
                        idxBloc -= 1
                    else:
                        vu = False
    return etatModif


def isLigneDecouverteImage(image: PlayerImage, listeBloc: LstBlocs, ligne: int = 0) -> bool:
    vu = True
    idxBloc = 0
    while idxBloc < len(listeBloc) and vu:
        if not isVuBloc(listeBloc[idxBloc]):
            vu = False
        else:
            idxBloc += 1
    return vu


def getCellsNonVuesLigneImage(image: PlayerImage, ligne: int) -> LstBlocs:
    nonVu = []
    pos = construirePosition()
    setLignePosition(pos, ligne)
    for i in range(len(image[ligne])):
        setColonnePosition(pos, i)
        if not isVuCellJoueur(image, pos):
            nonVu.append(i)
    return nonVu