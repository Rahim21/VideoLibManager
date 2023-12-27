# Dockerfile for API
FROM python:3.8-slim

WORKDIR /app

# Copier les fichiers requis
# COPY requirements.txt .
# COPY app.py .

# Copier l'ensemble du contenu local dans le conteneur
COPY . .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port
EXPOSE 5001

# Commande par défaut pour lancer l'application
CMD ["python", "app.py"]
