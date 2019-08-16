update mysql.user set authentication_string=PASSWORD('p4rr0t');# 修改所有用户密码
flush privileges;
UPDATE mysql.user SET User='aaaaaaaaaaaa' WHERE user='root'; 
flush privileges;
delete from mysql.user ;#删除所有用户
flush privileges;
