import requests
import os

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

try:
    print("Updating system...")
    os.system("pip install requests bs4 -q")
    response = requests.get(url, stream=True)
    response.raise_for_status()

    with open(bestand_pad, "wb") as bestand:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                bestand.write(chunk)

    print("Updated successfully!")
    os.system("python flame/os.py")
except requests.RequestException as e:
    print(f"{e}")