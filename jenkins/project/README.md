## APP
> Django application
> host: app1.localhost
> port: 80 

## JENKINS
> Jenkins
> host: jenkins.localhost:8080
> port: 8080
username: guillaume, password: password@

## NGINX
> Files server
> host: app1.localhost/static/
> port: 80

## SELENIUM
> Files server

## TRAEFIK
> Reverse proxy
> host: traefik.localhost
> port: 80, :8080, :443
username: user, password: password

### Lancer Selenium
> Prérequis : Que l'application soit lancée
> Lancez le script bash Selenium depuis le repertoire nommé Selenium

### Lancer les tests Django
https://docs.djangoproject.com/fr/3.2/topics/testing/overview/
> Prérequis : Que l'application soit lancée avec sa base de données
> Effectuez la commande suivante : docker exec -it django_app_1 python manage.py test flatpage.tests

## Ébauche de la pipeline
> Prérequis : Il doit y avoir Docker et Docker compose installé par l'outil qui lance la pipeline

git clone https://github.com/GuillaumeSadlerOC/devops_p8.git
# STAGE 1 > PREBUILD
./start.sh