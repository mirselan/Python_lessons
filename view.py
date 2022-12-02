import import_data, export_data, update_data, delete_data, logger
import easygui as g


def chosing_the_table():
    msg = 'Chose name of the table'
    title = 'Chosing the table'
    choices = ['employees', 'positions', 'status', 'contacts']
    choice = g.choicebox(msg, title, choices)
    return choice


def chosing_query_type(choice_2):
    res_query, query_type, questions = None, None, None
    if choice_2 == 'employees' or choice_2 == 'contacts':
        questions = '(?, ?, ?, ?, ?)'
    else:
        questions = '(?, ?, ?, ?)'
    msg = 'Chose query type'
    title = 'Query types'
    choices = ['Select all', 'Select with last name', 'Select with position', 
                'Insert row', 'Update item', 'Delete row']
    choice = g.choicebox(msg, title, choices)
    if choice == 'Select all':
        res_query = f'SELECT * FROM {choice_2}'
        query_type = 1
    elif choice =='Select with last name':
        res_query = f'SELECT * FROM {choice_2} WHERE last_name=?'
        query_type = 2
    elif choice == 'Select with position':
        res_query = f'SELECT * FROM {choice_2} WHERE name=?'
        query_type = 3
    elif choice == 'Insert row':
        res_query = f'INSERT INTO {choice_2} VALUES{questions}'
        if choice_2 == 'employees':
            query_type = 4
        elif choice_2 == 'positions':
            query_type = 5
        elif choice_2 == 'status':
            query_type = 6
        elif choice_2 == 'contacts':
            query_type = 7
    elif choice == 'Update item':
        query_type = None
        if choice_2 == 'employees':
            choicess = ['first_name', 'last_name', 'sex', 'date_of_birth']
        elif choice_2 == 'positions':
            choicess = ['name', 'salary']
        elif choice_2 == 'status':
            choicess = ['hired_at', 'fired_at']
        elif choice_2 == 'contacts':
            choicess = ['address', 'phone_num', 'email']
        msg = 'Chose what you want to change'
        title = 'Old values'
        choice_a = g.choicebox(msg, title, choicess)
        msg_2 = 'Chose condition'
        title_2 = 'Condition for better chosing row to change'
        choice_b = g.choicebox(msg_2, title_2, choicess)
        res_query = f'UPDATE {choice_2} SET {choice_a}=? WHERE {choice_b}=?'
    elif choice == 'Delete row':
        query_type = None
        if choice_2 == 'employees':
            choicess = ['first_name', 'last_name', 'sex', 'date_of_birth']
        elif choice_2 == 'positions':
            choicess = ['name', 'salary']
        elif choice_2 == 'status':
            choicess = ['hired_at', 'fired_at']
        elif choice_2 == 'contacts':
            choicess = ['address', 'phone_num', 'email']
        msg = 'Chose condition'
        title = 'Condition for better chosing row to delete'
        choice = g.choicebox(msg, title, choicess)
        res_query = f'DELETE FROM {choice_2} WHERE {choice}=?'
    return res_query, query_type


def request():
    choice = chosing_the_table()
    query, query_type = chosing_query_type(choice)
    msg = 'Enter your information'
    title = 'Puting information into DataBase'
    if query_type == 4:
        fieldNames = ['id', 'first name', 'last name', 'sex', 'date of birth']
    if query_type == 5:
        fieldNames = ['id', 'name', 'salary', 'employees id']
    if query_type == 6:
        fieldNames = ['id', 'hired_at', 'fired_at', 'employees id']
    if query_type == 7:
        fieldNames = ['id', 'address', 'phone_num', 'email', 'employees id']
    fieldValues = g.multenterbox(msg,title, fieldNames)
    import_data.imp_data(query, fieldValues)
    logger.log(fieldValues, 'INSERT')


def answer():
    choice = chosing_the_table()
    query, query_type = chosing_query_type(choice) 
    if query_type == 1:
        export_data.exp_data_all(query)
        logger.log(query, 'SELECT')
    elif query_type == 2:
        msg = 'Enter last name of employee'
        title = 'Choosing a person you interested in'
        inf = g.enterbox(msg, title)
        export_data.exp_data(query, inf)
        logger.log(inf, 'SELECT')
    elif query_type == 3:
        msg = "Enter name of employee's position"
        title = 'Choosing a person you interested in'
        choices = ['Manager', 'Driver', 'Programmer', 'SysAdmin', 
                    'Desiner', 'Accountant', 'Lawyer', 'Cleaner']
        inf = g.choicebox(msg, title, choices)
        export_data.exp_data(query, inf)
        logger.log(inf, 'SELECT')


def change():
    choice = chosing_the_table()
    query, *_ = chosing_query_type(choice)
    msg_2 = 'Enter new value'
    title_2 = 'New value'
    choice_2 = g.enterbox(msg_2, title_2)
    msg_4 = 'Enter value of condition'
    title_4 = 'Value of condition'
    choice_4 = g.enterbox(msg_4, title_4)
    data = (choice_2, choice_4)
    update_data.update_db(query, data)
    logger.log((query, data), 'UPDATE')



def remove():
    choice = chosing_the_table()
    query, *_ = chosing_query_type(choice)
    msg = 'Enter value of condition'
    title = 'Value of condition'
    choice_2 = g.enterbox(msg, title)
    delete_data.del_db(query, (choice_2, ))
    logger.log((query, (choice_2, )), 'DELETE')


# try:
#     request()
# except:
#     g.exceptionbox()
# try:
#     answer()
# except:
#     g.exceptionbox()
# try:
#     change()
# except:
#     g.exceptionbox()
# try:
#     remove()
# except:
#     g.exceptionbox()