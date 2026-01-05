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


