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
         nation,
         o_year,
         sum(amount) as sum_profit
 from
         (
                 select
                         n_name as nation,
                         strftime('%Y',o_orderdate) as o_year,
                         l_extendedprice * (1 - l_discount) - ps_supplycost * l_quantity as amount
                 from
                         part,
                         supplier,
                         lineitem,
                         partsupp,
                         orders,
                         nation
                 where
                         s_suppkey = l_suppkey
                         and ps_suppkey = l_suppkey
                         and ps_partkey = l_partkey
                         and p_partkey = l_partkey
                         and o_orderkey = l_orderkey
                         and s_nationkey = n_nationkey
                         and p_name like '%antique%'
         ) as profit
 group by
         nation,
         o_year
 order by
         nation,
         o_year desc;
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

