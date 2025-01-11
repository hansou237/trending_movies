import pandas as pd
import json

# Charger les données depuis le fichier JSON
with open("data/popular_movies_page_1.json", "r") as file:
    data = json.load(file)

# Extraire la liste des films
movies = pd.DataFrame(data["results"])

# Afficher les premières lignes
print("Aperçu des films populaires :")
print(movies[["title", "vote_average", "release_date"]])

# Calculer la note moyenne
print(f"\nNote moyenne des films : {movies['vote_average'].mean()}")

# Analyser les films par année de sortie
movies["release_year"] = pd.to_datetime(movies["release_date"], errors='coerce').dt.year
print("\nNombre de films par année :")
print(movies["release_year"].value_counts())
