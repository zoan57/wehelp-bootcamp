# 程式碼如下
```sql
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

#要求五：SQL JOIN
CREATE TABLE message(
	id BIGINT PRIMARY KEY auto_increment COMMENT '獨立編號',
	member_id BIGINT NOT null COMMENT '留言者會員編號',
    content VARCHAR(255) NOT null COMMENT '留言內容',
	like_count int unsigned NOT null DEFAULT 0 COMMENT '按讚的數量',
    time datetime NOT null default current_timestamp COMMENT '留言時間'
);
ALTER TABLE message ADD FOREIGN KEY(member_id) REFERENCES member(id);
INSERT INTO message(member_id, content) VALUES('1','哇好讚');
INSERT INTO message(member_id, content) VALUES('2','安安');
INSERT INTO message(member_id, content) VALUES('4','Test Test');
INSERT INTO message(member_id, content) VALUES('3','ctlorem200');
INSERT INTO message(member_id, content) VALUES('1','try try see');
INSERT INTO message(member_id, content) VALUES('5','The making of indebted man');
INSERT INTO message(member_id, content) VALUES('3','我愛半路咖啡');
INSERT INTO message(member_id, content) VALUES('1','掰掰台北哈囉花蓮');
INSERT INTO message(member_id, content) VALUES('2','我是機器人');
INSERT INTO message(member_id, content) VALUES('4','最近想看雲圖，但最愛Ursula Le Guinㄌ');
```
# 需截圖SQL指令的部分如下
### 要求三：SQL CRUD
#### 使⽤ SELECT 指令取得所有在 member 資料表中的會員資料
```sql
SELECT * FROM member;
```
![3-2](/week5/images/3-2.png)

#### 使⽤ SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近到遠排序。
```sql
SELECT * FROM member ORDER BY time ASC;
```
![3-3](/week5/images/3-3.png)

#### 使⽤ SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序。 ( 並非編號 2、3、4 的資料，⽽是排序後的第 2 ~ 4 筆資料 )
```sql
SELECT * FROM member ORDER BY time ASC limit 1,3;
```
![3-4](/week5/images/3-4.png)

#### 使⽤ SELECT 指令取得欄位 username 是 test的資料
```sql
SELECT * FROM member WHERE username='test';
```
![3-5](/week5/images/3-5.png)

#### 使⽤ SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料
```sql
SELECT * FROM member WHERE username='test';
```
![3-6](/week5/images/3-6.png)

#### 使⽤ UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2
```sql
SET SQL_SAFE_UPDATES=0;
UPDATE member SET name='tes2' WHERE username='test';
```
![3-7](/week5/images/3-7.png)

### 要求四：SQL Aggregate Functions
#### 取得 member 資料表中，總共有幾筆資料(幾位會員)
```sql
SELECT COUNT(name) FROM member;
```
![4-1](/week5/images/4-1.png)

#### 取得 member 資料表中，所有會員 follower_count 欄位的總和
```sql
SELECT SUM(follower_count) FROM member;
```
![4-2](/week5/images/4-2.png)

#### 取得 member 資料表中，所有會員 follower_count 欄位的平均數
```sql
SELECT AVG(follower_count) FROM member;
```
![4-3](/week5/images/4-3.png)

### 要求五：SQL JOIN
#### 確定有JOIN成功
```sql
SELECT * FROM member INNER JOIN message ON member.id=message.member_id ORDER BY member.id;
```
![5-1](/week5/images/5-1.png)

#### 使⽤ SELECT 搭配 JOIN 語法，取得所有留⾔，結果須包含留⾔者會員的姓名
```sql
SELECT member.name, message.content FROM member
INNER JOIN message ON member.id=message.member_id ORDER BY member.id;
```
![5-2](/week5/images/5-2.png)

#### 使⽤ SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留⾔，資料中須包含留⾔者會員的姓名。
```sql
SELECT member.name, message.content FROM member
INNER JOIN message ON member.id=message.member_id WHERE member.username='test' ORDER BY member.id;
```
![5-3](/week5/images/5-3.png)

#### 使⽤ SELECT、SQL Aggregate Functions 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留⾔平均按讚數。
```sql
SELECT member.username, FLOOR(AVG(message.like_count)) FROM member
INNER JOIN message ON member.id=message.member_id WHERE member.username='test'  ORDER BY member.id;
```
![5-4](/week5/images/5-4.png)




