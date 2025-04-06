#!/bin/bash
echo '"name","count"' > hh_uniq_positions1.csv
j_count=$(grep -i -E 'junior' ../ex03/hh_position.csv | wc -l)
m_count=$(grep -i -E 'middle' ../ex03/hh_position.csv | wc -l)
s_count=$(grep -i -E 'senior' ../ex03/hh_position.csv | wc -l)
echo '"Junior",'$j_count >> hh_uniq_positions1.csv
echo '"Middle",'$m_count >> hh_uniq_positions1.csv
echo '"Senior",'$s_count >> hh_uniq_positions1.csv
head -n1 hh_uniq_positions1.csv > hh_uniq_positions.csv
tail -n +2 hh_uniq_positions1.csv | sort -n -k2 >> hh_uniq_positions.csv
rm -rf hh_uniq_positions1.csv