-- settings.sql
CREATE DATABASE costumes;
CREATE USER costumeuser WITH PASSWORD 'costumes';
GRANT ALL PRIVILEGES ON DATABASE costumes TO costumeuser;