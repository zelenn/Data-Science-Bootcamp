#!/bin/sh
header=$(head -n 1 ../ex01/hh.csv)

tail -n +2 ../ex01/hh.csv | sort -t',' -k2,2 -k1,1n > sorted_body.csv

echo "$header" > hh_sorted.csv
cat sorted_body.csv >> hh_sorted.csv
rm sorted_body.csv
