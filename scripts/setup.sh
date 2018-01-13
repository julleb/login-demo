#sudo -u postgres psql
#\i setup-db.sql

cat setup-db.sql | sudo -u postgres psql
