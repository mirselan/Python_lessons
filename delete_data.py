import db_module


def del_db(query, data):
    db_module.delete_db(query, data)