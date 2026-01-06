# Model/Bloc.py
#

from Model.CustomTypes import Bloc

# Clé pour stocker le nombre de cellules contigües de même couleur (bloc)
NOMBRE = "nombre"
# Couleur des cellules contigües du bloc
COULEUR = "couleur"
# Booléen permettant de savoir si l'utilisateur a découvert ou non le bloc correspondant
VU = "vu"


def type_bloc(bloc: Bloc) -> bool:
    """
    Détermine si le paramètre peut correspondre ou non à un bloc.

    Un bloc est un dictionnaire contenant 3 clés (NOMBRE, COULEUR, VU) auquelles
    sont associées des valeurs de type (int, int, bool).

    :param bloc: Objet à tester
    :return: True si l'objet correspond à un bloc, False sinon.
    """
    if type(bloc) is not dict:
        return False
    if len(bloc) != 3 or NOMBRE not in bloc or COULEUR not in bloc or VU not in bloc:
        return False
    if type(bloc[NOMBRE]) is not int or bloc[NOMBRE]<=0:
        return False
    if type(bloc[COULEUR]) is not int or bloc[COULEUR]<=0:
        return False
    if type(bloc[VU]) is not bool:
        return False
    return True

#=============== DEBUT DU CODE ===================================

def construireBloc(nombre: int, couleur: int) -> Bloc:
    """
    Fonction permettant de créer un bloc

    :param nombre: entier correspondant au nombre de cellules
    :param couleur: entier correspondant à la couleur
    :return: un dictionnaire représentant le bloc
    """
    assert type(nombre) == int and type(couleur) == int, "Au moins l'un des deux paramètres n'est pas un entier"
    assert nombre > 0 and couleur > 0, "Au moins l'un des deux paramètres n'est pas strictement positif"
    bloc = {NOMBRE: nombre, COULEUR: couleur, VU: False}
    return bloc

def getNombreBloc(bloc: Bloc) -> int:
    """
    Fonction permettant d'obtenir le nombre de cellule contigües de même couleur du bloc

    :param bloc: bloc concerné
    :return: entier représentant la valeur du nombre de cellule contigües de même couleur du bloc
    """
    assert type_bloc(bloc) == True, "le paramètre n'est pas un bloc"
    nombre = bloc[NOMBRE]
    return nombre

def getCouleurBloc(bloc: Bloc) -> int:
    """
    Fonction permettant d'obtenir la valeur de la couleur du bloc

    :param bloc: bloc concerné
    :return: entier représentant la valeur de la couleur du bloc
    """
    assert type_bloc(bloc) == True, "le paramètre n'est pas un bloc"
    couleur = bloc[COULEUR]
    return couleur

def isVuBloc(bloc: Bloc) -> bool:
    """
    Fonction permettant de savoir si le bloc a été découvert ou non

    :param bloc: bloc concerné
    :return: True si le bloc a été découvert, False sinon
    """
    assert type_bloc(bloc) == True, "le paramètre n'est pas un bloc"
    vu = bloc[VU]
    return vu

def setVuBloc(bloc: Bloc, vu : bool) -> None:
    """
    Fonction permettant de définir si un bloc a été découvert ou non

    :param bloc: bloc concerné
    :param vu: booléen représentant si le bloc est découvert ou non
    :return: None
    """
    assert type_bloc(bloc) == True, "le premier paramètre n'est pas un bloc"
    assert type(vu) == bool, "le second paramètre n'est pas un booléen"
    bloc[VU] = vu
    return None