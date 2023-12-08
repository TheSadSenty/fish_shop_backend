#!/bin/bash

sudo apt-get update
sudo apt-get install postgresql

sudo -u postgres psql

#CREATE USER root WITH PASSWORD 'root';
#ALTER ROLE root SUPERUSER;
#Выход из сессии PostgreSQL можно осуществить, нажав Ctrl+D.

sudo -u postgres createdb DB --owner=root

python manage.py makemigrations
python manage.py migrate
