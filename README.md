# Data Modeling with Postgres

In this project data coming from audio streaming start-up has been modeled and prepared for analytics. 

## Requirements

1. Python 3.x
2. PostgreSQL 9.4+

## Data Structure

- **Fact Table**
    - **songplayes** - records in log data associated with song plays i.e. records with page `NextSong`
        - user_id, first_name, last_name, gender, level

- **Dimension Tables**
    - **users** - users in the app
        - user_id, first_name, last_name, gender, level
    - **songs** - songs in music databse
        - song_id, title, artist_id, year, duration
    - **artists** - artists in music database
        - artist_id, name, location, lattitude, longitude
    - **time** - timestamps of records in **songplays** broken down into specific units
        - start_time, hour, day, week, month, year, weekday

Client was oriented on analytics as well as on data validity so relational database like Postgres seems to be a good choice. 

## How to run a demonstrative ETL

As simple as those 2 comments in a command line:

    python create.py
    python etl.py
    
After that to see the process works properly, you can open `test.ipynb` and run all cells.