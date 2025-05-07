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
         supp_nation,
         cust_nation,
         l_year,
         sum(volume) as revenue
 from
         (
                 select
                         n1.n_name as supp_nation,
                         n2.n_name as cust_nation,
                         strftime('%Y',l_shipdate) as l_year,
                         l_extendedprice * (1 - l_discount) as volume
                 from
                         supplier,
                         lineitem,
                         orders,
                         customer,
                         nation n1,
                         nation n2
                 where
                         s_suppkey = l_suppkey
                         and o_orderkey = l_orderkey
                         and c_custkey = o_custkey
                         and s_nationkey = n1.n_nationkey
                         and c_nationkey = n2.n_nationkey
                         and (
                                 (n1.n_name = 'PERU' and n2.n_name = 'IRAQ')
                                 or (n1.n_name = 'IRAQ' and n2.n_name = 'PERU')
                         )
                         and l_shipdate between date ('1995-01-01') and date ('1996-12-31')
         ) as shipping
 group by
         supp_nation,
         cust_nation,
         l_year
 order by
         supp_nation,
         cust_nation,
         l_year;
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

