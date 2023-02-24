##Start up a server
pg_ctl -D /usr/local/var/postgres start

##Access the server
psql postgres

##Check to see if running 
brew services list

##Stop the Postgres server
brew services stop postgresql
