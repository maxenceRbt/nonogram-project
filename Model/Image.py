# Model/Image.py

from Model.CustomTypes import Image
from Model.Cellule import *
from Model.Position import *

#
# Gestion simple des nonograms
#
# Accès simple en lecture et en écriture à une "image"
# Création d'une "image"...
#


def type_image_light(img: Image) -> bool:
    """
    Permet de vérifier que le paramètre correspond à une image.
    Renvoie True si c'est le cas, False sinon.

    Version light : Ne vérifie pas le contenu des listes...

    :param img: Objet qu'on veut tester
    :return: True s'il correspond à une image, False sinon
    """
    if type(img) is not list:
        return False
    wrong = "Erreur !"
    if len(img) == 0:
        return False
    if type(img[0]) is not list:
        return False
    n_c = len(img[0])
    if n_c != len(img):
        return False
    if next((wrong for line in img if type(line) is not list or len(line) != n_c), True) == wrong:
        return False
    return True


def type_image_full(img: Image) -> bool:
    """
    Permet de vérifier que le paramètre correspond à une image.
    Renvoie True si c'est le cas, False sinon.

    En plus de la version light, vérifie que le contenu des listes correspond bien à une cellule.

    :param img: Objet qu'on veut tester
    :return: True s'il correspond à une image, False sinon
    """
    if not type_image_light(img):
        return False
    wrong = "Erreur !"
    if next((wrong for line in img for c in line if c is not None and not type_cellule(c)), True) == wrong:
        return False
    return True

#============== DEBUT DU CODE ============================

def getCellImage(image : Image, pos: Position) -> Cellule:
    """
    Fonction permettant d'obtenir la cellule de l'image à une position donnée

    :param image: liste 2D représentant l'image concernée
    :param pos: position concernée
    :return: Cellule de l'image
    """
    assert type_image_light(image) == True and type_position(pos) == True, "Le premier paramètre n'est pas une image ou le second n'est pas une position"
    Cell = image[pos[LIGNE]][pos[COLONNE]]
    return Cell

def setCellImage(image: Image, pos: Position, valeur: int|None) -> None:
    """
    Fonction permettant de déterminer une nouvelle couleur à la cellule d'une position donnée dans une image

    :param image: liste 2D représentant l'image concernée
    :param pos: position concernée
    :param valeur: entier représentant la nouvelle couleur
    :return:
    """
    assert type_image_light(image) == True and type_position(pos) == True and (type(valeur) == int or valeur is None), "Le premier paramètre n'est pas une image ou le second n'est pas une position ou le troisième n'est pas un entier"
    ligne = pos[LIGNE]
    colonne = pos[COLONNE]
    if valeur is not None:
        setCouleurCellule(image[ligne][colonne], valeur)
    else:
        setNonVuCellule(image[ligne][colonne])
    return None

def creerImage(taille : int, liste: list[list[int]] | None = None) -> Image:
    """
    Fonction permettant de créer une image avec une liste de valeur si donnée, ou alors avec "None", pour une taille donnée

    :param taille: dimension de l'image
    :param liste: liste 2D des valeurs à ajouter
    :return: l'image créée
    """
    assert type(taille) == int, "le premier paramètre n'est pas de type entier"
    assert taille >= 5 and taille <= 20, "le premier paramètre est infèrieur à 5 ou supérieur à 20"
    image = []
    if liste is not None:
        assert type_image_light(liste) == True
        assert len(liste) == taille
        for i in range(taille):
            lignes = []
            for j in range(taille):
                lignes.append({VALEUR:liste[i][j]})
            image.append(lignes)
    else:
        for i in range(taille):
            lignes = []
            for j in range(taille):
                lignes.append(construireCellule())
            image.append(lignes)
    return image

