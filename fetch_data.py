import requests
import json
from config import API_KEY, BASE_URL

def fetch_popular_movies(page=1):
    """
    Récupère les films populaires depuis l'API TMDB.
    :param page: Numéro de la page des résultats (par défaut 1).
    :return: Liste des films populaires.
    """
    url = f"{BASE_URL}/movie/popular?api_key={API_KEY}&language=en-US&page={page}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()  # Convertit la réponse en dictionnaire
        # Sauvegarder les résultats dans un fichier JSON
        with open(f"data/popular_movies_page_{page}.json", "w") as file:
            json.dump(data, file, indent=4)
        print(f"Page {page} des films populaires sauvegardée.")
        return data
    else:
        print(f"Erreur lors de la récupération des données : {response.status_code}")
        return None

if __name__ == "__main__":
    # Test de la récupération
    fetch_popular_movies()
