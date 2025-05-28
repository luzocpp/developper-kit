#!/usr/bin/env python3
import argparse
import uuid
import hashlib
import base64
import json
import yaml
import subprocess
import socket
import sys
from colorama import Fore, Style, init
try:
    import jwt
except ImportError:
    jwt = None

init(autoreset=True)

def generate_uuid():
    print(f"{Fore.GREEN}UUIDv4: {uuid.uuid4()}")

def hash_text(algo, text):
    algos = {
        'md5': hashlib.md5,
        'sha1': hashlib.sha1,
        'sha256': hashlib.sha256,
        'sha512': hashlib.sha512
    }
    if algo not in algos:
        print(f"{Fore.RED}Algorithme non supporté: {algo}")
        return
    h = algos[algo](text.encode()).hexdigest()
    print(f"{Fore.GREEN}{algo.upper()} hash: {h}")

def encode_base64(text):
    encoded = base64.b64encode(text.encode()).decode()
    print(f"{Fore.GREEN}Base64: {encoded}")

def decode_base64(text):
    try:
        decoded = base64.b64decode(text).decode()
        print(f"{Fore.GREEN}Decoded: {decoded}")
    except Exception as e:
        print(f"{Fore.RED}Erreur de décodage: {e}")

def decode_jwt(token):
    if not jwt:
        print(f"{Fore.RED}PyJWT n'est pas installé. Installez-le avec 'pip install pyjwt'.")
        return
    try:
        header = jwt.api_jws.get_unverified_header(token)
        payload = jwt.decode(token, options={"verify_signature": False})
        print(f"{Fore.CYAN}Header:\n{json.dumps(header, indent=2)}")
        print(f"{Fore.GREEN}Payload:\n{json.dumps(payload, indent=2)}")
    except Exception as e:
        print(f"{Fore.RED}Erreur de décodage JWT: {e}")

def beautify_json(input_str):
    try:
        obj = json.loads(input_str)
        print(f"{Fore.GREEN}{json.dumps(obj, indent=2, ensure_ascii=False)}")
    except Exception as e:
        print(f"{Fore.RED}Erreur JSON: {e}")

def beautify_yaml(input_str):
    try:
        obj = yaml.safe_load(input_str)
        print(f"{Fore.GREEN}{yaml.dump(obj, allow_unicode=True, sort_keys=False)}")
    except Exception as e:
        print(f"{Fore.RED}Erreur YAML: {e}")

def ping_host(host):
    try:
        print(f"{Fore.YELLOW}Ping {host}...\n")
        subprocess.run(["ping", "-c", "4", host], check=True)
    except Exception as e:
        print(f"{Fore.RED}Erreur ping: {e}")

def dns_lookup(host, record):
    import dns.resolver
    try:
        answers = dns.resolver.resolve(host, record)
        for rdata in answers:
            print(f"{Fore.GREEN}{rdata}")
    except Exception as e:
        print(f"{Fore.RED}Erreur DNS: {e}")

