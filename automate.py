#automate statistics for query processing and recording the data
import sqlite3
import time
import subprocess
import pandas as pd
import psutil  # Import the psutil library



database_file = "/home/taya/Downloads/tpch.db"
numQueries = 22 #the number of sql query files to be processed
num_executions = 30

def get_peak_memory():
    process = psutil.Process()
    return process.memory_info().rss / 1024000 # Resident Set Size in kb


def runOneSQL(database_file, sql_file, num_executions, csvSave):
    #we do not record the query execution results here
    results = []

    # Read the SQL query from the .sql file
    try:
        with open(sql_file, 'r') as f:
            sql_query = f.read().strip()
    except FileNotFoundError:
        print(f"Error: SQL file '{sql_file}' not found.")
        exit()

    for i in range(num_executions):
        conn = sqlite3.connect(database_file)
        cursor = conn.cursor()

        # Measure memory before execution
        memory_before = get_peak_memory()

        start_time = time.perf_counter()
        cursor.execute(sql_query)
        query_result = cursor.fetchall()  # Fetch all results for this query
        end_time = time.perf_counter()
        execution_time = end_time - start_time

        # Measure memory after execution
        memory_after = get_peak_memory()
        memory_used = memory_after - memory_before

        # Execute .stats command and capture output
        process_stats = subprocess.Popen(['sqlite3', database_file, '.stats'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout_stats, stderr_stats = process_stats.communicate()
        stats_output = stdout_stats.decode('utf-8').strip()

        # Execute EXPLAIN QUERY PLAN and capture output
        process_explain = subprocess.Popen(['sqlite3', database_file, 'EXPLAIN QUERY PLAN ' + sql_query], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout_explain, stderr_explain = process_explain.communicate()
        explain_output = stdout_explain.decode('utf-8').strip()

        print(f"done with execution {i + 1}")

        results.append({
            'execution': i + 1,
            #'query_result': query_result,
            'execution_time': execution_time,
            'stats': stats_output,
            'explain_query_plan': explain_output,
            #'memory_before_bytes': memory_before,
            #'memory_after_bytes': memory_after,
            'approximate_memory_used_bytes': memory_used
        })

        conn.close()

    """ for record in results:
        print(f"Execution {record['execution']}:")
        print(f"  Query Result:")
        for row in record['query_result']:
            print(f"    {row}")
        print(f"  Execution Time: {record['execution_time']:.6f} seconds")
        print(f"  Stats:\n{record['stats']}")
        print("-" * 20)
    """

    # save results into a pandas dataframe for further processing
    # Create a Pandas DataFrame from the results
    df = pd.DataFrame(results)
    # You can now further analyze or save the DataFrame to a file (e.g., CSV)
    df.to_csv(csvSave, index=False)


#run all files
"""for i in range(22) :
    runOneSQL(database_file,
              f"/home/taya/PycharmProjects/databaseFinal/tpchQueriesSQLlTE/q{i+1}.sql",
              num_executions,
              f"/home/taya/PycharmProjects/databaseFinal/finalMetrics/q{i+1}Run.csv")
    print(f"done processing file {i+1}")
"""

runOneSQL(database_file,
              f"/home/taya/PycharmProjects/databaseFinal/tpchQueriesSQLlTE/q1.sql",
              num_executions,
              f"/home/taya/PycharmProjects/databaseFinal/finalMetrics/q1Run.csv")






















