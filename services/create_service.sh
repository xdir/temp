#!/bin/bash
git pull

sudo cp -rf deploy.service /etc/systemd/system/deploy.service
sudo cp -rf monitoring.service /etc/systemd/system/monitoring.service
sudo cp -rf api.service /etc/systemd/system/api.service

sudo systemctl daemon-reload

sudo systemctl start deploy
sudo systemctl enable deploy
sudo systemctl restart deploy

sudo systemctl start monitoring
sudo systemctl enable monitoring
sudo systemctl restart monitoring

sudo systemctl start api
sudo systemctl enable api
sudo systemctl restart api