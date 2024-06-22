#!/bin/bash

# Update package list
sudo apt update

# Install MySQL server
sudo apt install -y mysql-server

# Start MySQL service
sudo systemctl start mysql
sudo systemctl enable mysql

# Secure MySQL installation
sudo mysql_secure_installation <<EOF

y
vagrant
vagrant
y
y
y
y
EOF

# Create a test database and user
sudo mysql -u root -pvagrant -e "CREATE DATABASE test_db;"
sudo mysql -u root -pvagrant -e "CREATE USER 'test_user'@'%' IDENTIFIED BY 'test_pass';"
sudo mysql -u root -pvagrant -e "GRANT ALL PRIVILEGES ON test_db.* TO 'test_user'@'%';"
sudo mysql -u root -pvagrant -e "FLUSH PRIVILEGES;"

# Allow remote access to MySQL
sudo sed -i "s/bind-address.*/bind-address = 0.0.0.0/" /etc/mysql/mysql.conf.d/mysqld.cnf
sudo systemctl restart mysql