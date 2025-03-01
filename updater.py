import requests
import os
from tqdm import tqdm  # Voortgangsbalk importeren
import time
os.system("clear")  # Terminal wissen (voor Linux/macOS; gebruik "cls" op Windows)
# URL van het bestand
url = "https://raw.githubusercontent.com/Virensahtiofficial/Flame/refs/heads/main/os.py"
# Specifieke map instellen
doelmap = "flame"  # Verander dit naar jouw gewenste map
bestand_naam = "os.py"  # Naam van het opgeslagen bestand

# Controleer of de map bestaat, anders maak hem aan
if not os.path.exists(doelmap):
    os.makedirs(doelmap)

# Volledig pad naar het bestand
bestand_pad = os.path.join(doelmap, bestand_naam)

# Functie om de download voortgang te tonen
def download_bestand(url, bestand_pad):
    try:
        print("Updating system...")
        os.system("pip install requests tqdm bs4 -q")  # Vereiste libraries installeren
        response = requests.get(url, stream=True)
        response.raise_for_status()

        # Haal de totale bestandsgrootte op om de voortgang te berekenen
        totaal_grootte = int(response.headers.get('Content-Length', 0))

        # Download het bestand met een voortgangsbalk
        with open(bestand_pad, "wb") as bestand, tqdm(
            desc=bestand_naam,
            total=totaal_grootte,
            unit='B',
            unit_scale=True,
            ncols=100
        ) as bar:  # Gebruik tqdm voor voortgangsbalk
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    bestand.write(chunk)
                    bar.update(len(chunk))  # Update de voortgangsbalk

        print("\nUpdate was successfully done!")
        time.sleep(2)
        # Het gedownloade bestand uitvoeren
        os.system(f"python {bestand_pad}")

    except requests.RequestException as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unknown error: {e}")

# Start de downloadfunctie
download_bestand(url, bestand_pad)
