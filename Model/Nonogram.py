# Model/Nonogram.py
from Model.Bloc import *
from Model.Cellule import getCouleurCellule, isVideCellule, isVuCellule, setNonVuCellule
from Model.CustomTypes import ModelImage, LstBlocs, PlayerImage
from Model.Image import getCellImage, type_image_light


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
    print(image)
    while vu == True and i < len(image):
        j = 0
        while vu == True and j < len(image[i]):
            print(image[i][j])
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