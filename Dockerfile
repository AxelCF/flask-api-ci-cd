# Utilise Python 3.12 slim
FROM python:3.12-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier requirements.txt et installer les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste de l’application
COPY . .

# Exposer le port
EXPOSE 5000

# Lancer l’application
CMD ["python", "app.py"]
