#!/bin/bash

num_iterations=21
automateBash="/home/taya/PycharmProjects/databaseFinal/automateBash.py"

for i in $(seq 21 "$num_iterations"); do
  sqlFileName="/home/taya/PycharmProjects/databaseFinal/tpchQueriesSQLlTE/q${i}.sql"
  csvFileName="/home/taya/PycharmProjects/databaseFinal/finalMetrics/run4/q${i}.csv"

  echo "Running $automateBash (iteration $i)"
  python "$automateBash" "/home/taya/Downloads/tpch.db" "$sqlFileName" "40" "$csvFileName"
done

echo "Loop finished."