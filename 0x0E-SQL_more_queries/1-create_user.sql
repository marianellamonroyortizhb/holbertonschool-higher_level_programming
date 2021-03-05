-- Creates an user
-- Check if the user exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
GRANT SELECT ON hbtn_0d_2.* TO 'user_02d_2' @'localhost' IDENTIFIED BY 'user_0d2_2_pwd';
