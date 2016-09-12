#!/bin/bash

for i in $(seq 1 100); do if ! (( $i % 3 )) && ! (($i % 5 )); then echo "CracklePop"; elif ! (( $i % 3 )); then echo "Crackle"; elif ! (( $i % 5 )); then echo "Pop"; else echo $i; fi; done;

# This was my first bash script I wrote in January 2016.
# It was my answer to code CracklePop from the RC Start application.
# RC Start is an initiative from the Recurse Center in New York to provide mentorship to new programmers.
