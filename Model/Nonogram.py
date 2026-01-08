# Model/Nonogram.py
from Model.Bloc import *
from Model.Cellule import *
from Model.CustomTypes import ModelImage, LstBlocs, PlayerImage
from Model.Image import getCellImage, type_image_light


def compterBlocsSurLigne(image: ModelImage, ligne: int = 0) -> LstBlocs:
    """
    Fonction permettant de compter les blocs sur la ligne

    :param image: image concernée
    :param ligne: ligne concernée
    :return: une liste des blocs sur la ligne
    :raise AssertionError: Si le premier paramètre n'est pas une image ou si le second n'est pas un entier
    """
    assert type_image_light(image) == True, "le premier paramètre n'est pas une image"
    assert type(ligne) == int, "le second paramètre n'est pas un entier"
    listeBlocs = []
    couleur = 0
    longueur = 0
    for cell in image[ligne]:
        couleurCell = getCouleurCellule(cell)
        if couleurCell != couleur:
            if couleur != 0:
                listeBlocs.append(construireBloc(longueur, couleur))
            couleur = couleurCell
            longueur = 1
        elif couleur != 0:
                longueur += 1
    if couleur != 0:
        listeBlocs.append(construireBloc(longueur, couleur))
    return listeBlocs

def getBlocsLignes(image: ModelImage) -> LstBlocs:
    """
    Fonction permettant d'obtenir les blocs pour chaque ligne d'une image donnée

    :param image: image concernée
    :return: une liste de liste des blocs pour chaque ligne
    :raise AssertionError: Si le paramètre n'est pas une image
    """
    assert type_image_light(image) == True, "le paramètre n'est pas une image"
    blocs = []
    for i in range(len(image)):
        blocLigne = compterBlocsSurLigne(image, i)
        blocs.append(blocLigne)
    return blocs

def compterBlocsSurColonne(image: ModelImage, colonne: int = 0) -> LstBlocs:
    """
    Fonction permettant de compter les blocs pour une colonne donnée, d'une image donnée

    :param image: image concernée
    :param colonne: colonne choisit
    :return: une liste des blocs sur la colonne
    :raise AssertionError: Si le premier paramètre n'est pas une image ou si le second n'est pas un entier
    """
    assert type_image_light(image) == True, "le premier paramètre n'est pas une image"
    assert type(colonne) == int, "le second paramètre n'est pas un entier"
    listeBlocs = []
    couleur = getCouleurCellule(image[0][colonne])
    longueur = 1
    for i in range(1, len(image)):
        couleurCell = getCouleurCellule(image[i][colonne])
        if couleurCell != couleur:
            if couleur != 0:
                listeBlocs.append(construireBloc(longueur, couleur))
            couleur = couleurCell
            longueur = 1
        else:
            if couleur != 0:
                longueur += 1
    if couleur != 0:
        listeBlocs.append(construireBloc(longueur, couleur))
    return listeBlocs

def getBlocsColonnes(image: ModelImage) -> LstBlocs:
    """
    Fonction permettant de compter les blocs sur chaque colonne d'une image donnée

    :param image: image concernée
    :return: Une liste de liste des blocs pour chaque colonne
    """
    assert type_image_light(image) == True, "Le paramètre n'est pas une image"
    blocs = []
    for j in range(len(image[0])):
        blocsColonne = compterBlocsSurColonne(image, j)
        blocs.append(blocsColonne)
    return blocs

def isVuImage(image: PlayerImage) -> bool:
    """
    Fonction permettant de savoir si toutes les cellules de l'image ont été découvertes par le joueur

    :param image: image du joueur
    :return: True si toutes les cellules sont découvertes, False sinon
    """
    vu = True
    i = 0
    print(image)
    while vu == True and i < len(image):
        j = 0
        while vu == True and j < len(image[i]):
            print(image[i][j])
            vu = isVuCellule(image[i][j])
            j += 1
        i += 1
    return vu

def reinitialiserImage(image: PlayerImage) -> None:
    """
    Fonction permettant de remettre toutes les cellules de l'image à l'état non-découvert

    :param image: image du joueur
    :return: None
    """
    for i in range(len(image)):
        for j in range(len(image[i])):
            setNonVuCellule(image[i][j])
    return None

def vuGauche(image: PlayerImage, listeBloc: LstBlocs, ligne: int) -> bool:
    """
    Fonction permettant de vérifier si les blocs sur une ligne donnée ont été découvert à gauche du bloc sélectionné

    :param image: image du joueur
    :param listeBloc: liste des blocs
    :param ligne: ligne sélectionnée
    :return: True si tous les blocs à gauche du blocs découvert sont découvert, False sinon
    """
    reponse = False
    vu_gauche = True
    i = 0
    idxBloc = 0
    while i < len(image[ligne]) and idxBloc < len(listeBloc) and vu_gauche:
        if not isVuCellule(image[ligne][i]):
            vu_gauche = False
        elif image[ligne][i][VALEUR] == getCouleurBloc(listeBloc[idxBloc]):
            bloc_vu = True
            j = 0
            while bloc_vu and j < listeBloc[idxBloc][NOMBRE] and i+j < len(image):
                if not isVuCellule(image[ligne][i+j]):
                    bloc_vu = False
                j += 1
            if bloc_vu:
                setVuBloc(listeBloc[idxBloc], True)
                reponse = True
                i += j
            idxBloc += 1
        i += 1
    return reponse

