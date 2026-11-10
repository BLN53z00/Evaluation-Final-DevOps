import sys
import time
import urllib.request

URL = "http://127.0.0.1:5000/"
ATTENDU = "Database Connection Status: Connected"

limite = time.time() + 60
derniere_reponse = "aucune réponse"

while time.time() < limite:
    try:
        with urllib.request.urlopen(URL, timeout=5) as reponse:
            derniere_reponse = reponse.read().decode()
        if derniere_reponse.strip() == ATTENDU:
            print("OK :", derniere_reponse)
            sys.exit(0)
    except Exception as erreur:
        derniere_reponse = f"erreur : {erreur}"
    time.sleep(2)

print(f"ECHEC : attendu '{ATTENDU}', obtenu '{derniere_reponse}'")
sys.exit(1)