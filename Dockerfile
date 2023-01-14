FROM python:3.9

ENV PYTHONUNBUFFERED 1

WORKDIR /app
EXPOSE 8000

RUN apt-get update && apt-get install -y wget gnupg && \
    echo 'deb https://apt-archive.postgresql.org/pub/repos/apt stretch-pgdg main' > /etc/apt/sources.list.d/pg.list && \
    wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - && \
    apt-get update && apt-get install -y \
        postgresql-client-12

COPY ./backend/requirements.txt /app
RUN pip3 install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "./entrypoint.sh" ]
CMD ./manage.py runserver 0.0.0.0:8000
