from connection import connection

cursor = connection.cursor()

create_students_query = """
create table `Students`(
    `Student_Id` varchar(10) PRIMARY KEY,
    `Name` varchar(25) NOT NULL,
    `Standard` int not null,
    `Fees` int not null
)
"""

create_fee_query = """
create table `Fee_Status`(
    `S.No` int auto_increment primary key,
    `Student_Id`varchar(10) not null,
    `Fees` int not null,
    `Status` varchar(10) Default Null,
    FOREIGN KEY(`Student_Id`) REFERENCES Students(`Student_Id`)
)
"""
# cursor.execute(create_students_query)
# cursor.execute(create_fee_query)


insert_query = """
insert into Students(`Name`, `Standard`, `Fees`)
values
("Kira", 11, 800),
("Nina", 7, 500),
("Shino", 9, 700)
"""

# cursor.execute(insert_query)