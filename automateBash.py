#same file as automate but now this will run through the command line to avoid data polution
#each file was run 30 times, processing 1 file at a time
import sys
import sqlite3
import subprocess
import time
import pandas as pd

def runOneSQL (database_file, sql_file, num_executions, csvSave):
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

        start_time = time.perf_counter()
        cursor.execute(sql_query)
        query_result = cursor.fetchall()  # Fetch all results for this query
        end_time = time.perf_counter()
        execution_time = end_time - start_time

        # Execute .stats command and capture output
        process = subprocess.Popen(['sqlite3', database_file, '.stats'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        stats_output = stdout.decode('utf-8').strip()

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
            'explain_query_plan': explain_output
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


if __name__ == "__main__":
    if len(sys.argv) == 5:
        database_file = sys.argv[1]
        sql_file = sys.argv[2]
        num_executions = int(sys.argv[3])
        csvSave = sys.argv[4]
        runOneSQL(database_file, sql_file, num_executions, csvSave)
    else:
        print("Not enough arguments")