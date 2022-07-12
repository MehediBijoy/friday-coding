# Assignment API Endpoints

## Project setup

clone project, and use `pipenv` or `virtualenv` for create environment. I use `pipenv` so navigate in project root directory and command `pipenv install` after installed then command `pipenv shell` for activate virtualenv. I also given `postman collections` for testing api endpoints.

## Project run

`python manage.py runserver` for run project server. Also run
` pipenv run celery -A config worker --beat --scheduler django --loglevel=info` for background tasks.
Make sure redis installed your machine for running `celery`.

## Api endpoints

### `Registration user`

api endpoints: `/user/registration/`

sample post request data

```json
{
  "name": "Mehedi Hasan",
  "email": "test1@gmail.com",
  "phone_number": "01726720012",
  "password": "test12345"
}
```

### `user access token`

api endpoints: `/api/token/`

sample post request data

```json
{
  "email": "mehedi@gmail.com",
  "password": "test12345"
}
```

access token use to make balance transfer, and get transaction history.

### `Transaction Balance`

api endpoints: `/transfer_balance/`

sample post request data

- required jwt token

```json
[
  {
    "recipient": "2",
    "amount": 10,
    "scheduled_at": "2022-07-03 10:40:03"
  },
  {
    "recipient": "2",
    "amount": 10,
    "scheduled_at": "2022-07-10 09:19:03"
  },
  {
    "recipient": "2",
    "amount": 10,
    "scheduled_at": null
  }
]
```

Here `recipient` userid who received the balance,
if `scheduled_at` null or less then current date it's mean send balance now, otherwise transaction turned at scheduled date.

### `Transaction History`

api endpoints: `/transaction_history/`

- required jwt token

This request is get request.
