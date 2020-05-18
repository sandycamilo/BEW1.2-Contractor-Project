docker image build --compress -t docker-django-image:latest . && \
docker container run --publish 8080:8080 --env PROJECT_DB_HOST=docker.for.mac.host.internal --env DEBUG=True --env COMPRESS_ENABLED=True --env COMPRESS_OFFLINE=True --name=docker-django docker-django-image:latest

#!/bin/sh
python manage.py collectstatic --noinput
python manage.py migrate

# For Production:
gunicorn journal.wsgi --reload --workers=2 --threads=4 --worker-tmp-dir=/dev/shm --bind=0.0.0.0:8080 --log-file=- --worker-class=gthread
