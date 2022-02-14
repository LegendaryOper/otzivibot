#761983343

import telebot
import pymysql
from config import *
from time import sleep
import re

token = '5181846470:AAEQZCDqenxYj29lH25KXBxuwKoKCpASVwc'
ADMINS = []
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
primer_platforms = ['Яндекс карты - 1', 'Google карты - 2', 'Restoclub - 3', 'Zoon - 4', 'Фламп - 5', 'Отзовик - 6',
                    '2ГИС - 7', 'Allcafe - 8']
primer = '/add\nОтзыв о Мгу\n1\n50р\nЖенский\nhttps://yandex.by/maps/org/mgu/15803908161/?ll=37.552516%2C55.685061&z=17.96'\
'\n Тебе нужно оставить три отзыва об этом здании. Отзывы придумывай сам, главное чтобы было реалистично. Как сделаешь'\
' присылай скрин'

platforms_ids = {'1': 'Яндекс карты', '2': 'Google карты', '3': 'Restoclub','4': 'Zoon','5': 'Фламп', '6': 'Отзовик',
                 '7': '2ГИС', '8': 'Allcafe'}
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

# Клавы админа
admin_keyboard = telebot.types.ReplyKeyboardMarkup(True)
admin_messages = ['Добавить новое задание', 'Доступные задания']
admin_keyboard.row(admin_messages[0], admin_messages[1])

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


def select_user_info(user_id):
    cursor1 = connection.cursor()
    cursor1.execute('select * from users where user_id=%s', (user_id,))
    data = cursor1.fetchall()[0]
    print(data)
    result = 'Твой пол: '+data['sex'] + '\nВсего выполнено заданий: '+str(data['full_count'])\
             + '\nВыполнено заданий за сегодня: ' + str(data['today_tasks'])
    connection.commit()
    cursor1.close()
    return result


def add_user_category_now(category_id, user_id):
    cursor = connection.cursor()
    cursor.execute('update users set category_id=%s where user_id=%s', (category_id, user_id))
    connection.commit()
    cursor.close()



# функции админа
# добавление записей
def add_task(arr1):
    print(arr1)
    arr1=[i.strip() for i in arr1]
    print(arr1)
    cursor = connection.cursor()
    cursor.execute('insert into tasks(name,category_id,cost,sex,url,descript,vision) '\
                   'values (%s,%s,%s,%s,%s,%s,true)', (arr1[1], arr1[2], arr1[3], arr1[4], arr1[5], arr1[6]))
    connection.commit()
    cursor.close()


def select_last_task():
    cursor = connection.cursor()
    cursor.execute('select * from tasks order by id DESC limit 1')
    data=cursor.fetchall()[0]
    print(data['name'])
    cursor.execute('update categories set tasks_id = concat(tasks_id,%s,";") where id = %s', (str(data['id']),str(data['category_id'])))
    zadaniye ='Краткое описание: '+data['name']+'\nПлатформа: '+platforms_ids[str(data['category_id'])]+'\nId задания: '+str(data['id'])+\
              '\nПол: '+data['sex']+'\nОплата: '+data['cost']+'\n'+'\nСсылка: '+data['url']+'\nПолное описание: '+data['descript']
    cursor.close()
    print(zadaniye)
    return zadaniye


def select_all_tasks():
    cursor = connection.cursor()
    cursor.execute('select name, sex, category_id, id from tasks')
    data = cursor.fetchall()
    cursor.close()
    return data

def select_task(task_id):
    cursor = connection.cursor()
    cursor.execute('select * from tasks where id=%s', (task_id,))
    data = cursor.fetchall()[0]
    print(data['name'])
    cursor.execute('update categories set tasks_id = concat(tasks_id,%s,";") where id = %s',
                   (str(data['id']), str(data['category_id'])))
    zadaniye = 'Краткое описание: ' + data['name'] + '\nПлатформа: ' + platforms_ids[
        str(data['category_id'])] + '\nId задания: ' + str(data['id']) + \
               '\nПол: ' + data['sex'] + '\nОплата: ' + data['cost'] + '\n' + '\nСсылка: ' + data[
                   'url'] + '\nПолное описание: ' + data['descript']
    cursor.close()
    print(zadaniye)
    return zadaniye






