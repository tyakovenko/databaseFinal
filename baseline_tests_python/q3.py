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
         l_orderkey,
         sum(l_extendedprice * (1 - l_discount)) as revenue,
         o_orderdate,
         o_shippriority
 from
         customer,
         orders,
         lineitem
 where
         c_mktsegment = 'MACHINERY'
         and c_custkey = o_custkey
         and l_orderkey = o_orderkey
         and o_orderdate < date ('1995-03-21')
         and l_shipdate > date ('1995-03-21')
 group by
         l_orderkey,
         o_orderdate,
         o_shippriority
 order by
         revenue desc,
         o_orderdate;
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

