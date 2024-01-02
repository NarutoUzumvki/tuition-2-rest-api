from connection import connection

cursor = connection.cursor()

create_query = """
create table `Students`(
    `Student_Id` int AUTO_INCREMENT PRIMARY KEY,
    `Name` varchar(25) NOT NULL,
    `Standard` int not null,
    `Fees` int not null
)
"""

# cursor.execute(create_query)

insert_query = """
insert into Students(`Name`, `Standard`, `Fees`)
values
("Kira", 11, 800),
("Nina", 7, 500),
("Shino", 9, 700)
"""

# cursor.execute(insert_query)