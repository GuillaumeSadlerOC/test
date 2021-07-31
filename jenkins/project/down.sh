docker-compose -f ./nginx/docker-compose.yml down -v
docker-compose -f ./app/docker-compose.yml down -v
# docker-compose -f ./jenkins/docker-compose.yml down -v
docker-compose -f ./traefik/docker-compose.yml down -v