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
         o_year,
         sum(case
                 when nation = 'IRAQ' then volume
                 else 0
         end) / sum(volume) as mkt_share
 from
         (
                 select
                         strftime('%Y',o_orderdate) as o_year,
                         l_extendedprice * (1 - l_discount) as volume,
                         n2.n_name as nation
                 from
                         part,
                         supplier,
                         lineitem,
                         orders,
                         customer,
                         nation n1,
                         nation n2,
                         region
                 where
                         p_partkey = l_partkey
                         and s_suppkey = l_suppkey
                         and l_orderkey = o_orderkey
                         and o_custkey = c_custkey
                         and c_nationkey = n1.n_nationkey
                         and n1.n_regionkey = r_regionkey
                         and r_name = 'MIDDLE EAST'
                         and s_nationkey = n2.n_nationkey
                         and o_orderdate between date ('1995-01-01') and date ('1996-12-31')
                         and p_type = 'STANDARD ANODIZED BRASS'
         ) as all_nations
 group by
         o_year
 order by
         o_year;
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

