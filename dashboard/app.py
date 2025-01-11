import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json

# Charger les données
import os
import json
import pandas as pd

def load_data():
    # Récupérer le répertoire du script actuel
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # Construire un chemin relatif au fichier JSON
    filepath = os.path.join(base_dir, "../data/popular_movies_page_1.json")
    
    # Vérifier si le fichier existe
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Le fichier {filepath} est introuvable. Assurez-vous qu'il a été généré.")
    
    # Charger les données JSON
    with open(filepath, "r") as file:
        data = json.load(file)
    
    # Retourner un DataFrame pandas avec les résultats
    return pd.DataFrame(data["results"])

movies = load_data()
# Créer la colonne release_year à partir de release_date
movies["release_year"] = pd.to_datetime(movies["release_date"], errors='coerce').dt.year


# Titre de l'application
st.title("Analyse des Tendances des Films Populaires")
st.markdown("Ce tableau de bord vous permet d'explorer les tendances des films populaires basées sur les données TMDB.")

# Options pour l'utilisateur
st.sidebar.header("Options")
year_filter = st.sidebar.slider("Filtrer par année de sortie", int(movies["release_year"].min()), int(movies["release_year"].max()), (2010, 2023))
rating_filter = st.sidebar.slider("Filtrer par note moyenne", 0.0, 10.0, (5.0, 10.0))

# Appliquer les filtres
filtered_movies = movies[(movies["release_year"].between(*year_filter)) & (movies["vote_average"].between(*rating_filter))]

# Graphique 1 : Répartition des notes moyennes
st.subheader("Répartition des notes moyennes")
fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(filtered_movies["vote_average"], bins=10, kde=True, ax=ax, color="blue")
ax.set_title("Répartition des notes moyennes des films")
ax.set_xlabel("Note moyenne")
ax.set_ylabel("Nombre de films")
st.pyplot(fig)

# Graphique 2 : Nombre de films par année
st.subheader("Nombre de films par année")
fig, ax = plt.subplots(figsize=(12, 6))
movies_per_year = filtered_movies["release_year"].value_counts().sort_index()
sns.barplot(x=movies_per_year.index, y=movies_per_year.values, ax=ax, palette="viridis")
ax.set_title("Nombre de films par année de sortie")
ax.set_xlabel("Année")
ax.set_ylabel("Nombre de films")
st.pyplot(fig)

# Tableau des films
st.subheader("Tableau des films filtrés")
st.dataframe(filtered_movies[["title", "release_year", "vote_average", "overview"]])

# Top 10 des films les mieux notés
st.subheader("Top 10 des films les mieux notés")
top_movies = filtered_movies.sort_values(by="vote_average", ascending=False).head(10)
st.table(top_movies[["title", "vote_average", "release_year"]])
