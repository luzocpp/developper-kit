# luzo devkit

Un outil en ligne de commande (CLI) qui regroupe plusieurs petits outils pratiques pour les développeurs, étudiants, makers, ou toute personne qui veut gagner du temps avec des manipulations courantes (hash, encodage, formatage, réseau, etc.).

## À quoi ça sert ?
Ce programme te permet de :
- Générer des identifiants uniques (UUID)
- Chiffrer ou vérifier des mots de passe (hash)
- Encoder/décoder des textes en base64
- Lire le contenu d'un token JWT (utile pour les API)
- Rendre du JSON ou du YAML plus lisible
- Vérifier si un site répond (ping)
- Trouver l'adresse IP d'un site (DNS)

Tout ça, sans rien installer d'autre que Python et les dépendances listées !

## Installation (une seule fois)
1. Ouvre un terminal dans le dossier du projet.
2. Tape :
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Comment l'utiliser ?
Chaque outil est une "commande". Tu lances le programme avec la commande de ton choix. Voici les plus utiles :

- **Générer un identifiant unique**
  ```
  python toolbox.py uuid
  ```
  → Affiche un UUID (pratique pour créer des identifiants).

- **Calculer le hash d'un texte** (pour vérifier un mot de passe, etc.)
  ```
  python toolbox.py hash --algo sha256 --text "BonjourLuzo"
  ```
  → Affiche le hash SHA256 du mot "BonjourLuzo".

- **Encoder un texte en base64** (pour cacher un mot de passe, transmettre des données, etc.)
  ```
  python toolbox.py encode base64 --text "Luzocppboy123"
  ```

- **Décoder du base64**
  ```
  python toolbox.py decode base64 --text c2VjcmV0MTIz
  ```

- **Lire le contenu d'un token JWT** (utile pour les développeurs d'API)
  ```
  python toolbox.py decode jwt --token "eyJhbGciOi..."
  ```

- **Rendre du JSON plus lisible**
  ```
  python toolbox.py beautify json --input '{"name":"GPT","age":2}'
  ```

- **Rendre du YAML plus lisible**
  ```
  python toolbox.py beautify yaml --input 'nom: GPT\nage: 2'
  ```

- **Vérifier si un site répond (ping)**
  ```
  python toolbox.py ping --host google.com
  ```

- **Trouver l'adresse IP d'un site (DNS)**
  ```
  python toolbox.py dns --host github.com --record A
  ```

## Astuce débutant
Si tu lances juste :
```
python toolbox.py
```
tu verras un menu avec la liste des outils et des exemples.

## Dépendances
- colorama (pour la couleur)
- PyYAML (pour le YAML)
- pyjwt (pour les tokens JWT)
- dnspython (pour le DNS)

Installe-les avec :
```
pip install -r requirements.txt
```

---

**Auteur :** luzocpp
