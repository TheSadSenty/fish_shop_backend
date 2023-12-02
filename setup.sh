#!/bin/sh
docker container exec -it backend /usr/bin/python3 /app/manage.py migrate
docker container exec -it backend /usr/bin/python3 /app/manage.py createsuperuser --no-input