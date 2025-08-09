#!/bin/sh

# CSV → JSON
csvjson ../ex02/hh_sorted.csv > tmp.json

jq 'map({
  id: .id,
  created_at: .created_at,
  name: (
    (
      [
        (if .name | test("Junior") then "Junior" else empty end),
        (if .name | test("Middle") then "Middle" else empty end),
        (if .name | test("Senior") then "Senior" else empty end)
      ] | unique | join("/") | if . == "" then "-" else . end
    )
  ) | tostring,
  has_test: .has_test,
  alternate_url: .alternate_url
})' tmp.json > tmp_clean.json

# JSON → CSV
in2csv tmp_clean.json > hh_positions.csv

rm tmp.json tmp_clean.json
