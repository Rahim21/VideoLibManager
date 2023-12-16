# Dockerfile for VideoLibManager
FROM python:3.8-slim

WORKDIR /app

# Copier les fichiers requis
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copie le répertoire source (local) dans la destination (image Docker)
COPY . .

# Exposer le port
EXPOSE 5002

# Commande par défaut pour lancer l'application
CMD ["python", "app.py"]
