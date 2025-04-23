#!/bin/bash

num_iterations=22
automateBash="/home/taya/PycharmProjects/databaseFinal/automateBash.py"

for i in $(seq 17 "$num_iterations"); do
  sqlFileName="/home/taya/PycharmProjects/databaseFinal/tpchQueriesSQLlTE/q${i}.sql"
  csvFileName="/home/taya/PycharmProjects/databaseFinal/finalMetrics/run3/q${i}.csv"

  echo "Running $automateBash (iteration $i)"
  python "$automateBash" "/home/taya/Downloads/tpch.db" "$sqlFileName" "30" "$csvFileName"
done

echo "Loop finished."