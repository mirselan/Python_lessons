import db_module
import easygui as g


def exp_data(query, data):
    #msg = 'Employee that you have chosen'
    title = 'Getting answer'
    msg = db_module.read_db(query, data)
    g.msgbox(msg, title)


def exp_data_all(query):
    #msg = 'Employee that you have chosen'
    title = 'Getting answer'
    msg = db_module.read_db_all(query)
    g.msgbox(msg, title)