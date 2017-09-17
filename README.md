# heroku-flask-playground
Getting started with Python (Flask) on Heroku.

## Running locally

```
pipenv install
createdb playground
alembic upgrade heads
heroku local
```

Note: You may need to update `DATABASE_URL` in `.env` to match your
local database url.

## Deploying to Heroku
```
heroku create
git push heroku master

heroku addons:create heroku-postgresql
heroku run alembic upgrade heads
heroku open
```