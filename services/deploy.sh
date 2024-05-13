#!/bin/bash
git pull

sudo systemctl daemon-reload

sudo systemctl start monitoring
sudo systemctl enable monitoring