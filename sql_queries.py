# DROP TABLES

songplay_table_drop = "DROP table songplay"
user_table_drop = "DROP table user"
song_table_drop = "DROP table song"
artist_table_drop = "DROP table artist"
time_table_drop = "DROP table time"

# CREATE TABLES

songplay_table_create = ("CREATE TABLE IF NOT EXISTS songplays (songplay_id int NOT NULL, start_time timestamp NOT NULL, user_id int NOT NULL, level text, song_id text, artist_id text, session_id numeric NOT NULL, \
location text, user_agent text)")

user_table_create = ("CREATE TABLE IF NOT EXISTS users (user_id int NOT NULL, first_name text, last_name text, gender text, level text)")

song_table_create = ("CREATE TABLE IF NOT EXISTS songs (song_id text NOT NULL, title text, artist_id text NOT NULL, year int, duration numeric)")

artist_table_create = ("CREATE TABLE IF NOT EXISTS artists (artist_id text NOT NULL, name text, location text, latitude numeric, longitude numeric)")

time_table_create = ("CREATE TABLE IF NOT EXISTS time (start_time timestamp, hour int, day int, week int, month int, \
year int, weekday text)")

# INSERT RECORDS

songplay_table_insert = ("INSERT INTO songplays (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")

user_table_insert = ("INSERT INTO users (user_id, first_name, last_name, gender, level) VALUES (%s, %s, %s, %s, %s)")

song_table_insert = ("INSERT INTO songs (song_id, title, artist_id, year, duration) VALUES (%s, %s, %s, %s, %s)")

artist_table_insert = ("INSERT INTO artists (artist_id, name, location, latitude, longitude) VALUES (%s, %s, %s, %s, %s)")


time_table_insert = ("INSERT INTO time (start_time, hour, day, week, month, year, weekday) VALUES (%s, %s, %s, %s, %s, %s, %s)")

# FIND SONGS

song_select = ("SELECT song_id, artist_id FROM songs")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
