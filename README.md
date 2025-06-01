# ENGLISH

Zotokaf DevKit is a command-line tool (CLI) that groups together several small and practical utilities for developers, students, makers, or anyone looking to save time with common operations such as hashing, encoding, formatting, and networking.

This tool has been developed and tested on Linux environments, including Manjaro, Arch Linux, Kali Linux, Ubuntu, and is also fully compatible with Windows systems.

## What is it for?

This program allows you to:

* Generate unique identifiers (UUID)
* Hash or verify passwords
* Encode/decode text in base64
* Decode the content of a JWT token (useful for API development)
* Beautify JSON or YAML
* Check if a website is responsive (ping)
* Resolve the IP address of a domain (DNS query)

All of this works without installing anything beyond Python and the listed dependencies.

## Installation (one-time setup)

1. Open a terminal in the project directory.
2. Run the following commands:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## How to use it

Each utility is a "command". You launch the program with the specific command you need. Here are the most useful ones:

* **Generate a unique identifier (UUID)**

```bash
python toolbox.py uuid
```

* **Hash a string**

```bash
python toolbox.py hash --algo sha256 --text "HelloZotokaf"
```

* **Encode a string in base64**

```bash
python toolbox.py encode base64 --text "Zotokaf123"
```

* **Decode a base64 string**

```bash
python toolbox.py decode base64 --text c2VjcmV0MTIz
```

* **Decode a JWT token**

```bash
python toolbox.py decode jwt --token "eyJhbGciOi..."
```

* **Beautify a JSON string**

```bash
python toolbox.py beautify json --input '{"name":"GPT","age":2}'
```

* **Beautify a YAML string**

```bash
python toolbox.py beautify yaml --input 'name: GPT\nage: 2'
```

* **Ping a website**

```bash
python toolbox.py ping --host google.com
```

* **DNS resolution**

```bash
python toolbox.py dns --host github.com --record A
```

## Beginner Tip

If you just run the program without arguments:

```bash
python toolbox.py
```

A menu will appear showing available tools and usage examples.

## Dependencies

* `colorama` (for colored terminal output)
* `PyYAML` (for YAML parsing)
* `pyjwt` (for decoding JWT tokens)
* `dnspython` (for DNS queries)

Install with:

```bash
pip install -r requirements.txt
```

---

**Author:** luzocpp (renamed in this project as Zotokaf)

# FRENCH

Zotokaf DevKit est un outil en ligne de commande (CLI) qui regroupe plusieurs petits utilitaires pratiques pour les développeurs, étudiants, makers ou toute personne souhaitant gagner du temps avec des opérations courantes telles que le hachage, l'encodage, le formatage et le réseau.

Cet outil a été développé et testé sur des systèmes Linux, dont Manjaro, Arch Linux, Kali Linux, Ubuntu, et est également totalement compatible avec Windows.

## À quoi ça sert ?

Ce programme permet de :

* Générer des identifiants uniques (UUID)
* Chiffrer ou vérifier des mots de passe
* Encoder/décoder des textes en base64
* Lire le contenu d'un token JWT (utile pour les APIs)
* Rendre le JSON ou YAML plus lisible (beautify)
* Vérifier la disponibilité d’un site (ping)
* Trouver l'adresse IP d’un domaine (résolution DNS)

Tout cela fonctionne sans avoir à installer autre chose que Python et les dépendances listées.

## Installation (à faire une seule fois)

1. Ouvre un terminal dans le dossier du projet.
2. Exécute les commandes suivantes :

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Comment l'utiliser

Chaque outil est une "commande". Tu lances le programme avec la commande souhaitée. Voici les plus utiles :

* **Générer un identifiant unique (UUID)**

```bash
python toolbox.py uuid
```

* **Calculer le hash d'un texte**

```bash
python toolbox.py hash --algo sha256 --text "HelloZotokaf"
```

* **Encoder une chaîne en base64**

```bash
python toolbox.py encode base64 --text "Zotokaf123"
```

* **Décoder une chaîne base64**

```bash
python toolbox.py decode base64 --text c2VjcmV0MTIz
```

* **Décoder un token JWT**

```bash
python toolbox.py decode jwt --token "eyJhbGciOi..."
```

* **Rendre un JSON plus lisible**

```bash
python toolbox.py beautify json --input '{"name":"GPT","age":2}'
```

* **Rendre un YAML plus lisible**

```bash
python toolbox.py beautify yaml --input 'name: GPT\nage: 2'
```

* **Tester la disponibilité d’un site (ping)**

```bash
python toolbox.py ping --host google.com
```

* **Résolution DNS**

```bash
python toolbox.py dns --host github.com --record A
```

## Astuce Débutant

Si tu exécutes le programme sans argument :

```bash
python toolbox.py
```

Un menu s’affichera avec la liste des outils disponibles et des exemples d’utilisation.

## Dépendances

* `colorama` (pour la couleur dans le terminal)
* `PyYAML` (pour le YAML)
* `pyjwt` (pour lire les tokens JWT)
* `dnspython` (pour les requêtes DNS)

Installation :

```bash
pip install -r requirements.txt
```

---

**Auteur :** luzocpp (renommé dans ce projet en Zotokaf)
