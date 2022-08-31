FROM python:3.10-alpine3.16

COPY Pipfile /
COPY Pipfile.lock /

RUN pip install pipenv
RUN pipenv install

COPY . .
RUN pipenv run python manage.py migrate
CMD ["pipenv", "run","gunicorn", "--bind", ":8000", "--workers", "3", "config.wsgi"]
