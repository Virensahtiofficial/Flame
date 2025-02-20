import time
import sys
import os
import json
import hashlib
import requests

CONFIG_PATH = "flame/data/config.json"
PASSWORD_PATH = "flame/data/password.json"
OS_PATH = "flame/os.py"

# Controleer of de modules al geïnstalleerd zijn
try:
    import bs4
    import requests
except ImportError:
    os.system(f"{sys.executable} -m pip install bs4 requests -q")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def setup():
    clear()
    print("\033[93mWelcome to FlameOS!\033[0m")
    time.sleep(1)

    # Vraag de gebruiker om een wachtwoord in te stellen
    while True:
        password = input("Set a password: ")
        confirm_password = input("Confirm password: ")
        
        if password == confirm_password:
            hashed_password = hash_password(password)
            break
        else:
            print("\033[91mPasswords do not match! Try again.\033[0m")

    # Maak de benodigde mappen aan
    os.makedirs("flame/data", exist_ok=True)

    # Sla setup-status op in config.json
    with open(CONFIG_PATH, "w") as f:
        json.dump({"setup": True}, f, indent=4)

    # Sla het gehashte wachtwoord op in password.json
    with open(PASSWORD_PATH, "w") as f:
        json.dump({"password": hashed_password}, f, indent=4)

    print("\n\033[92mSetup done! Updating OS...\033[0m")
    update_os()
    time.sleep(2)

def update_os():
    """Downloadt de nieuwste versie van os.py na de setup"""
    url = "https://raw.githubusercontent.com/Virensahtiofficial/Flame/refs/heads/main/os.py"
    doelmap = "flame"
    bestand_naam = "os.py"
    bestand_pad = os.path.join(doelmap, bestand_naam)

    try:
        print("\033[94mUpdating system...\033[0m")
        response = requests.get(url, stream=True)
        response.raise_for_status()

        with open(bestand_pad, "wb") as bestand:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    bestand.write(chunk)

        print("\033[92mUpdate successful!\033[0m")
    except requests.RequestException as e:
        print(f"\033[91mUpdate failed: {e}\033[0m")

def boot():
    clear()
    
    # Controleer of setup al is uitgevoerd
    if not os.path.isfile(CONFIG_PATH):
        setup()
        

    # Controleer of het OS-bestand bestaat
    if not os.path.isfile(OS_PATH):
        print("\033[91mError: OS files not found!\033[0m")
        time.sleep(3)
        clear()
        sys.exit(1)
        
    # Start het OS
    os.system(f"{sys.executable} {OS_PATH}")

if __name__ == "__main__":
    boot()