def vuDroite(image: PlayerImage, listeBloc: LstBlocs, ligne: int) -> bool:
    """
    Fonction permettant de vérifier si les blocs sur une ligne donnée ont été découvert à droite du bloc sélectionné

    :param image: image du joueur
    :param listeBloc: liste des blocs
    :param ligne: ligne sélectionnée
    :return: True si tous les blocs à droite du blocs découvert sont découvert, False sinon
    """
    reponse = False
    vu_droite = True
    i = len(image[ligne]) - 1
    idxBloc = len(listeBloc) - 1
    while i > 0 and idxBloc > 0 and vu_droite:
        if not isVuCellule(image[ligne][i]):
            vu_droite = False
        elif getCouleurCellule(image[ligne][i])== getCouleurBloc(listeBloc[idxBloc]):
            bloc_vu = True
            j = getNombreBloc(listeBloc[idxBloc]) -1
            while bloc_vu and j >= 0:
                if not isVuCellule(image[ligne][i-j]):
                    bloc_vu = False
                j -= 1
            if bloc_vu:
                setVuBloc(listeBloc[idxBloc], True)
                reponse = True
            idxBloc -= 1
        i -= 1
    return reponse


def verifierBlocsLigneImage(image: PlayerImage, listeBloc: LstBlocs, ligne: int) -> bool:
    """
    Fonction permettant de vérifier si les blocs sur une ligne donnée d'une image ont été découvert à gauche et à droite

    :param image: image du joueur
    :param listeBloc: liste des blocs
    :param ligne: ligne concernée
    :return: True si les blocs ont été découvert, False sinon
    """
    reponse = False
    if vuGauche(image, listeBloc, ligne) or vuDroite(image, listeBloc, ligne):
        reponse = True
    return reponse

def vuHaut(image: PlayerImage, listeBloc: LstBlocs, col: int) -> bool:
    """
    Fonction permettant de vérifier si les blocs d'une colonne donnée sont découvert en haut du bloc sélectionné

    :param image: image du joueur
    :param listeBloc: liste des blocs
    :param col: colonne concernée
    :return: True si tous les blocs en haut du bloc sont découvert, False sinon
    """
    reponse = False
    vu_haut = True
    i = 0
    idxBloc = 0
    while i < len(image) and idxBloc < len(listeBloc) and vu_haut:
        if not isVuCellule(image[i][col]):
            vu_haut = False
        elif image[i][col][VALEUR] == getCouleurBloc(listeBloc[idxBloc]):
            bloc_vu = True
            j = 0
            while bloc_vu and j < listeBloc[idxBloc][NOMBRE] and i+j < len(image):
                if not isVuCellule(image[i+j][col]):
                    bloc_vu = False
                j += 1
            if bloc_vu:
                setVuBloc(listeBloc[idxBloc], True)
                reponse = True
                i += j
            idxBloc += 1
        i += 1
    return reponse

def vuBas(image: PlayerImage, listeBloc: LstBlocs, col: int) -> bool:
    """
    Fonction permettant de vérifier si les blocs d'une colonne donnée sont découvert en bas du bloc sélectionné

    :param image: image du joueur
    :param listeBloc: liste des blocs
    :param col: colonne concernée
    :return: True si tous les blocs en bas du bloc sont découvert, False sinon
    """
    reponse = False
    vu_bas = True
    i = len(image) - 1
    idxBloc = len(listeBloc) - 1
    while i >= 0 and idxBloc >= 0 and vu_bas:
        if not isVuCellule(image[i][col]):
            vu_bas = False
        elif getCouleurCellule(image[i][col]) == getCouleurBloc(listeBloc[idxBloc]):
            bloc_vu = True
            j = getNombreBloc(listeBloc[idxBloc]) - 1
            while bloc_vu and j >= 0:
                if not isVuCellule(image[i-j][col]):
                    bloc_vu = False
                j -= 1
            if bloc_vu:
                setVuBloc(listeBloc[idxBloc], True)
                reponse = True
            idxBloc -= 1
        i -= 1
    return reponse

def verifierBlocsColonneImage(image: PlayerImage, listeBloc: LstBlocs, colonne: int) -> bool:
    """
    Fonction permettant de vérifier si les blocs sur une colonne donnée d'une image ont été découvert en haut et en bas

    :param image: image du joueur
    :param listeBloc: liste des blocs
    :param ligne: ligne concernée
    :return: True si les blocs ont été découvert, False sinon
    """
    reponse = False
    if vuHaut(image, listeBloc, colonne) or vuBas(image, listeBloc, colonne):
        reponse = True
    return reponse