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
         ps_partkey,
         sum(ps_supplycost * ps_availqty) as value
 from
         partsupp,
         supplier,
         nation
 where
         ps_suppkey = s_suppkey
         and s_nationkey = n_nationkey
         and n_name = 'CHINA'
 group by
         ps_partkey having
                 sum(ps_supplycost * ps_availqty) > (
                         select
                                 sum(ps_supplycost * ps_availqty) * 0.0001000000
                         from
                                 partsupp,
                                 supplier,
                                 nation
                         where
                                 ps_suppkey = s_suppkey
                                 and s_nationkey = n_nationkey
                                 and n_name = 'CHINA'
                 )
 order by
         value desc;
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
