# Nonogram

Le jeu du Nonogram en Python/PyGame (pour la SAE 1 & 2 du S1) - [Wikipedia](https://en.wikipedia.org/wiki/Nonogram)

## Préparer l'environnement Python

Vérifiez que PyGame est bien installé sur le système utilisé. Le plus simple est
de lancer la commande d'installation : 
```sh
pip install pygame
```
Si la commande est refusée (vous n'avez pas les droits administrateur par exemple),
il faudra peut-être créer son environnement de développement.

Il sera peut-être utile de mettre à jour PyGame :
```shell
pip install pygame --upgrade
```

Commencez par vérifier que PyGame est installé ou non avec la commande : 
```shell
pip freeze | grep pygame
```
> Sous Windows : 
> ```shell
> pip freeze | findstr pygame
> ```

Si PyGame n'est pas installé et que vous n'êtes pas administrateur de la machine, 
créez votre environnement de développement avec la commande :
```shell
python -m venv venv
```
Cette commande crée un répertoire `venv/` contenant une "copie" de l'environnement Python.

Placez-vous dans l'environnement de développement `venv/` en tapant
la commande :

```shell
source venv/bin/activate
```
> Sous Windows
> ```Shell
> venv\Scripts\activate
> ```

Dans cet environnement, vous pouvez alors installer PyGame avec la commande : 
```shell
pip install pygame
```

Pour quitter l'environnement `venv/`, il suffit de taper la commande :
```shell
deactivate
```

### Remarque

Pour mettre à jour le package PyGame, il faut taper la commande : 
```shell
pip install pygame --upgrade
```

feat: ajoute la fonctionnalité de recherche

Cette fonctionnalité permet aux utilisateurs de rechercher des articles par mots-clés.
```

En utilisant ces préfixes, vous facilitez la compréhension des changements apportés et améliorez la collaboration 
au sein de votre équipe.
