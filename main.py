import requests

# Votre clé API
api_key = "VOTRE_CLE_API"

# Exemple : Rechercher des films populaires
url = f"https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=fr-FR&page=1"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Erreur : {response.status_code}")
