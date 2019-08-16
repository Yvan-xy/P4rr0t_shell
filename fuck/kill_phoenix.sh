#!/usr/bin/env sh
ps -aux|grep 'www-data'|awk '{print $2}'|xargs kill -9

