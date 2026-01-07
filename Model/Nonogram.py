# Model/Nonogram.py
from Model.Bloc import COULEUR, construireBloc
from Model.Cellule import getCouleurCellule, isVideCellule
from Model.CustomTypes import ModelImage, LstBlocs
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
    :return: une list de liste des blocs pour chaque ligne
    :raise AssertionError: Si le paramètre n'est pas une image
    """
    assert type_image_light(image) == True, "le paramètre n'est pas une image"
    blocs = []
    for i in range(len(image)):
        blocLigne = compterBlocsSurLigne(image, i)
        blocs.append(blocLigne)
    return blocs

