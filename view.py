import import_data, export_data, logger
from constants import API_KEY
import telebot


def bot_starting():
    bot = telebot.TeleBot(API_KEY)


    def get_import_mode(data, mode=1):
        if mode == 1:
            import_data.get_txt(data)
        elif mode == 2:
            import_data.get_csv(data)
        elif mode ==3:
            import_data.get_json(data)


    def get_export_mode(data, mode=1):
        if mode == 1:
            return export_data.from_txt(data)
        elif mode == 2:
            return export_data.from_csv(data)
        elif mode == 3:
            return export_data.from_json(data)


    def mode_int_to_str(mode: int):
        mode_inf = ''
        if mode == 1:
            mode_inf += 'txt'
        elif mode == 2:
            mode_inf += 'csv'
        elif mode == 3:
            mode_inf += 'json'
        return mode_inf


    @bot.message_handler(commands=['start'])
    def get_mode(message):
        send_mes = bot.send_message(message.from_user.id, 'Enter EX for export and IM for import phone numbers: ')
        bot.register_next_step_handler(send_mes, user_mode)
        logger.log_menu(message)


    def user_mode(message):
        mode = message.text
        logger.log_mode(message)
        if 'im'.casefold() in mode:
            get_data(message)
        elif 'ex'.casefold() in mode:
            input_data(message)
        else:
            bot.send_message(message.from_user.id, 'Just EX or IM is correct.')
            get_mode(message)
        

    # Functions for export data from phoneBook
    def input_data(message):
        send_mes = bot.send_message(message.from_user.id, 'Enter 1 for txt, 2 for csv, 3 for json: ')
        bot.register_next_step_handler(send_mes, mode_hold)


    def mode_hold(message):
        mode = message.text
        send_mes = bot.send_message(message.from_user.id, 'Enter Second name: ')
        bot.register_next_step_handler(send_mes,answer, mode)


    def answer(message, mode):
        data = message.text
        mode = int(mode)
        bot.send_message(message.from_user.id, get_export_mode(data, mode))
        logger.log_user_requests(mode_int_to_str(mode), message)
        return data


    # Functions for import data into phoneBook
    def get_data(message):
        send_mes = bot.send_message(message.from_user.id, 'Enter 1 for txt, 2 for csv, 3 for json: ')
        bot.register_next_step_handler(send_mes, mode_holder)


    def mode_holder(message):
        mode = message.text
        send_mes = bot.send_message(message.from_user.id, 'Enter First_name, Second_name, Phone_number and your comments with space: ')
        bot.register_next_step_handler(send_mes,get_request, mode)


    def get_request(message, mode):
        data = message.text
        mode = int(mode)
        if ' ' not in data:
            bot.send_message(message.from_user.id, 'You have to put space between values.')
            get_data(message)
        get_import_mode(data, mode)
        logger.log_user_requests(mode_int_to_str(mode), message)


    @bot.message_handler(commands=['log'])
    def get_log(message):
        bot.send_message(message.from_user.id, logger.read_log())
        logger.log_menu(message)


    # @bot.message_handler(commands=['stop'])
    # def get_stop(message_3):
    #     bot.send_message(message_3.from_user.id, 'Ok!')
    #     #log.log_menu(message)
    #     bot.stop_polling()


    bot.polling()