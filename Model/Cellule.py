# Model/Cellule.py
#

from Model.debug import debug
from Model.CustomTypes import Cellule

# Clé contenant la valeur d'une cellule
VALEUR = "value"

#
# La Cellule
#
# L'objet cellule va représenter une case de l'image (du nonogram)
#
# La cellule sera représentée par un dictionnaire.
# Une cellule pourra être :
#   - vide (absence de bille) : La valeur sera 0.
#   - non découverte (non connue) : la valeur sera None.
#   - une couleur (ou plutôt l'indice non nul d'une couleur, la palette sera fournie plus tard).
#



def type_cellule(cell: Cellule) -> bool:
    """
    Permet de vérifier si l'argument peut correspondre ou non à une cellule

    :param cell: Objet dont on veut tester le type
    :return: True s'il s'agit d'une cellule, False sinon.
    """
    if type(cell) is not dict:
        debug(f"La cellule {cell} n'est pas un dictionnaire")
        return False
    if VALEUR not in cell:
        debug(f"La clé VALUE ({VALEUR}) n'est pas dans le dictionnaire")
        return False
    if cell[VALEUR] is not None and type(cell[VALEUR]) is not int:
        debug(f"La valeur {cell[VALEUR]} n'est ni entière ni None ")
        return False
    return True


#=============== DEBUT DU CODE ===================================

def construireCellule() -> Cellule:
    """
    Construction d'une cellule non "découverte"

    :return: Dictionnaire représentant une cellule
    """
    Cellule = {VALEUR: None}
    return Cellule

def isVuCellule(cell: Cellule) -> bool:
    """
    Fonction permettant de vérifier si la cellule est bien découverte

    :param cell: cellule concernée
    :return: True s'il s'agit d'une cellule découverte, False sinon.
    :raise AssertionError: Si le paramètre n'est pas une cellule
    """
    test = False
    assert type_cellule(cell) == True, "La cellule n'est pas une cellule"
    if cell[VALEUR] != None:
        test = True
    return test

def isVideCellule(cell: Cellule) -> bool:
    """
    Fonction permettant de vérifier si la cellule est vide

    :param cell: cellule concernée
    :return: True si la cellule est vide, False sinon
    :raise AssertionError: Si le paramètre n'est pas une cellule
    """
    test = False
    assert type_cellule(cell) == True, "La cellule n'est pas une cellule"
    if cell[VALEUR] == 0:
        test = True
    return test

def getCouleurCellule(cell: Cellule) -> int:
    """
    Fonction permettant d'obtenir la valeur de la couleur de la cellule

    :param cell: cellule concernée
    :return: l'entier représentant la couleur de la cellule
    :raise AssertionError: Si le paramètre n'est pas une cellule ou si la cellule ne contient pas de couleur
    """
    assert type_cellule(cell) == True and cell[VALEUR] >= 0, "La cellule n'est pas une cellule ou n'a pas de couleur "
    couleur = cell[VALEUR]
    return couleur

def setCouleurCellule(cell: Cellule, couleur: int) -> None:
    """
    Fonction permettant de définir une couleur à une cellule

    :param cell: cellule concernée
    :param couleur: couleur attribuée à la cellule concernée
    :return: None
    :raise AssertionError: Si le paramètre n'est pas une cellule ou que le second paramètre n'est pas un entier
    """
    assert type_cellule(cell) == True and type(couleur) == int, "La cellule n'est pas une cellule ou le second paramètre n'est pas un entier"
    cell[VALEUR] = couleur
    return None

def setNonVuCellule(cell : Cellule) -> None:
    """
    Fonction permettant de rendre une cellule en non-"découverte"

    :param cell: Cellule concernée
    :return: None
    :raise AssertionError: Si le paramètre n'est pas une cellule
    """
    assert type_cellule(cell) == True, "La cellule n'est pas une cellule"
    cell[VALEUR] = None
    return None

