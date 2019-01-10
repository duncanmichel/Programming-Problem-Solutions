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