@bot.callback_query_handler(func=lambda callback_query: True)
def query_callback(callback_query):
    pattern = r'\d+'
    match = re.search(pattern, str(callback_query.data))
    task_id = match.group()
    cursor = connection.cursor()
    if str(callback_query.data).startswith('admin'):
        inline_button = telebot.types.InlineKeyboardButton('Удалить задание', callback_data=f'del {task_id}')
        inline_keyboard = telebot.types.InlineKeyboardMarkup().add(inline_button)
        bot.send_message(callback_query.message.chat.id, select_task(task_id), reply_markup=inline_keyboard)
    elif str(callback_query.data).startswith('del'):
        cursor.execute('delete from tasks where id=%s', (task_id,))
        connection.commit()
        bot.send_message(callback_query.message.chat.id, 'Задание удалено', reply_markup=admin_keyboard)
    cursor.close()









@bot.message_handler(content_types=['text'])
def message_text_handler(message):
    print(message.text)
    user_id = message.from_user.id
    # admin
    if user_id in ADMINS:
        if message.text == '/start':
            db_table_val(message.from_user.id)
            bot.send_message(message.from_user.id, 'Здорова Хозяин', reply_markup=admin_keyboard)
        if message.text == admin_messages[0]:
            bot.send_message(message.from_user.id, 'Напиши команду /add, перейди на новую строку и построчно впиши '
                                                   'мне краткое описание задания(не более 40 символов), номер платформы,'
                                                   'цену задания, пол, ссылку, полное описание задания')
            bot.send_message(message.from_user.id, 'Доступные платформы:\n'+'\n'.join(primer_platforms))
            bot.send_message(message.from_user.id, 'Пример:\n'+primer)
        if message.text.startswith('/add'):
            taskarr = message.text.split('\n')
            try:
                add_task(taskarr)
                bot.send_message(message.from_user.id, 'Окей, я добавил твое задание, можешь на него посмотреть', reply_markup=admin_keyboard)
                bot.send_message(message.from_user.id, select_last_task())
            except Exception as ex:
                bot.send_message(message.from_user.id, 'Упс..что то пошло не так, попробуй еще раз',reply_markup=admin_keyboard)
                print(ex)
        if message.text == admin_messages[1]:
            try:
                for task in select_all_tasks():
                    sleep(0.1)
                    inline_button = telebot.types.InlineKeyboardButton('Подробнее', callback_data=f'admin {task["id"]}')
                    inline_keyboard = telebot.types.InlineKeyboardMarkup().add(inline_button)
                    task_message = 'Платформа: ' + platforms_ids[str(task['category_id'])] + '\nЗаголовок: '\
                                   + task['name'] + '\nПол: ' + task['sex']
                    bot.send_message(user_id, task_message, reply_markup=inline_keyboard)
            except Exception as ex:
                bot.send_message(message.from_user.id, 'Упс..что то пошло не так, попробуй еще раз',reply_markup=admin_keyboard)
                print(ex)

    else:

        if message.text == '/start':
            db_table_val(message.from_user.id)
            bot.send_message(message.from_user.id, start_message, reply_markup=start_keyboard)
        elif message.text == account_message:
            bot.send_message(message.from_user.id,'Вот информация о твоем аккаунте', reply_markup=account_keyboard)
            select_user_info(user_id)
            bot.send_message(message.from_user.id, select_user_info(user_id), reply_markup=account_keyboard)
        elif message.text == account_messages[0]:
            bot.send_message(message.from_user.id, 'Возвращаю...', reply_markup=start_keyboard)
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
            add_user_category_now(for_message_platforms.index(message.text)+1, user_id)
            bot.send_message(message.from_user.id, 'Понял, какого ты пола?', reply_markup=sex_keyboard)
        elif message.text in sex_messages:
            if message.text == sex_messages[0]:
                add_sex_to_user('Мужской',user_id)
            else:
                add_sex_to_user('Женский',user_id)
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
