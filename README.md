
# Creation d'une Application avec KivyMD

## Installation des modules necessaires

Rassurez vous que python est déjà installé dans votre ordinateur

### Mise a jour des pip:

Environnement virtuel

    python -m pip install --upgrade pip setuptools virtualenv

Mise a jour du module pip

    python.exe -m pip install --upgrade pip

Créer un dossier projet "projet" par exemple et placer vous dans le repertoire "projet"

    C:\Users\.......\projet>

### Excuter les commandes ci-après:

Créer un environnement virtuel dans le repertoire du projet

    python -m virtualenv nomDuProjet

Activer l'environnement pour l'excution du programme:

    nomDuProjet\Scripts\activate

Installation de kivy dans le repertoire du projet:

    pip install kivy[base] kivy_examples --pre --extra-index-url https://kivy.org/downloads/simple/

Installation de kivymd dans le repertoire du projet:

    pip install kivymd

### Créer un fichier python: "test.py" par exemple

Excuter le programme comme dans python simplement:

    py text.py


