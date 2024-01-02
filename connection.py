import pymysql

db_config = {
    'user':'root',
    'host':'localhost',
    'database':'tuition2',
    'password':'SQLP@ssw0rd',
    'autocommit':'True'
}

connection = pymysql.connect(**db_config)