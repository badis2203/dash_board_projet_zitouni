import requests
from bs4 import BeautifulSoup
import os

url = "https://www.santepubliquefrance.fr/determinants-de-sante/vaccination/articles/donnees-infra-nationales-de-couverture-vaccinale-papillomavirus-humains-hpv"

response = requests.get(url)

if response.status_code == 200:
    print("Page téléchargée avec succès.")
    soup = BeautifulSoup(response.content, "html.parser")

    links = soup.find_all("a", string=lambda text: text and "région" in text.lower())

    if links:
        print(f"{len(links)} fichiers régionaux trouvés.")
        os.makedirs("fichiers_regionaux", exist_ok=True)  # Créer un dossier pour sauvegarder les fichiers

        for i, link in enumerate(links):
            file_url = "https://www.santepubliquefrance.fr" + link['href']  # Construire l'URL complète
            file_name = f"fichiers_regionaux/fichier_regional_{i + 1}.csv"  # Nom du fichier à sauvegarder

            file_response = requests.get(file_url)
            if file_response.status_code == 200:
                with open(file_name, "wb") as file:
                    file.write(file_response.content)
                print(f"Fichier {i + 1} sauvegardé sous {file_name}.")
            else:
                print(f"Erreur lors du téléchargement du fichier {i + 1} : {file_response.status_code}")
    else:
        print("Aucun fichier régional trouvé.")
else:
    print(f"Erreur lors du téléchargement de la page : {response.status_code}")
