FROM ubuntu:22.04

RUN apt -y update
RUN apt -y upgrade

RUN apt -y install apache2 python3 python3-pip libapache2-mod-wsgi-py3
RUN pip install --upgrade pip

COPY ./rest_api_site.conf /etc/apache2/sites-available/000-default.conf

RUN mkdir logs
RUN mkdir app
WORKDIR /app
RUN mkdir media
COPY . .

RUN pip install -r requirements.txt

RUN cp -r /usr/local/lib/python3.10/dist-packages/django/contrib/admin/static/ ./static/

EXPOSE 80

ENTRYPOINT  "apache2ctl" "-D" "FOREGROUND"