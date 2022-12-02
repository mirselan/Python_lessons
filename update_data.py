import db_module


def update_db(query, data):
    db_module.change_db(query, data)