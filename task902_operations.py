import telebot
from task902_constants import APY_KEY
from task902_view import keyboard
import task902_logger as log
# Операции с телеграмботом

value = ''
old_value = ''


def bot_starting():
    bot = telebot.TeleBot(APY_KEY)


    @bot.message_handler(commands=['calculator'])
    def get_message(message):
        global value
        if value == '':
            bot.send_message(message.from_user.id, '0', reply_markup=keyboard)
        else:
            bot.send_message(message.from_user.id, value, reply_markup=keyboard)
        log.log_menu(message)


    @bot.message_handler(commands=['stop'])
    def get_stop(message):
        bot.send_message(message.from_user.id, 'Ok!')
        log.log_menu(message)
        bot.stop_polling()


    @bot.message_handler(commands=['log'])
    def get_log(message):
        bot.send_message(message.from_user.id, log.read_log())
        log.log_menu(message)


    @bot.callback_query_handler(func=lambda call: True)
    def callback(query):
        global value, old_value
        data = query.data

        if data == 'no':
            ...
        elif data == 'C':
            value = ''
        elif data == '<=':
            if value != '':
                value = value[:len(value) - 1]
        elif data == '=':
            try:
                value = str(eval(value))
            except:
                value = 'Ошибка.'
            log.log_operations(query, value)
        else:
            value += data

        if (value != old_value and value != '') or ('0' != old_value and value == ''):
            if value == '':
                bot.edit_message_text(chat_id=query.message.chat.id,
                                    message_id=query.message.message_id, text='0',
                                    reply_markup=keyboard)
            else:
                bot.edit_message_text(chat_id=query.message.chat.id,
                                    message_id=query.message.message_id, text=value,
                                    reply_markup=keyboard)
            # print(f'{str(query.message.chat.first_name)} {str(query.message.chat.last_name)}\
            #         (id: {query.message.from_user.id})')
            old_value = value
            if value == 'Ошибка.':
                value = ''


    bot.polling()


    
    




