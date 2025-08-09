#!/bin/sh

csvjson ../ex03/hh_positions.csv > tmp.json

jq -r '
  map(select(.name != "-")) |
  group_by(.name) |
  map({name: .[0].name, count: length}) |
  sort_by(-.count)
' tmp.json | \
in2csv -f json > hh_uniq_positions.csv

rm tmp.json
