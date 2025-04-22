#automate statistics for query processing and recording the data
import sqlite3
import subprocess


database_file = '/home/taya/Downloads/tpch.db'
sql_file = '/home/taya/PycharmProjects/databaseFinal/tpchQueriesSQLlTE/q1.sql' 
num_executions = 30
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

    cursor.execute(sql_query)
    result = cursor.fetchone()[0]

    # Execute .stats command and capture output
    process = subprocess.Popen(['sqlite3', database_file, '.stats'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    stats_output = stdout.decode('utf-8').strip()

    results.append({
        'execution': i + 1,
        'result': result,
        'stats': stats_output
    })

    conn.close()

for record in results:
    print(f"Execution {record['execution']}:")
    print(f"  Result: {record['result']}")
    print(f"  Stats:\n{record['stats']}")
    print("-" * 20)
