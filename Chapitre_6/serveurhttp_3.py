#!/usr/bin/env python3
from http.server import SimpleHTTPRequestHandler
from http.server import HTTPServer
import os


ip = "127.0.0.1"
port = 8080


def main():
    try:
        os.chdir("/")
        serveur = HTTPServer((ip, port), SimpleHTTPRequestHandler)
        print(f"Démarrage du serveur HTTP: http://{ip}:{port}")
        serveur.serve_forever()
    except FileNotFoundError as e:
        sys.stderr.write(
            f"ERREUR! Le répertoire \"{repertoire}\" n'existe pas!\n")
        raise e
    except KeyboardInterrupt:
        serveur.socket.close()


if __name__ == "__main__":
    main()
