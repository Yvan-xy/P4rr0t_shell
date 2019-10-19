#!/bin/bash
PATH=/bin:/sbin:/usr/bin:/usr/sbin/:/usr/local/bin:/usr/local/sbin:~/bin
s=10
touch /tmp/abc
while [ "$s" != "0" ]
do
find ./ -name "*.php*" -type f -anewer /tmp/abc -print0 | xargs -0 rm -rf {}
find ./ -name "*.PHP*"  -type f -anewer /tmp/abc -print0 | xargs -0 rm -rf {}
find ./ -name "*.pht"  -type f -anewer /tmp/abc -print0 | xargs -0 rm -rf {}
find ./ -name "*.PHP"  -type f -anewer /tmp/abc -print0 | xargs -0 rm -rf {}
find ./ -name "*.pHp"  -type f -anewer /tmp/abc -print0 | xargs -0 rm -rf {}
#find /tmp/test -type f -newer abc | xargs
echo "=========" 
sleep 0.000001
done
