--MySQL server for the project:
--Database named hbnb_dev_db
--Creates a user named hbnb_dev with the password hbnb_dev_pwd on localhost.
--Gives hbnb_dev with all privileges on the hbnb_dev_db database. 
--Grants hbnb_dev the SELECT privilege on the performance database.

-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create the user if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges on hbnb_dev_db to hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant SELECT privilege on performance_schema to hbnb_dev
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Flush privileges to apply changes
FLUSH PRIVILEGES;
