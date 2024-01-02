from connection import connection
cursor = connection.cursor()

def add_student(data):
    query = """
    insert into Students(`Name`, `Standard`, `Fees`)
    values(%s, %s, %s)
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