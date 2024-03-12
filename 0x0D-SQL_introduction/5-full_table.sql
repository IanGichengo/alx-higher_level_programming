-- prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server.
SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_DEFAULT FROM COLUMNS WHERE TABLE_SCHEMA='$1' AND TABLE_NAME='first_table';
