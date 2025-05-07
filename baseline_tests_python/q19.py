import sqlite3
import time
import tracemalloc

# Connect to SQLite database
# Change 'your_database.db' to the path of your SQLite database file
conn = sqlite3.connect('C:\\Users\\hp-guest\\Desktop\\tpch\\tpch.db')
cursor = conn.cursor()

# The query to be executed
query = """
select
         sum(l_extendedprice* (1 - l_discount)) as revenue
 from
         lineitem,
         part
 where
         (
                 p_partkey = l_partkey
                 and p_brand = 'Brand#43'
                 and p_container in ('SM CASE', 'SM BOX', 'SM PACK', 'SM PKG')
                 and l_quantity >= 3 and l_quantity <= 3 + 10
                 and p_size between 1 and 5
                 and l_shipmode in ('AIR', 'AIR REG')
                 and l_shipinstruct = 'DELIVER IN PERSON'
         )
         or
         (
                 p_partkey = l_partkey
                 and p_brand = 'Brand#25'
                 and p_container in ('MED BAG', 'MED BOX', 'MED PKG', 'MED PACK')
                 and l_quantity >= 10 and l_quantity <= 10 + 10
                 and p_size between 1 and 10
                 and l_shipmode in ('AIR', 'AIR REG')
                 and l_shipinstruct = 'DELIVER IN PERSON'
         )
         or
         (
                 p_partkey = l_partkey
                 and p_brand = 'Brand#24'
                 and p_container in ('LG CASE', 'LG BOX', 'LG PACK', 'LG PKG')
                 and l_quantity >= 22 and l_quantity <= 22 + 10
                 and p_size between 1 and 15
                 and l_shipmode in ('AIR', 'AIR REG')
                 and l_shipinstruct = 'DELIVER IN PERSON'
         );
"""

# Start tracking memory usage
tracemalloc.start()

# Measure the start time
start_time = time.perf_counter()

# Execute the query
cursor.execute(query)
results = cursor.fetchall()

# Measure the end time
end_time = time.perf_counter()

# Measure memory usage
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

# Output the results
print("Query Results:")
for row in results:
    print(row)

# Output performance metrics
print(f"\nQuery execution time: {end_time - start_time:.4f} seconds")
print(f"Peak memory usage: {peak / 1024:.2f} KB")

# Clean up
cursor.close()
conn.close()
