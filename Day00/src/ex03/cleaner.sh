#!/bin/sh
head -n1 ../ex02/hh_sorted.csv > hh_position.csv
IFS=','
while read -r id created_at name has_test alternative_url; do
    new_name=""
    if echo "$id" | grep -qv "id"; then
        if echo "$name" | grep -q "Junior\|junior"; then
            if [ -z "$new_name" ]; then
                new_name="Junior"
            fi
        fi
        if echo "$name" | grep -q "Middle\|middle"; then
            if [ -z "$new_name" ]; then
                new_name="Middle"
            else
                new_name="${new_name}/Middle"
            fi
        fi
        if echo "$name" | grep -q "Senior\|senior"; then
            if [ -z "$new_name" ]; then
                new_name="Senior"
            else
                new_name="${new_name}/Senior"
            fi
        fi
        if [ -z "$new_name" ]; then
            new_name="-"
        fi
        echo "$id,$created_at,$new_name,$has_test,$alternative_url" >> hh_position.csv
    fi
done < ../ex02/hh_sorted.csv
