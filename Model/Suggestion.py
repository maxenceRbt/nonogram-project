# Model/Suggestion.py

# Suggestions de coups à jouer modélisés par un dictionnaire à deux clés :
# - POSITION : Position dans l'image
# - COULEUR : Couleur à placer (la couleur transparente, 0, étant acceptée)

# Deux clés associées au dictionnaire représentant une suggestion :
POSITION = "position"
COULEUR = "couleur"


from Model.CustomTypes import *
from Model.Position import *

def type_suggestion(suggestion: Suggestion) -> bool:
    """
    Détermine si le paramètre correspond ou non à une suggestion

    :param suggestion: Objet à tester
    :return: True s'il correspond à une suggestion, False sinon
    """
    if type(suggestion) is not dict:
        return False
    if POSITION not in suggestion or COULEUR not in suggestion:
        return False
    if not type_position(suggestion[POSITION]):
        return False
    if type(suggestion[COULEUR]) is not int:
        return False
    return True

#=============== DEBUT DU CODE ===================================

def construireSuggestion(pos: Position, couleur: int) -> Suggestion:
    """
    Fonction permettant de construire une suggestion avec une position et une couleur donnée

    :param pos: position de la suggestion
    :param couleur: couleur à placer
    :return: un dictionnaire représentant la suggestion
    :raise AssertionError: Si pos n'est pas une position ou si couleur n'est pas un entier
    """
    assert type_position(pos), "le premier paramètre n'est pas une position"
    assert type(couleur) is int, "le second paramètre n'est pas un entier"
    suggestion = {POSITION: pos, COULEUR: couleur}
    return suggestion

def getPositionSuggestion(suggestion: Suggestion) -> Position:
    """
    Fonction permettant d'obtenir la position de la suggestion

    :param suggestion: suggestion concernée
    :return: un dictionnaire représentant la position de la suggestion
    :raise AssertionError: Si suggestion n'est pas une suggestion
    """
    assert type_suggestion(suggestion), "Le paramètre n'est pas une position"
    posSug = suggestion[POSITION]
    return posSug

def getCouleurSuggestion(suggestion : Suggestion) -> int:
    """
    Fonction permettant d'obtenir la couleur de la suggestion

    :param suggestion: suggestion concernée
    :return: la valeur de la couleur de la suggestion
    :raise AssertionError: Si suggestion n'est pas une suggestion
    """
    assert type_suggestion(suggestion), "le paramètre n'est pas une position"
    coulSug = suggestion[COULEUR]
    return coulSug
