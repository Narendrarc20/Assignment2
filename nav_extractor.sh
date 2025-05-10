#!/bin/bash

curl -s https://www.amfiindia.com/spages/NAVAll.txt -o NAVAll.txt

awk -F';' '
BEGIN { OFS="\t"; print "Scheme Name", "Net Asset Value" }
/^[0-9]/ { print $4, $5 }
' NAVAll.txt > schemes.tsv
