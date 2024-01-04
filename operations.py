from connection import connection
from utils import *
cursor = connection.cursor()

def add_student(data):
    student_id = create_random()
    data.append(student_id)
    query = """
    insert into Students(`Name`, `Standard`, `Fees`, `Student_Id`)
    values(%s, %s, %s, %s)
    """
    cursor.execute(query, data)


def retrieve_data(id):
    query = "Select * from Students where `Student_Id`=%s"
    cursor.execute(query, id)
    data = cursor.fetchone()

    if data:
        column_names = [column[0] for column in cursor.description]
        data = dict(zip(column_names, data))
    return data


def update_data(data):
    query = "Update Students set `Name`=%s, `Standard`=%s, `Fees`=%s where `Student_Id`=%s"
    cursor.execute(query, data)


def remove_data(id):
    query = "delete from Students where `Student_Id`=%s"
    cursor.execute(query, id)

def pay_fees(id, status):
    get_fees_query="select `Fees` from Students where `Student_Id`=%s"
    cursor.execute(get_fees_query, id)
    fee = cursor.fetchone()
    insert_query = """
    insert into Fee_Status(`Student_Id`, `Fees`, `Status`)
    values(%s, %s, %s)
    """
    cursor.execute(insert_query, (id, fee[0], status))