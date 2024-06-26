import pandas as pd
import sqlite3


stations_df = pd.read_csv(r'C:\Users\DELL\Downloads\clean_stations.csv')
measure_df = pd.read_csv(r'C:\Users\DELL\Downloads\clean_measure.csv')


print("Stations DataFrame:")
print(stations_df.head())
print("\nMeasurements DataFrame:")
print(measure_df.head())


conn = sqlite3.connect('weather_data.db')


stations_df.to_sql('stations', conn, if_exists='replace', index=False)
measure_df.to_sql('measurements', conn, if_exists='replace', index=False)


results = conn.execute("SELECT * FROM stations LIMIT 5").fetchall()

results1 = conn.execute("SELECT * FROM stations WHERE name = 'WAIMANALO EXPERIMENTAL FARM'").fetchall()


print("\nFirst 5 rows from 'stations' table:")
for row in results:
    print(row)

print("\n Row from table 'stations' where table name = 'WAIMANALO EXPERIMENTAL FARM':")
for row in results1:
    print(row)


conn.close()