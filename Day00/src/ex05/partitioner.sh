#!/bin/sh
IFS=','
while read -r id created_at name has_test alternative_url; do
    if echo "$id" | grep -qv "id"; then
        filename=$(echo "$created_at" | cut -c2-11)
        if [ -e "$filename.csv" ]; then
            echo "$id,$created_at,$name,$has_test,$alternative_url" >> "$filename.csv"
        else
            head -n1 ../ex03/hh_position.csv > "$filename.csv"
            echo "$id,$created_at,$name,$has_test,$alternative_url" >> "$filename.csv"
        fi
    fi
done < ../ex03/hh_position.csv
