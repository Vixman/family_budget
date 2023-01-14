#!/bin/bash
# set -e

until psql -h "${DB_HOST:-db}" -U "${DB_USER:-postgres}"  -c '\d'; do
  echo "Postgres is unavailable - sleeping"
  sleep 1
done

echo "DB is up - continuing"

if [ "x$DJANGO_MANAGEPY_MIGRATE" = 'xon' ]; then
    /venv/bin/python manage.py migrate --noinput
fi

if [ "x$DJANGO_MANAGEPY_COLLECTSTATIC" = 'xon' ]; then
    /venv/bin/python manage.py collectstatic --noinput
fi

exec "$@"
