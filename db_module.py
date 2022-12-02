import sqlite3
# импорт загрузчика from_db_cursor
from prettytable import from_db_cursor


def create_db():
    con = sqlite3.connect('CompanyEmployees.db')
    print('--> Connected to SQLITE.')
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS employees(
        id INT PRIMARY KEY NOT NULL,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        sex TEXT NOT NULL,
        date_of_birth TEXT NOT NULL
    );            
    ''')
    
    cur.execute('PRAGMA foreign_keys=ON')

    cur.execute('''CREATE TABLE IF NOT EXISTS positions(
        id INT PRIMARY KEY NOT NULL,
        name TEXT NOT NULL,
        salary REAL NOT NULL CHECK(salary > 0),
        employees_id INT NOT NULL,
        FOREIGN KEY(employees_id) REFERENCES employees(id)
    );
    ''')

    cur.execute('''CREATE TABLE IF NOT EXISTS status(
        id INT PRIMARY KEY NOT NULL,
        hired_at TEXT NOT NULL,
        fired_at TEXT,
        employees_id INT NOT NULL,
        FOREIGN KEY(employees_id) REFERENCES employees(id)
    );
    ''')

    cur.execute('''CREATE TABLE IF NOT EXISTS contacts(
        id INT PRIMARY KEY NOT NULL,
        address TEXT NOT NULL,
        phone_num TEXT NOT NULL,
        email TEXT NOT NULL,
        employees_id INT NOT NULL,
        FOREIGN KEY(employees_id) REFERENCES employees(id)
    );
    ''')

    con.commit()
    print('--> DataBase has created.')
    con.close()
    print('--> Connection to SQLITE has closed.')


data_1 = [(1, 'Ivan', 'Ivanov', 'male', '1995-05-28'),
            (2, 'Petr', 'Ivanov', 'male', '1999-11-18'),
            (3, 'Ivan', 'Petrov', 'male', '2000-10-08'),
            (4, 'Larisa', 'Durova', 'female', '1996-05-04'),
            (5, 'Olga', 'Sidorova', 'female', '2001-06-22'),
            (6, 'Petr', 'Petrov', 'male', '2002-12-18'),
            (7, 'Ulia', 'Baranova', 'female', '1998-09-09'),
            (8, 'Boris', 'Britva', 'male', '1994-07-20'),
            (9, 'Svetlana', 'Baranova', 'female', '2000-10-28'),
            (10, 'Boris', 'Sedov', 'male', '1999-12-01')]
data_2 = [(1, 'Manager', 50000.0, 1),
            (2, 'Driver', 50000.0, 2),
            (3, 'Programmer', 70000.0, 3),
            (4, 'SysAdmin', 45000.0, 4),
            (5, 'Desiner', 55000.0, 5),
            (6, 'Accountant', 45000.0, 6),
            (7, 'Lawyer', 50000.0, 7),
            (8, 'Cleaner', 30000.0, 8),
            (9, 'Programmer', 70000.0, 9),
            (10, 'Desiner', 55000.0, 10)]
data_3 = [(1, '2018-12-06', '', 1),
            (2, '2019-11-11', '', 2),
            (3, '2018-07-08', '2022-10-02', 3),
            (4, '2020-10-09', '', 4),
            (5, '2020-01-07', '2021-12-20', 5),
            (6, '2019-03-16', '', 6),
            (7, '2021-08-20', '', 7),
            (8, '2015-04-10', '', 8),
            (9, '2022-10-03', '', 9),
            (10, '2019-01-22', '', 10)]
data_4 = [(1, 'Moscow, Lenin str. 49', '+79267412369', 'mail1@mail.ru', 1),
            (2, 'Moscow, Lenin str. 101', '+79224962185', 'mail2@mail.ru', 2),
            (3, 'Moscow, Gorky str. 84/3', '+79005472222', 'mail3@mail.ru', 3),
            (4, 'Moscow, Sakharov str. 3', '+79231475698', 'mail4@mail.ru', 4),
            (5, 'Moscow, Fillipov str. 16', '+79078942369', 'mail5@mail.ru', 5),
            (6, 'Moscow, Beregovaya str. 150', '+79024751298', 'mail6@mail.ru', 6),
            (7, 'Moscow, Astrakhan str. 2', '+79174568912', 'mail7@mail.ru', 7),
            (8, 'Moscow, Koroleva str. 12', '+79014692178', 'mail8@mail.ru', 8),
            (9, 'Moscow, Vavilova str. 203', '+79061892147', 'mail9@mail.ru', 9),
            (10, 'Moscow, Vavilova str. 155', '+79201237951', 'mail10@mail.ru', 10)]

data_temp = (7, 'Ulia', 'Baranova', 'female', '1998-09-09')

def fill_db(query, data):
    con = sqlite3.connect('CompanyEmployees.db')
    print('--> Connected to SQLITE.')
    cur = con.cursor()
    # cur.executemany('INSERT INTO employees VALUES(?, ?, ?, ?, ?)', data_1)
    # cur.executemany('INSERT INTO positions VALUES(?, ?, ?, ?)', data_2)
    # cur.executemany('INSERT INTO status VALUES(?, ?, ?, ?)', data_3)
    # cur.executemany('INSERT INTO contacts VALUES(?, ?, ?, ?, ?)', data_4)
    #cur.execute('INSERT INTO employees VALUES(?, ?, ?, ?, ?)', data)
    cur.execute(query, data)

    con.commit()
    print('--> Changes have saved successfuly!')
    con.close()
    print('--> Connection to SQLITE has closed.')


def read_db(query, data):
    con = sqlite3.connect('CompanyEmployees.db')
    print('--> Connected to SQLITE.')
    cur = con.cursor()
    #cur.execute('SELECT first_name, last_name FROM employees WHERE sex="female" AND last_name="Baranova"')
    #cur.execute('SELECT first_name, last_name FROM employees WHERE first_name="Ulia"')
    #cur.execute('SELECT * FROM employees WHERE last_name=?', (data, ))
    cur.execute(query, (data, ))
    #res = cur.fetchall()
    # создание таблицы из объекта курсора
    res = from_db_cursor(cur)

    #con.commit()
    con.close()
    print('--> Connection to SQLITE has closed.')

    return res

    
def read_db_all(query):
    con = sqlite3.connect('CompanyEmployees.db')
    print('--> Connected to SQLITE.')
    cur = con.cursor()
    cur.execute(query)
    # создание таблицы из объекта курсора
    res = from_db_cursor(cur)

    con.close()
    print('--> Connection to SQLITE has closed.')

    return res


def change_db(query, data):
    con = sqlite3.connect('CompanyEmployees.db')
    print('--> Connected to SQLITE.')
    cur = con.cursor()
    cur.execute(query, data)

    con.commit()
    print('--> Changes have saved successfuly!')
    con.close()
    print('--> Connection to SQLITE has closed.')


def delete_db(query, data):
    con = sqlite3.connect('CompanyEmployees.db')
    print('--> Connected to SQLITE.')
    cur = con.cursor()
    cur.execute(query, data)

    con.commit()
    print('--> Chosen data has deleted.')
    con.close()
    print('--> Connection to SQLITE has closed.')