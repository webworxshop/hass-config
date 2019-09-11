#!/bin/bash
set -e

cd /mnt/docker-data/home-assistant || exit
docker-compose pull
docker-compose down
docker-compose up -d
docker system prune -fa
docker volume prune -f
exit

