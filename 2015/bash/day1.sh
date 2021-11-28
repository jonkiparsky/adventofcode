#!/usr/bin/env bash

# Day 1, part 1
up=${1//')'/''}
down=${1//'('/''}
echo $((${#up}-${#down}))
echo Part 1: ${#up}-${#down}

#Day 1, part 2

(( floor=0 ))
for (( i=0; i<${#1}; i++ )); do
    c="${1:$i:1}"
    case $c in

	"(") (( floor++ ));;
	")") (( floor-- ));;
    esac
    if (( $floor<0)); then
	echo $i;
	exit 0;
    fi;
done;
echo "didn't enter basement!"
exit 1

    
    
	 
	 
    

