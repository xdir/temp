#!/bin/bash
git pull

sudo cp api.service /etc/systemd/system/api.service

systemctl daemon-reload

sudo systemctl start api
sudo systemctl enable api

#sudo systemctl start monitoring
#sudo systemctl enable monitoring
