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
         c_custkey,
         c_name,
         sum(l_extendedprice * (1 - l_discount)) as revenue,
         c_acctbal,
         n_name,
         c_address,
         c_phone,
         c_comment
 from
         customer,
         orders,
         lineitem,
         nation
 where
         c_custkey = o_custkey
         and l_orderkey = o_orderkey
         and o_orderdate >= date ('1993-12-01')
         and o_orderdate < date ('1993-12-01', '+3 months')
         and l_returnflag = 'R'
         and c_nationkey = n_nationkey
 group by
         c_custkey,
         c_name,
         c_acctbal,
         c_phone,
         n_name,
         c_address,
         c_comment
 order by
         revenue desc;
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


