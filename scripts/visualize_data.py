import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json

# Charger les données depuis le fichier JSON
with open("data/popular_movies_page_1.json", "r") as file:
    data = json.load(file)

# Transformer les résultats en DataFrame pandas
movies = pd.DataFrame(data["results"])

# Nettoyer les données (par exemple, convertir les dates)
movies["release_year"] = pd.to_datetime(movies["release_date"], errors='coerce').dt.year

# Graphique 1 : Répartition des films par note moyenne
def plot_vote_distribution():
    plt.figure(figsize=(10, 6))
    sns.histplot(movies["vote_average"], bins=10, kde=True, color="blue")
    plt.title("Répartition des notes moyennes des films", fontsize=16)
    plt.xlabel("Note moyenne", fontsize=12)
    plt.ylabel("Nombre de films", fontsize=12)
    plt.savefig("data/notes moyennes.png")

    plt.show()

# Graphique 2 : Nombre de films par année de sortie
def plot_movies_by_year():
    plt.figure(figsize=(12, 6))
    movies_per_year = movies["release_year"].value_counts().sort_index()
    sns.barplot(x=movies_per_year.index, y=movies_per_year.values, palette="viridis")
    plt.title("Nombre de films par année de sortie", fontsize=16)
    plt.xlabel("Année", fontsize=12)
    plt.ylabel("Nombre de films", fontsize=12)
    plt.xticks(rotation=45)
    plt.savefig("data/films par annees.png")

    plt.show()

# Graphique 3 : Top 10 des films les mieux notés
def plot_top_rated_movies():
    top_movies = movies.sort_values(by="vote_average", ascending=False).head(10)
    plt.figure(figsize=(12, 6))
    sns.barplot(
        x=top_movies["vote_average"], 
        y=top_movies["title"], 
        palette="coolwarm", 
        orient="h"
    )
    plt.title("Top 10 des films les mieux notés", fontsize=16)
    plt.xlabel("Note moyenne", fontsize=12)
    plt.ylabel("Titre du film", fontsize=12)
    plt.savefig("data/films mieux notes .png")

    plt.show()

# Lancer les graphiques
if __name__ == "__main__":
    plot_vote_distribution()
    plot_movies_by_year()
    plot_top_rated_movies()
