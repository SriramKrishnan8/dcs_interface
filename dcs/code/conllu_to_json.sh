#!/bin/bash
mkdir -p ../data/json/
#python3 run_for_all.py ../data/json/ ../data/conllu/files/*.conllu
for d in ../data/conllu/files/*/; do
    echo "$d"
    python3 run_for_all.py ../data/json_data/ "$d"*.conllu
done
