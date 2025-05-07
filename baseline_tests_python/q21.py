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
         s_name,
         count(*) as numwait
 from
         supplier,
         lineitem l1,
         orders,
         nation
 where
         s_suppkey = l1.l_suppkey
         and o_orderkey = l1.l_orderkey
         and o_orderstatus = 'F'
         and l1.l_receiptdate > l1.l_commitdate
         and exists (
                 select
                         *
                 from
                         lineitem l2
                 where
                         l2.l_orderkey = l1.l_orderkey
                         and l2.l_suppkey <> l1.l_suppkey
         )
         and not exists (
                 select
                         *
                 from
                         lineitem l3
                 where
                         l3.l_orderkey = l1.l_orderkey
                         and l3.l_suppkey <> l1.l_suppkey
                         and l3.l_receiptdate > l3.l_commitdate
         )
         and s_nationkey = n_nationkey
         and n_name = 'INDIA'
 group by
         s_name
 order by
         numwait desc,
         s_name;
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
