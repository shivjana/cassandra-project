OBJECTIVE

Sparkify is a music streaming app and as part of user-analysis, they analyze the data which are mainly composed of log files on songs and user activity. The primary objective of their analysis is to determine what songs users are mostly interested in.

DATABASE DESIGN

So as part of this, the database must be designed in such a way that that we can execute 3 optimized select queries on 3 different tables created for each query. The 3 tables are song table, users table and usage table where song table gives us information about the song artists, title and length played with sessionId 338 and item number in session 4, users table gives us information about the users firstname and lastname, the song titles listened bye user with userId 10 and sessionId 182, usage table which gives us information about all the users who listened to the song 'All Hands Against His Own'. For the songs table, sessionId as partition key and items in session as clustering column is that we need to divide the data into multiple sessions and then order the data based on the item number. For the users table, userId and sessionId as partition key and item in session as clustering columns is that we need to partition the data based on multiple users and sessions and then order the data based on the item number. For the usage table, userId and sessionId as partition key and item in session as clustering columns is that we need to partition the data based on multiple users and sessions and then order the data based on the item number.

ETL PIPELINING

The dataset event_data is a directory of CSV files partitioned by date. The CSV files are processed and written into a file event_datafile_new.csv to create a denormalized set. The data is modeled based on the select queries that need to be run.

CODE EXECUTION

In order to execute the python files:

1) First create event_datafile_new.csv file

python process_csv_data.py

2) Then run cassandra_connect.py to create database, create tables, insert values into tables and execute select queries

python cassandra_connect.py