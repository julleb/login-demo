#sudo -u postgres psql
#\i setup-db.sql

cat cleanse-db.sql | sudo -u postgres psql
