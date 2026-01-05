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


