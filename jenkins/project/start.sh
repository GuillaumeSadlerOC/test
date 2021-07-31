docker-compose -f ./traefik/docker-compose.yml up -d --build
docker-compose -f ./app/docker-compose.yml up -d --build
docker-compose -f ./nginx/docker-compose.yml up -d --build