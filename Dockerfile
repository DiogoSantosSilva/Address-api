FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app

ENV  GEO_KEY="AIzaSyDTK0igIQTCi5EYKL9tzOIJ9N6FUASGZos"
ENV DJANGO_KEY="=(u@e99cg6frf!qwb@!=)gy6u&-cw6p+fl4_^@1+c)t@v+k*%l"

RUN apt-get update && apt-get upgrade -y && apt-get install -y \
libsqlite3-dev

RUN pip install -U pip setuptools

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/
RUN  chmod +x  /app/docker-entrypoint.sh
ENTRYPOINT ["/app/docker-entrypoint.sh"]