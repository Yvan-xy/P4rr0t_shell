# P4rr0t_shell

---  

### 目录结构  
```shell
.
├── a.php
├── awd.sh
├── flag
├── flag.txt
├── log
├── README.md
├── seg.log
└── target.txt
```

### 主要功能  

主要支持php木马,支持批量拿flag,群控,命令控制,批量扫描,不死.

使用方式如下:  
```shell
    ____   __ __               ____   __
   / __ \ / // /  _____ _____ / __ \ / /_
  / /_/ // // /_ / ___// ___// / / // __/
 / ____//__  __// /   / /   / /_/ // /_
/_/       /_/  /_/   /_/    \____/ \__/
[+]1. CommandMode
[+]2. ReadAllFlag
[+]3. SegmentScan
[+]4. Exit
>1
[+]Input Target url>
127.0.0.1/.a.php
www-data@/var/www/html>ls -al
ls -al
ls -alstring(521) "total 48
drwxr-xr-x 5 root root  4096 Aug 16 14:43 .
drwxr-xr-x 9 root root  4096 Aug 14 14:30 ..
-rwxrwxrwx 1 root root   330 Aug 16 14:45 .a.php
-rw-r--r-- 1 root root   107 Aug 15 00:00 .index.php
-rw-r--r-- 1 root root   152 Aug 15 21:54 a.php
drwxr-xr-x 3 root root  4096 Aug 16 16:45 awd
drwxr-xr-x 2 root root  4096 Aug 14 14:30 blockchain
-rw-r--r-- 1 root root 10480 Feb 22 14:19 index.apache.html
-rw-r--r-- 1 root root   612 Oct 17  2018 index.nginx-debian.html
drwxr-xr-x 2 root root  4096 Aug 14 14:30 shell
"
www-data@/var/www/html>
```

### 配置方式
在target.txt中填写靶机的url地址,flag将输入到flag.txt中.  

```plain
http://127.0.0.1/.a.php
http://192.168.100.22/.fuck.php
```
连接脚本的密码在awd.sh中进行修改.
