from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine, select


engine = create_engine('sqlite:///weather_data.db')

metadata = MetaData()
metadata.reflect(bind=engine)

print(metadata.tables.keys())

stations = Table('stations', metadata, autoload=True, autoload_with=engine)

query1 = select([stations]).limit(5)  
query2 = select([stations]).where(stations.c.name == 'WAIMANALO EXPERIMENTAL FARM')  

results1 = engine.execute(query1).fetchall()

print("Results from query 1:")
for r in results1:
    print(r)

results2 = engine.execute(query2).fetchall()

print("\nResults from query 2:")
for r in results2:
    print(r)