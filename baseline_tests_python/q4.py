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
         o_orderpriority,
         count(*) as order_count
 from
         orders
 where
         o_orderdate >= date ('1996-03-01')
         and o_orderdate < date ('1996-03-01', '+3 months')
         and exists (
                 select
                         *
                 from
                         lineitem
                 where
                         l_orderkey = o_orderkey
                         and l_commitdate < l_receiptdate
         )
 group by
         o_orderpriority
 order by
         o_orderpriority;
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

