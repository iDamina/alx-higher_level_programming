-- creating the database hbtn_0d_2 and the user user_0d_2
-- creating hbtn_0d_2 database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- creating a user user_0d_2
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
-- granting SELECT privileges to the user
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
