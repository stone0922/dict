import pymysql

db = pymysql.connect("localhost","root","123456")
cursor = db.cursor()

try:
    cursor.execute('create database dict;')
    cursor.execute('use dict;')
    cursor.execute('''create table words(
                    id int(11) auto_increment primary key,
                    word varchar(32) not null,
                    interpret text not null);
                    ''')
    cursor.execute('''create table user(
                    id int(11) auto_increment primary key,
                    name varchar(32) not null,
                    passwd varchar(16) default '000000');
                    ''')
    cursor.execute('''create table hist(
                    id int(11) auto_increment primary key,
                    name varchar(32) not null,
                    word varchar(32) not null,
                    time varchar(64));
                    ''')
    db.commit()
    print('OK')
except Exception as e:
    db.rollback()
    print(e)

cursor.close()
db.close()