import os
import subprocess

# Structure des dossiers
project_structure = {
    "root": ["data", "scripts", "notebooks", "dashboard"],
    "files": [
        ".gitignore",
        "README.md",
        "requirements.txt",
    ]
}

# Contenu du fichier .gitignore
gitignore_content = """__pycache__/
*.pyc
*.env
*.json
*.csv
*.db
*.log
"""

# Contenu du fichier README.md
readme_content = """# Analyse des Tendances des Films et Séries
Ce projet vise à analyser les tendances des films et séries en utilisant l'API TMDB, avec des visualisations interactives et un tableau de bord Streamlit.

## Structure
- **data/** : Contient les fichiers de données extraites (JSON, CSV).
- **scripts/** : Scripts Python pour extractions et analyses.
- **notebooks/** : Notebooks Jupyter pour analyses exploratoires.
- **dashboard/** : Scripts pour le tableau de bord Streamlit.

## Commandes utiles
- Installer les dépendances : `pip install -r requirements.txt`
- Lancer le tableau de bord : `streamlit run dashboard/app.py`
"""

# Fichiers de dépendances (requirements.txt)
requirements_content = """requests
pandas
matplotlib
seaborn
streamlit
"""

# Fonction pour créer la structure du projet
def setup_project():
    # Création des dossiers
    for folder in project_structure["root"]:
        os.makedirs(folder, exist_ok=True)
        print(f"Dossier créé : {folder}")

    # Création des fichiers
    for file in project_structure["files"]:
        if file == ".gitignore":
            with open(file, "w") as f:
                f.write(gitignore_content)
        elif file == "README.md":
            with open(file, "w") as f:
                f.write(readme_content)
        elif file == "requirements.txt":
            with open(file, "w") as f:
                f.write(requirements_content)
        print(f"Fichier créé : {file}")

    # Initialisation Git
    if not os.path.exists(".git"):
        subprocess.run(["git", "init"])
        print("Repository Git initialisé.")

    # Ajout et commit initial
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "Initialisation du projet."])
    print("Commit initial effectué.")

    print("Configuration terminée. Votre projet est prêt !")

# Exécution de la fonction
if __name__ == "__main__":
    setup_project()
