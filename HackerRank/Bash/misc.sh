#!/bin/bash

BEGINCOMMENT
  Your task is to use for loops to display only odd natural numbers from 1 to 99. 
ENDCOMMENT

for i in {1..99..2}
  do 
     echo $i
 done


BEGINCOMMENT
  Four lines containing the sum (), difference (), product (), and quotient (), respectively. 
ENDCOMMENT

read num1
read num2
echo `expr $num1 + $num2`
echo `expr $num1 - $num2`
echo `expr $num1 \* $num2`
echo `expr $num1 / $num2`


BEGINCOMMENT
  Given two integers, X and Y, identify whether X>Y or X<Y or X=Y.
Exactly one of the following lines: 
- X is less than Y 
- X is greater than Y 
- X is equal to Y
ENDCOMMENT

read num1
read num2
if [ $num1 -gt $num2 ]; then #VERY sensitive to spacing in the conditional
    echo "X is greater than Y"
elif [ $num1 -lt $num2 ]; then
    echo "X is less than Y"
elif [ $num1 -eq $num2 ]; then
    echo "X is equal to Y"
fi
