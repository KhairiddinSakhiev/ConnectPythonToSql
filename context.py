from secret import database_password
import psycopg2

def open_connection():
    conn = psycopg2.connect(database = "EducationDB", 
                        user = "postgres", 
                        host= 'localhost',
                        password = database_password,
                        port = 5432)
    return conn


def close_connection(conn, cur):
    cur.close()
    conn.close()


def create_database_tables():
    conn = open_connection()
    cursor = conn.cursor()
    cursor.execute(
        """ CREATE TABLE IF NOT EXISTS users(
            id serial primary key,
            username varchar(30) unique not null,
            password varchar(8) not null,
            first_name varchar(30) null , 
            last_name varchar(30) null, 
            email varchar(100) not null unique,
            is_active boolean default True,
            created_at timestamp default now()
        ); """
    )
    conn.commit()
    close_connection(conn, cursor)