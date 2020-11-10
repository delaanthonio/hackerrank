#!/usr/bin/env bash

test_dir="$(pwd)"
input_file="$test_dir/input_file.txt"
output_solution="$test_dir/output_solution.txt"
output_brute="$test_dir/output_brute.txt"

for i in {1..10}; do
    $test_dir/gen.py $i >$input_file
    $test_dir/solution.py <$input_file >$output_solution
    $test_dir/brute.py <$input_file >$output_brute
    if diff -wqZ --brief $output_solution $output_brute >/dev/null; then
        echo "Passed test: $i"
        continue
    fi
    echo "Failed test: $i"
    cat $input_file
    echo "$(diff --color=always $output_solution $output_brute)"
    break
done
