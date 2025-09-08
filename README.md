# Flask API - CI/CD & Monitoring

## Description

Ce projet met en place une API REST avec **Flask** pour gérer des tâches.
J’ai choisi **PostgreSQL** comme base de données (et **SQLite en mémoire** pour les tests), avec un déploiement conteneurisé via **Docker** sur **AWS Elastic Beanstalk**.
Le pipeline **CI/CD** est géré avec **GitHub Actions**, car GitHub offre une intégration plus simple et directe avec mes dépôts, ainsi qu’une communauté et une documentation très riches, ce qui correspondait mieux à mes besoins que GitLab.
Enfin, j’ai intégré **Prometheus** et **Grafana** pour la surveillance et la visualisation des métriques.
