#!/bin/sh

if [ "$#" -lt 1 ]; then
  echo "Usage: $0 <vacancy name>"
  exit 1
fi

VACANCY=$(echo "$*" | sed 's/ /%20/g')

curl -H "User-Agent: s21-school" "https://api.hh.ru/vacancies?text=$VACANCY&per_page=20" | jq '.' > hh.json
