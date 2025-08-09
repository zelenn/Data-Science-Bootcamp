#!/bin/sh
header=$(head -n 1 ../ex03/hh_positions.csv)
tail -n +2 ../ex03/hh_positions.csv | while IFS= read -r line; do
    date_field=$(echo "$line" | cut -d',' -f2 | tr -d '"' | cut -c1-10)
    if [ ! -f "${date_field}.csv" ]; then
        echo "$header" > "${date_field}.csv"
    fi
    echo "$line" >> "${date_field}.csv"
done
