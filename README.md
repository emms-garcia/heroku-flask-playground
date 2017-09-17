# heroku-flask-playground
Getting started with Python (Flask) on Heroku.

## Running locally

Make sure you have Python [installed properly](http://install.python-guide.org). Also, install the [Heroku Toolbelt](https://toolbelt.heroku.com/) and [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh
$ pipenv install
$ createdb playground
$ alembic upgrade heads

$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

Note: You may need to update `DATABASE_URL` in `.env` to match your local database url.

## Deploying to Heroku
```sh
$ heroku create
$ git push heroku master

$ heroku addons:create heroku-postgresql
$ heroku run alembic upgrade heads
$ heroku open
```
