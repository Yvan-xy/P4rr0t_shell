#!/usr/bin/env python3
import base64
def rm_db(db_user,my_db_passwd):
    cmd = "/usr/bin/mysql -h localhost -u%s %s -e '"%(db_user,my_db_passwd)
    db_name = ['performance_schema','mysql','flag']
    for db in db_name:
        cmd += "drop database %s;"%db
    cmd += "'"
    return cmd  

