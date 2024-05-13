#!/bin/bash
git pull

sudo cp api.service /etc/systemd/system/deploy.service
sudo cp api.service /etc/systemd/system/monitoring.service
sudo cp api.service /etc/systemd/system/api.service

sudo systemctl daemon-reload

sudo systemctl start deploy
sudo systemctl enable deploy

sudo systemctl start monitoring
sudo systemctl enable monitoring

sudo systemctl start api
sudo systemctl enable api