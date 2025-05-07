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
         p_brand,
         p_type,
         p_size,
         count(distinct ps_suppkey) as supplier_cnt
 from
         partsupp,
         part
 where
         p_partkey = ps_partkey
         and p_brand <> 'Brand#15'
         and p_type not like 'MEDIUM BURNISHED%'
         and p_size in (39, 26, 18, 45, 19, 1, 3, 9)
         and ps_suppkey not in (
                 select
                         s_suppkey
                 from
                         supplier
                 where
                         s_comment like '%Customer%Complaints%'
         )
 group by
         p_brand,
         p_type,
         p_size
 order by
         supplier_cnt desc,
         p_brand,
         p_type,
         p_size;
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
