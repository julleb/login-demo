

create database logindemo;

\c logindemo;


create table users (
username varchar(50) PRIMARY KEY,
password varchar(100),
salt varchar(50)
);

\dt
