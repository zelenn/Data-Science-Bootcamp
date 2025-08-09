#!/bin/sh
output="concatenated.csv"
first=1
for file in *.csv; do
    [ "$file" = "$output" ] && continue
    if [ $first -eq 1 ]; then
        cat "$file" > "$output"
        first=0
    else
        tail -n +2 "$file" >> "$output"
    fi
done
