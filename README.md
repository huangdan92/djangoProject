# pythonWebDemo
# djangoProject

#数据库
CREATE TABLE IF NOT EXISTS `person`(
   `id` INT UNSIGNED AUTO_INCREMENT,
   `name` VARCHAR(100) NOT NULL,
   `context` VARCHAR(40) NOT NULL,
   `sex` VARCHAR(40) NOT NULL,
   PRIMARY KEY ( `id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

#入口
http://127.0.0.1:8000/user_list/