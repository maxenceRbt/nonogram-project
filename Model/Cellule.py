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