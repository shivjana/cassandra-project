# DROP TABLES

song_table_drop = "DROP TABLE IF EXISTS song_table"
users_table_drop = "DROP TABLE IF EXISTS users_table"
usage_table_drop = "DROP TABLE IF EXISTS usage_table"

# CREATE TABLES

song_table_create = ("""CREATE TABLE IF NOT EXISTS song_table (sessionId int,itemInSession int,artist text, firstName text,gender text,lastName text, level text, length double, location text, song text, userId int, PRIMARY KEY (sessionId,itemInSession))""")

users_table_create = ("""CREATE TABLE IF NOT EXISTS users_table (userId int,sessionId int, itemInSession int, artist text, firstName text,gender text, lastName text, length double, level text, location text, song text, PRIMARY KEY ((userId,sessionId),itemInSession))""")

usage_table_create = ("""CREATE TABLE IF NOT EXISTS usage_table (song text,userId int, artist text, firstName text,gender text,itemInSession int,lastName text, length double, level text, location text, sessionId int, PRIMARY KEY (song,userId))""")

# INSERT RECORDS

song_table_insert = "INSERT INTO song_table (sessionId,itemInSession,artist, firstName,gender,lastName, level, length, location, song, userId)"

users_table_insert = "INSERT INTO users_table (userId,sessionId, itemInSession, artist, firstName,gender, lastName, length, level, location, song)"

usage_table_insert = "INSERT INTO usage_table (song,userId, artist, firstName,gender,itemInSession,lastName, length, level, location, sessionId)"

# SELECT STATEMENTS

query1_select = "SELECT artist,song,length FROM song_table WHERE sessionId =338 and itemInSession=4"

query2_select = "SELECT artist,song,firstName,lastName FROM users_table WHERE userId = 10 and sessionId = 182"

query3_select = "SELECT firstName,lastName FROM usage_table WHERE song = 'All Hands Against His Own'"


# QUERY LISTS

create_table_queries = [song_table_create, users_table_create, usage_table_create]
drop_table_queries = [song_table_drop, users_table_drop, usage_table_drop]
insert_table_queries = [song_table_insert, users_table_insert, usage_table_insert]
select_table_queries = [query1_select,query2_select,query3_select]
columnList = [[8,3,0,1,2,4,6,5,7,9,10],[10,8,3,0,1,2,4,5,6,7,9],[9,10,0,1,2,3,4,5,6,7,8]]
#columnList[1] = [10,8,3,0,1,2,4,5,6,7,9]
#columnList[2] = [9,10,0,1,2,3,4,5,6,7,8]