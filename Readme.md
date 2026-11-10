# Application Flask + MariaDB

Application web Python (Flask) dont la page d'accueil indique si la connexion
à la base de données MariaDB fonctionne :

- `Database Connection Status: Connected` : la base répond
- `Database Connection Status: Disconnected` : la base est injoignable

## Prérequis

- [Docker](https://docs.docker.com/get-docker/)
- (Optionnel) Python 3.13 pour lancer l'application sans Docker

## Variables d'environnement

| Variable      | Valeur par défaut | Rôle                    |
|---------------|-------------------|-------------------------|
| `DB_HOST`     | `localhost`       | Adresse de la base      |
| `DB_USER`     | `root`            | Utilisateur MariaDB     |
| `DB_PASSWORD` | *(vide)*          | Mot de passe MariaDB    |
| `DB_NAME`     | `test`            | Nom de la base          |

## Lancer l'application avec Docker

1. Créer un réseau Docker pour que les deux conteneurs puissent communiquer :

   ```bash
   docker network create tp-net
   ```

2. Démarrer la base MariaDB :

   ```bash
   docker run -d --name db --network tp-net \
     -e MARIADB_ALLOW_EMPTY_ROOT_PASSWORD=yes \
     -e MARIADB_DATABASE=test \
     mariadb:11
   ```

3. Construire l'image de l'application :

   ```bash
   docker build -t flask-app .
   ```

4. Démarrer l'application :

   ```bash
   docker run -d --name app --network tp-net -p 5000:5000 \
     -e DB_HOST=db \
     flask-app
   ```

5. Ouvrir <http://localhost:5000> : la page doit afficher
   `Database Connection Status: Connected`.

6. Pour tout arrêter et nettoyer :

   ```bash
   docker rm -f app db
   docker network rm tp-net
   ```

## Utiliser l'image publiée sur GHCR : 
ghcr.io/bln53z00/evaluation-final-devops:6ec163e43318a9f186ee50b2b4717183ad77168b