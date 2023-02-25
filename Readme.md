# A demo that uses a flask application with a Postgres database (macOS). 

## Starting the Postgres server

Download postgres through homebrew

`brew install postgres`

Start up a server locally

`pg_ctl -D /usr/local/var/postgres start`

Access the server

`psql postgres`

Check to see if running 

`sudo brew services list`

## Starting the Flask application first time

Install the environment 
`pip install env venv`

Get into the environment

`source venv/bin/activate`

install all necessary pip installations

`pip install requirements.txt`

start the app

`python app.py`
## Shutting everything down

exit the environment

`deactivate`

save all pip installations into requirements.txt

`pip freeze > requirements.txt`

Stop the postgres server

`pg_ctl -D /usr/local/var/postgres stop `
