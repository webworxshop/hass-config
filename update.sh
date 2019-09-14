#!/bin/bash
set -e

cd /mnt/docker-data/home-assistant || exit
docker-compose -p ha pull
docker-compose -p ha down
docker-compose -p ha up -d --remove-orphans
docker system prune -fa
docker volume prune -f
exit

