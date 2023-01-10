#!/bin/sh
sudo docker volume create mysql
sudo docker volume create grafana
sudo docker volume create stc
sudo docker run -p 3306:3306 --name mysql -e MYSQL_ROOT_PASSWORD='$ani-Matic2855' -d --restart always -v mysql:/var/lib/mysql mysql
sudo docker run -p 80:3000 --name grafana -d --restart always -v grafana:/var/lib/grafana grafana/grafana-oss
# sudo docker run --name stc -d --restart always -v stc:/stc stc


# docker build for logic
# sudo docker build --network=host stc .sudo d