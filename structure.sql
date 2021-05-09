CREATE TABLE wordsonline (
    id INT AUTO_INCREMENT UNIQUE,
    channel varchar(50) PRIMARY KEY,
    words text,
    pass varchar(100) DEFAULT null
);

drop table wordsonline;

update wordsonline set words='hello' where channel='general'
IF @@ROWCOUNT=0
   insert into wordsonline(channel, words) values('general','hello');


IF EXISTS(select * from wordsonline where channel='general')
   update wordsonline set words='hello' where channel='general'
ELSE
   insert into wordsonline(channel, words) values('general','hello');
   

IF 'general' is unique 
INSERT INTO wordsonline (channel, words) VALUES("general", "hello");



describe wordsonline;


delete from wordsonline where id = 2;
INSERT INTO wordsonline (channel, words, pass) VALUES("snotes", "hello", "test") ON DUPLICATE KEY UPDATE words = 'hi';
select * from wordsonline order by id;
select * from wordsonline order by id;


INSERT INTO wordsonline(words)
VALUES ('hello');

UPDATE wordsonline SET words = 'ahhh';


SELECT CHECKSUM_AGG(binary_integer(*)) FROM wordsonline;

select * from wordsonline;
