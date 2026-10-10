#!/bin/bash


echo "Enter Any Name : "
read name

echo "Your Name is : $name"

echo -n "Enter Your Age : "
read age

if [ $age -ge 18 ];then
	echo "You Are Eligible for Vote in India...!"
else
	echo "Sorry! You Are not Eligible for Vote in India...!"
fi


no=5
for(( i=1 ; i<=$no ; i++ ))
do
        echo $i
done

exit 0
