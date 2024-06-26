from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine, select

# Create an SQLite engine
engine = create_engine('sqlite:///weather_data.db')

# Reflect all tables in the database
metadata = MetaData()
metadata.reflect(bind=engine)

# Print table names (optional)
print(metadata.tables.keys())

# Assuming 'stations' table is one of the reflected tables or defined explicitly
stations = Table('stations', metadata, autoload=True, autoload_with=engine)

# Define the select queries using SQLAlchemy's select function
query1 = select([stations]).limit(5)  # Select all columns, limit to 5 rows
query2 = select([stations]).where(stations.c.name == 'WAIMANALO EXPERIMENTAL FARM')  # Filter by name

# Execute the first query
results1 = engine.execute(query1).fetchall()

# Print results from the first query
print("Results from query 1:")
for r in results1:
    print(r)

# Execute the second query
results2 = engine.execute(query2).fetchall()

# Print results from the second query
print("\nResults from query 2:")
for r in results2:
    print(r)