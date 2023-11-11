FROM ubuntu:22.04

RUN apt -y update
RUN apt -y upgrade

RUN apt -y install apache2 python3 python3-pip libapache2-mod-wsgi-py3
RUN pip install --upgrade pip

COPY ./rest_api_site.conf /etc/apache2/sites-available/000-default.conf

RUN mkdir empty
RUN mkdir logs
RUN mkdir app
WORKDIR /app
COPY requirements.txt .
COPY manage.py .
COPY fish_shop_backend ./fish_shop_backend
COPY products ./products

RUN pip install -r requirements.txt
EXPOSE 80

ENTRYPOINT  "apache2ctl" "-D" "FOREGROUND"