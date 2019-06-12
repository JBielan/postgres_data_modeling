import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *

def get_files(filepath):
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))
    
    return all_files

def process_song_file(cur, filepath):
    song_files = get_files('data/song_data')
    df = pd.DataFrame()
    for filepath, i in zip(song_files, range(len(song_files))):
        if '.ipynb' not in filepath:
            temp = pd.read_json(filepath, lines=True)
            df = df.append(temp.loc[0], ignore_index=True)

    song_data = df[['song_id', 'title', 'artist_id', 'year', 'duration']]
    value = song_data.values[0]
    song_data = list(value) 
    cur.execute(song_table_insert, song_data)

    artist_data = df[['artist_id', 'artist_name', 'artist_location', 'artist_latitude', 'artist_longitude']]
    value = artist_data.values[0]
    artist_data = list(value)
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    log_files = get_files('data/log_data')
    df = pd.DataFrame()
    for filepath, i in zip(log_files, range(len(log_files))):
        if '.ipynb' not in filepath:
            temp = pd.read_json(filepath, lines=True)
            df = df.append(temp.loc[0], ignore_index=True)

    df = df.loc[df['page'] == 'NextSong']

    df['ts'] = pd.to_datetime(df['ts'], unit='ms')

    ts = df['ts']
    time_data = (ts, ts.dt.hour, ts.dt.day, ts.dt.weekofyear, ts.dt.month, ts.dt.year, ts.dt.weekday)
    column_labels = ('timestamp', 'hour', 'day', 'week', 'month', 'year', 'weekday')
    time_dic = dict(zip(column_labels, time_data))
    time_df = pd.DataFrame.from_dict(time_dic)

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    user_df = df[['userId', 'firstName', 'lastName', 'gender', 'level']]

    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    for index, row in df.iterrows():

        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        songplay_data = (index, row.ts, row.userId, row.level, songid, artistid, row.sessionId, row.location, row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()
