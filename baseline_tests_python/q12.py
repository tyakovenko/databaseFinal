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
         l_shipmode,
         sum(case
                 when o_orderpriority = '1-URGENT'
                         or o_orderpriority = '2-HIGH'
                         then 1
                 else 0
         end) as high_line_count,
         sum(case
                 when o_orderpriority <> '1-URGENT'
                         and o_orderpriority <> '2-HIGH'
                         then 1
                 else 0
         end) as low_line_count
 from
         orders,
         lineitem
 where
         o_orderkey = l_orderkey
         and l_shipmode in ('AIR', 'RAIL')
         and l_commitdate < l_receiptdate
         and l_shipdate < l_commitdate
         and l_receiptdate >= date ('1994-01-01')
         and l_receiptdate < date ('1994-01-01', '+1 years')
 group by
         l_shipmode
 order by
         l_shipmode;
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
