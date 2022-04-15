FROM nikolaik/python-nodejs:python3.10-nodejs17-slim

WORKDIR /usr/src/app

RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get -y install --no-install-recommends python3-dev postgresql postgresql-contrib python3-psycopg2 libpq-dev gcc
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/*


RUN pip install --upgrade pip
RUN pip install poetry
COPY pyproject.toml .
RUN poetry config virtualenvs.create false
RUN poetry install

WORKDIR /usr/src/app/frontend
COPY ./frontend/package.json .
RUN npm install
COPY ./frontend .
RUN npm run build
WORKDIR /usr/src/app

COPY . .

RUN python manage.py collectstatic

CMD gunicorn --bind=0.0.0.0:8000 devproject.wsgi