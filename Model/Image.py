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


