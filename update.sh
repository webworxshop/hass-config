#!/bin/bash

cd /mnt/docker-data/home-assistant
sudo apt update && sudo apt upgrade -y && sudo apt autoremove -y && sudo apt clean
docker-compose pull
docker-compose down
docker-compose up -d
docker system prune -fa
docker volume prune -f
exit

