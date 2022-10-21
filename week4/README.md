```
mySQL=
SHOW DATABASES;
SHOW TABLES;

#要求⼆：建立資料庫和資料表
CREATE DATABASE website;
USE website;
CREATE TABLE member(
	id BIGINT PRIMARY KEY auto_increment COMMENT '獨立編號',
    name VARCHAR(255) NOT null COMMENT '姓名',
	username VARCHAR(255) NOT null COMMENT '帳戶名稱',
    password VARCHAR(255) NOT null COMMENT '帳戶密碼',
    follower_count int unsigned NOT null DEFAULT 0 COMMENT '追蹤者數量',
    time datetime NOT null default current_timestamp COMMENT '註冊時間'
);

#使⽤ INSERT 指令新增資料到 member 資料表中
INSERT INTO member(name, username, password) VALUES('unknown', 'test', 'test');
INSERT INTO member(name, username, password) VALUES('Andrew', 'andrew', 'andrew123');
INSERT INTO member(name, username, password) VALUES('Inu', 'lokah', 'lokah123');
INSERT INTO member(name, username, password) VALUES('Pangcah', 'amis', 'amis123');
INSERT INTO member(name, username, password) VALUES('viva', 'la', 'vida');

#使⽤ SELECT 指令取得所有在 member 資料表中的會員資料
SELECT * FROM member;
```
