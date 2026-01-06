# Model/Position.py
from Model.debug import *
from Model.CustomTypes import Position


#
# Les positions ne sont pas toujours faciles à gérer !
#
# Sur une image, quand on parle d'un pixel (x, y), x représente la colonne et y la ligne.
# Dans un tableau, quand on cherche la valeur tab[i][j], cette fois, c'est i qui désigne la ligne et j la colonne.
#
# Pour tenter d'éviter d'intervertir ligne/colonne, on va créer un dictionnaire avec deux clés bien explicites
# - la clé LIGNE qui représentera le numéro de ligne
# - la clé COLONNE qui représentera le numéro de colonne
#

LIGNE = "ligne"
COLONNE = "colonne"



def type_position(position: Position) -> bool:
    """
    Fonction permettant de déterminer si le paramètre peut représenter ou non une position.

    Cette fonction ne peut valider la valeur des lignes/colonnes

    :param position: Position à tester
    :return: True si le paramètre correspond à une position, False sinon
    """
    if type(position) is not dict:
        debug(f"Le paramètre {position} n'est pas un dictionnaire")
        return False
    if LIGNE not in position or COLONNE not in position:
        debug(f"Le dictionnaire {position} ne contient pas une des clés {LIGNE} ou {COLONNE}")
        return False
    if type(position[LIGNE]) is not int or type(position[COLONNE]) is not int:
        debug(f"Une des valeurs du dictionnaire {position} n'est pas un entier")
        return False
    return True


#============== DEBUT DU CODE ============================

def construirePosition() -> Position:
    """
    Fonction permettant de créer un dictionnaire de position avec pour chaque clé LIGNE et COLONNE, une valeur de 0

    :return: Dictionnaire de type Position
    """
    pos = {LIGNE : 0, COLONNE: 0}
    return pos

def getLignePosition(pos: dict) -> int:
    """
    Fonction permettant d'obtenir le numéro de ligne d'une position

    :param pos: dictionnaire représentant la position concernée
    :return: entier représentant le numéro de la ligne de la position
    """
    assert type_position(pos) == True, "le paramètre n'est pas une position"
    ligne = pos.get(LIGNE)
    return ligne

def getColonnePosition(pos: dict) -> int:
    """
    Fonction permettant d'obtenir le numéro de colonne d'une position

    :param pos: dictionnaire représentant la position concernée
    :return: entier représentant le numéro de la colonne de la position
    """
    assert type_position(pos) == True, "le paramètre n'est pas une position"
    colonne = pos.get(COLONNE)
    return colonne

def setLignePosition(pos: dict, ligne: int) -> None:
    """
    Fonction permettant de modifier la valeur de la ligne de la position avec un entier

    :param pos: dictionnaire représentant la position concernée
    :param ligne: entier remplaçant le numéro de ligne de la position
    :return: None
    """
    assert type_position(pos) == True and type(ligne) == int, "le premier paramètre n'est pas une position ou le second n'est pas un entier"
    pos[LIGNE] = ligne
    return None

def setColonnePosition(pos: dict, colonne: int) -> None:
    """
    Fonction permettant de modifier la valeur de la colonne de la position avec un entier

    :param pos: dictionnaire représentant la position concernée
    :param colonne: entier remplaçant le numéro de colonne de la position
    :return: None
    """
    assert type_position(pos) == True and type(colonne) == int, "le premier paramètre n'est pas une position ou le second n'est pas un entier"
    pos[COLONNE] = colonne
    return colonne

def incLignePosition(pos: dict, valeur: int = 1) -> None:
    """
    Fonction permettant d'incrémenter une valeur au numéro de ligne d'une position

    :param pos: dictionnaire représentant la position concernée
    :param valeur: entier à incrémenter au numéro de ligne de la position
    :return: None
    """
    assert type_position(pos) == True and type(valeur) == int, "le premier paramètre n'est pas une position ou le second n'est pas un entier"
    pos[LIGNE] += valeur
    return None

def incColonnePosition(pos: dict, valeur: int = 1) -> None:
    """
    Fonction permettant d'incrémenter une valeur au numéro de colonne d'une position

    :param pos: dictionnaire représentant la position concernée
    :param valeur: entier à incrémenter au numéro de colonne de la position
    :return: None
    """
    assert type_position(pos) == True and type(valeur) == int, "le premier paramètre n'est pas une position ou le second n'est pas un entier"
    pos[COLONNE] += valeur
    return None

def decLignePosition(pos: dict, valeur: int = 1) -> None:
    """
    Fonction permettant de décrémenter une valeur au numéro de ligne d'une position

    :param pos: dictionnaire représentant la position concernée
    :param valeur: entier à décrémenter au numéro de ligne de la position
    :return: None
    """
    assert type_position(pos) == True and type(valeur) == int, "le premier paramètre n'est pas une position ou le second n'est pas un entier"
    pos[LIGNE] -= valeur
    return None

def decColonnePosition(pos: dict, valeur: int = 1) -> None:
    """
    Fonction permettant de décrémenter une valeur au numéro de colonne d'une position

    :param pos: dictionnaire représentant la position concernée
    :param valeur: entier à décrémenter au numéro de colonne de la position
    :return: None
    """
    assert type_position(pos) == True and type(valeur) == int, "le premier paramètre n'est pas une position ou le second n'est pas un entier"
    pos[COLONNE] -= valeur
    return None