# Model/Joueur.py

from Model.CustomTypes import *
from Model.Image import *
from Model.Cellule import *
from Model.Bloc import *
from Model.Suggestion import *
from Model.Nonogram import *


def isVuCellJoueur(image: PlayerImage, pos: Position) -> bool:
    """
    Fonction permettant de savoir si la cellule sélectionnée par le joueur a déjà été découverte

    :param image: image du joueur
    :param pos: position de la cellule
    :return: True si la cellule a déjà été découverte, False sinon
    """
    decouv = False
    cell = getCellImage(image, pos)
    if isVuCellule(cell) == True:
        decouv = True
    return decouv

def isCouleurCorrecteImage(image: ModelImage, pos: Position, couleur: int) -> bool:
    """
    Fonction permettant de savoir si la couleur choisit par le joueur est correcte

    :param image: image à trouver
    :param pos: position de la cellule sélectionnée
    :param couleur: couleur choisit par le joueur
    :return: True si la couleur est correcte, False sinon
    """
    cell = getCellImage(image, pos)
    couleurCorrecte = getCouleurCellule(cell)
    bonneCouleur = False
    if couleur == couleurCorrecte:
        bonneCouleur = True
    return bonneCouleur

