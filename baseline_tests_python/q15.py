import sqlite3
import time
import tracemalloc

# Connect to SQLite database
# Change 'your_database.db' to the path of your SQLite database file
conn = sqlite3.connect('C:\\Users\\hp-guest\\Desktop\\tpch\\tpch.db')
cursor = conn.cursor()

# The query to be executed
query = """
with
 revenue0 as
         (select
                 l_suppkey as supplier_no,
                 sum(l_extendedprice * (1 - l_discount)) as total_revenue
         from
                 lineitem
         where
                 l_shipdate >= date ('1995-06-01')
                 and l_shipdate < date ('1995-06-01', '+3 months')
         group by
                 l_suppkey)
 select
         s_suppkey,
         s_name,
         s_address,
         s_phone,
         total_revenue
 from
         supplier,
         revenue0
 where
         s_suppkey = supplier_no
         and total_revenue = (
                 select
                         max(total_revenue)
                 from
                         revenue0
         )
 order by
         s_suppkey;
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
