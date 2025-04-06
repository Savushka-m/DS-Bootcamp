#!/bin/sh 
head -n1 ../ex01/hh.csv > hh_sorted.csv
tail -n +2 ../ex01/hh.csv | sort -n -k2 -k1 >> hh_sorted.csv
