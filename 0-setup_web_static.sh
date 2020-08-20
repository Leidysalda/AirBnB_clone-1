#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

#sudo addgroup ubuntu && useradd -md /home/ubuntu -g ubuntu -s /bin/bash ubuntu
sudo apt-get -y update
sudo apt-get -y install nginx

sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/

sudo echo "
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
" | sudo tee /data/web_static/releases/test/index.html


sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

new="location /hbnb_static {\n\talias /data/web_static/current;\n}"
sudo sed -i "/listen 80 default_server;/a $new" /etc/nginx/sites-available/default

sudo service nginx restart
