#!/bin/bash
git pull

systemctl start api
systemctl enable api

systemctl start monitoring
systemctl enable monitoring
