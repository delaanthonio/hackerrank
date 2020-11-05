#!/usr/bin/env bash

input_file="input_file.txt"
output_solution="output_solution.txt"
output_brute="output_brute.txt"

for i in {1..10}; do
    ./gen.py $i >$input_file
    ./solution.py <$input_file >$output_solution
    ./brute.py <$input_file >$output_brute
    if diff -wqZ --brief $output_solution $output_brute > /dev/null; then
        echo "Passed test: $i"
        continue
    fi
    echo "Failed test: $i"
    cat $input_file
    echo "$(diff --color=always $output_solution $output_brute)"
    break
done