def main():
    parser = argparse.ArgumentParser(
        description="Outils CLI pour développeurs",
        epilog="Exemples:\n  python toolbox.py uuid\n  python toolbox.py hash --algo sha256 --text 'bonjour'\n  python toolbox.py encode base64 --text 'secret123'\n  python toolbox.py decode jwt --token 'eyJhbGciOi...'\n  python toolbox.py beautify json --input '{\"name\":\"GPT\",\"age\":2}'\n  python toolbox.py ping --host google.com\n  python toolbox.py dns --host openai.com --record A",
        formatter_class=argparse.RawTextHelpFormatter
    )
    subparsers = parser.add_subparsers(dest="command")

    # UUID
    subparsers.add_parser("uuid", help="Générer un UUID v4")

    # Hash
    hash_parser = subparsers.add_parser("hash", help="Calculer un hash")
    hash_parser.add_argument("--algo", required=True, choices=["md5", "sha1", "sha256", "sha512"], help="Algorithme de hash")
    hash_parser.add_argument("--text", required=True, help="Texte à hasher")

    # Encode
    encode_parser = subparsers.add_parser("encode", help="Encodage")
    encode_sub = encode_parser.add_subparsers(dest="enc_type")
    base64_parser = encode_sub.add_parser("base64", help="Base64 encode")
    base64_parser.add_argument("--text", required=True, help="Texte à encoder")

    # Decode
    decode_parser = subparsers.add_parser("decode", help="Décodage")
    decode_sub = decode_parser.add_subparsers(dest="dec_type")
    base64_dec_parser = decode_sub.add_parser("base64", help="Base64 decode")
    base64_dec_parser.add_argument("--text", required=True, help="Texte à décoder")
    jwt_parser = decode_sub.add_parser("jwt", help="Décoder JWT (header+payload)")
    jwt_parser.add_argument("--token", required=True, help="Token JWT à décoder")

    # Beautify
    beautify_parser = subparsers.add_parser("beautify", help="Beautifier JSON/YAML")
    beautify_sub = beautify_parser.add_subparsers(dest="fmt_type")
    json_parser = beautify_sub.add_parser("json", help="Beautifier JSON")
    json_parser.add_argument("--input", required=True, help="Entrée JSON brute")
    yaml_parser = beautify_sub.add_parser("yaml", help="Beautifier YAML")
    yaml_parser.add_argument("--input", required=True, help="Entrée YAML brute")

    # Ping
    ping_parser = subparsers.add_parser("ping", help="Ping une adresse")
    ping_parser.add_argument("--host", required=True, help="Hôte à pinger")

    # DNS
    dns_parser = subparsers.add_parser("dns", help="DNS lookup")
    dns_parser.add_argument("--host", required=True, help="Nom de domaine")
    dns_parser.add_argument("--record", required=True, help="Type d'enregistrement (A, MX, TXT, etc.)")

    args = parser.parse_args()

    if not args.command:
        print(f"\nOutils disponibles :\n")
        print(f"  uuid         Générer un UUID v4")
        print(f"  hash         Calculer un hash (MD5, SHA1, SHA256, SHA512)")
        print(f"  encode base64  Encoder en base64")
        print(f"  decode base64  Décoder du base64")
        print(f"  decode jwt     Décoder un JWT (header+payload)")
        print(f"  beautify json  Beautifier du JSON")
        print(f"  beautify yaml  Beautifier du YAML")
        print(f"  ping           Ping une adresse")
        print(f"  dns            DNS lookup (A, MX, TXT, etc.)\n")
        print(f"Exemples :")
        print("  python toolbox.py uuid")
        print("  python toolbox.py hash --algo sha256 --text 'bonjour'")
        print("  python toolbox.py encode base64 --text 'secret123'")
        print("  python toolbox.py decode jwt --token 'eyJhbGciOi...'")
        print('  python toolbox.py beautify json --input "{\\"name\\":\\"GPT\\",\\"age\\":2}"')
        print("  python toolbox.py ping --host google.com")
        print("  python toolbox.py dns --host wilycpp.com --record A\n")
        sys.exit(0)

    if args.command == "uuid":
        generate_uuid()
    elif args.command == "hash":
        hash_text(args.algo, args.text)
    elif args.command == "encode":
        if args.enc_type == "base64":
            encode_base64(args.text)
    elif args.command == "decode":
        if args.dec_type == "base64":
            decode_base64(args.text)
        elif args.dec_type == "jwt":
            decode_jwt(args.token)
    elif args.command == "beautify":
        if args.fmt_type == "json":
            beautify_json(args.input)
        elif args.fmt_type == "yaml":
            beautify_yaml(args.input)
    elif args.command == "ping":
        ping_host(args.host)
    elif args.command == "dns":
        dns_lookup(args.host, args.record)

if __name__ == "__main__":
    main()
