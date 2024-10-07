from context import *

# create table
create_database_tables()

def register():
    connection = open_connection()
    cur = connection.cursor()
    cur.execute(
        f""" insert into users(username, password, first_name, last_name, email)
        values(
            '{input("username: ")}',
            '{input("password: ")}',
            '{input("first_name: ")}',
            '{input("last_name: ")}',
            '{input("email: ")}'
        ) """
    )
    connection.commit()
    close_connection(connection, cur)


def get_users():
    conn = open_connection()
    cur = conn.cursor()
    cur.execute("select * from users")
    users = cur.fetchall()
    close_connection(conn,cur)
    return users


def login(username, password):
    conn = open_connection()
    cur = conn.cursor()
    cur.execute(f"select * from users where username = '{username}' and password = '{password}'")
    user = cur.fetchone()
    close_connection(conn,cur)
    return user


print(login("sunatulo","1234"))


def change_password(username,password):
    conn = open_connection()
    cur = conn.cursor()
    cur.execute(f"update users set password='{input('Enter new password: ')}'  where username = '{username}' and password = '{password}'")
    conn.commit()
    close_connection(conn,cur)

# change_password('sunat','1234')



def delete(username):
    conn = open_connection()
    cur = conn.cursor()
    a = input("do you want delete your acaunt: ")
    if a == "Yes":
        cur.execute(f"delete from users where username = '{username}'")
    else :
        pass
    conn.commit()
    close_connection(conn,cur)

delete('sunat')

    
