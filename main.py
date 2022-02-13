import telebot
import pymysql
from config import *

token = '5181846470:AAEQZCDqenxYj29lH25KXBxuwKoKCpASVwc'
ADMINS = [761983343]
bot = telebot.TeleBot(token)

start_message = 'Привет, я бот для заработка на выполнении простых заданий. Если хочешь заработать, нажимай на кнопку ниже'

# стартовая клава
start_keyboard = telebot.types.ReplyKeyboardMarkup(True)
zarab_message = 'Зарабатывать🔥🔥🔥'
account_message = 'Мой аккаунт'
start_keyboard.row(zarab_message, account_message)

# клава на владение акком одной из платформ
email_acсess_keyboard = telebot.types.ReplyKeyboardMarkup(True)
email_yes_message = 'Да😀'
email_no_message = 'Нет😩'
email_acсess_keyboard.row(email_yes_message, email_no_message)

# платформы, используемые в сообщении
for_message_platforms = ['Яндекс карты', 'Google карты', 'Restoclub', 'Zoon', 'Фламп', 'Отзовик', '2ГИС', 'Allcafe']

# клава по платформам
platforms_keyboard = telebot.types.ReplyKeyboardMarkup(True)
for platform in for_message_platforms:
    platforms_keyboard.row(platform)







try:
    connection = pymysql.connect(host=host,
                                 port=3306,
                                 user=user,
                                 password=password,
                                 database=db_name,
                                 cursorclass=pymysql.cursors.DictCursor
                                 )


    db_setting1 = 'SET SQL_SAFE_UPDATES = 0'


    connection.cursor().execute(db_setting1)

    connection.cursor().close()
    print('succesful')


except Exception as ex:
    print("Error")
    print(ex)







# клава для определения пола юзера
sex_keyboard = telebot.types.ReplyKeyboardMarkup(True)
sex_messages = ['Мужской👱🏼‍♂', 'Женский👩🏽‍🦰']
sex_keyboard.row(sex_messages[0], sex_messages[1])

# клава аккаунта
account_keyboard = telebot.types.ReplyKeyboardMarkup(True)
account_messages = ['Вернуться к заданиям']
account_keyboard.row(account_messages[0])

# клава выбора задания
select_keyboard = telebot.types.ReplyKeyboardMarkup(True)
select_messages = ['Вернуться к платформам', 'Выбрать задание']
select_keyboard.row(select_messages[0], select_messages[1])


# функции
def check_userid_in_database(id):
    cursor = connection.cursor()
    cursor.execute("SELECT user_id FROM users WHERE user_id=%s", (id,))
    data = cursor.fetchall()
    if len(data) == 0:
        cursor.close()
        return True
    else:
        cursor.close()
        return False


def db_table_val(user_id: int):
    cursor1 = connection.cursor()
    if check_userid_in_database(user_id):
        cursor1.execute('INSERT INTO users (user_id,full_count,now_task_id,today_tasks) VALUES (%s,0,0,0)', (user_id,))
        connection.commit()
    cursor1.close()

def add_sex_to_user(sex,user_id):
    cursor1 = connection.cursor()
    cursor1.execute('update users set sex =%s where user_id=%s', (sex, user_id))
    connection.commit()
    cursor1.close()




@bot.message_handler(content_types=['text'])
def message_text_handler(message):
    print(message.text)
    user_id = message.from_user.id
    if message.text == '/start':
        db_table_val(message.from_user.id)
        bot.send_message(message.from_user.id, start_message, reply_markup=start_keyboard)
    elif message.text == account_message:
        bot.send_message(message.from_user.id,'Вот информация о твоем аккаунте', reply_markup=account_keyboard)
        # sql запрос спиздить фулл инфу об аккаунте
        pass
    elif message.text == account_messages[0]:
        # вернуть обратно
        pass

    elif message.text == zarab_message:
        bot.send_message(message.from_user.id, 'Окей, у тебя есть аккаунт на одной из этих платформ?', reply_markup=email_acсess_keyboard)
        bot.send_message(message.from_user.id, ', '.join(for_message_platforms),reply_markup=email_acсess_keyboard)
    elif message.text in (email_yes_message,select_messages[0]):
        bot.send_message(message.from_user.id, 'Окей, на какой платформе хочешь выполнять задания?', reply_markup=platforms_keyboard)
    elif message.text == email_no_message:
        bot.send_message(message.from_user.id, 'Для работы с нами тебе нужно иметь аккаунт хотя '
                                               'бы на одной из этих платформ:')
        bot.send_message(message.from_user.id, ', '.join(for_message_platforms))
        bot.send_message(message.from_user.id, 'Приходи, как зарегистрируешься', reply_markup=email_acсess_keyboard)
    elif message.text in for_message_platforms:
        #sql запрос
        bot.send_message(message.from_user.id, 'Понял, какого ты пола?', reply_markup=sex_keyboard)
    elif message.text in sex_messages:
        if message.text == sex_messages[0]:
            add_sex_to_user('male',user_id)
        else:
            add_sex_to_user('female',user_id)
            pass
        bot.send_message(message.from_user.id, 'Держи доступные задания на этой платформе:', reply_markup=select_keyboard)
        # sql запрос чтобы спиздить описание заданий по категории
    elif message.text == select_messages[1]:
        bot.send_message(message.from_user.id, 'Напиши мне id задания за которое хочешь взяться')


    # if message.text == (pk задания)
    #   if pk задания not in banned_categories для юзера
    #             выслать задание
    #             sql запрос задание выполняется

    else:bot.send_message(message.from_user.id, 'Я тебя не понимаю', reply_markup=start_keyboard)












bot.polling(none_stop=True, interval=0)
