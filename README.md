# 🔧 Zotokaf DevKit

A command-line tool (CLI) that brings together several small and useful utilities for developers, students, makers, or anyone who wants to save time with common tasks (hashing, encoding, formatting, networking, etc.).

---

## 🚀 What is it for?

This program allows you to:

* Generate unique identifiers (UUID)
* Hash or verify passwords (hashing)
* Encode/decode text in base64
* Read the content of a JWT token (useful for APIs)
* Beautify JSON or YAML
* Check if a website is reachable (ping)
* Get the IP address of a website (DNS resolution)

All this, without installing anything besides Python and the listed dependencies!

---

## ⚙️ Installation (one-time setup)

1. Open a terminal in the project directory.
2. Run the following commands:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 🧪 How to use it?

Each tool is a "command". You run the program with the specific command you want. Here are the most useful ones:

* **Generate a unique identifier (UUID)**

  ```bash
  python toolbox.py uuid
  ```

  → Displays a UUID (useful for generating unique IDs).

* **Hash a text** (e.g., to verify a password)

  ```bash
  python toolbox.py hash --algo sha256 --text "HelloZotokaf"
  ```

  → Displays the SHA256 hash of the string "HelloZotokaf".

* **Encode text in base64**

  ```bash
  python toolbox.py encode base64 --text "Zotokaf123"
  ```

* **Decode base64 text**

  ```bash
  python toolbox.py decode base64 --text c2VjcmV0MTIz
  ```

* **Decode a JWT token**

  ```bash
  python toolbox.py decode jwt --token "eyJhbGciOi..."
  ```

* **Beautify JSON**

  ```bash
  python toolbox.py beautify json --input '{"name":"GPT","age":2}'
  ```

* **Beautify YAML**

  ```bash
  python toolbox.py beautify yaml --input 'name: GPT\nage: 2'
  ```

* **Ping a website**

  ```bash
  python toolbox.py ping --host google.com
  ```

* **Resolve a domain (DNS)**

  ```bash
  python toolbox.py dns --host github.com --record A
  ```

---

## 💡 Beginner tip

If you just run:

```bash
python toolbox.py
```

You'll see a menu listing the available tools and usage examples.

---

## 📦 Dependencies

* `colorama` (for colored output)
* `PyYAML` (for YAML support)
* `pyjwt` (for JWT token decoding)
* `dnspython` (for DNS resolution)

Install them with:

```bash
pip install -r requirements.txt
```

---

**Author:** luzocpp (renamed as part of the Zotokaf project)




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
