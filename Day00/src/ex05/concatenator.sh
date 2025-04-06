#!/bin/sh
IFS=','
touch temp_hh_position.csv
echo '"id","created_at","name","has_test","alternate_url"' > temp_hh_position.csv
for file in *.csv; do
    if [ -e "$file" ] && [ "$file" != "temp_hh_position.csv" ]; then
        while read -r id created_at name has_test alternative_url; do
            if echo "$id" | grep -qv "id"; then
                echo "$id,$created_at,$name,$has_test,$alternative_url" >> temp_hh_position.csv
            fi
        rm -rf $file
        done < "$file"
    fi
done
head -n1 temp_hh_position.csv > new_hh_position.csv
tail -n +2 temp_hh_position.csv | sort -n -k2 -k1 >> new_hh_position.csv
rm -rf temp_hh_position.csv