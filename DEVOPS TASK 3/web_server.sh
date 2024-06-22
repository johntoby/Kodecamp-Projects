#!/bin/bash

# Update package list
sudo apt-get update

# Install Nginx
sudo apt-get install -y nginx

# Start Nginx service
sudo systemctl start nginx
sudo systemctl enable nginx

# Configure firewall to allow Nginx
sudo ufw allow 'Nginx HTTP'
sudo ufw enable