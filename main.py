#761983343
from threading import Thread

import telebot
import pymysql
from config import *
from time import sleep,time
import re



def connect_to_db():
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
    return connection
connection = connect_to_db()
token = '5181846470:AAEQZCDqenxYj29lH25KXBxuwKoKCpASVwc'
ADMINS = [619616592,761983343]
bot = telebot.TeleBot(token)

start_message = 'Привет, я бот для заработка на выполнении простых заданий. Если хочешь заработать, нажимай на кнопку ниже'
attention_message = 'Внимание! Перед началом работы со мной установи себе какой нибудь username(настройки -> имя пользователя)' \
                    ', если он еще у тебя не установлен. В противном случае админ не сможет с тобой связаться для оплаты.'

vazhno = 'ВАЖНО: Перед публикацией отзыва на Яндекс или Google ПОЖАЛУЙСТА, Авито (На остальные не распространяется),' \
          ' проверьте что Ваш аккаунт зарегистрирован не менее 2х месяцев назад, если Вы возьмете задание с нового' \
          ' аккаунта, Вам будет заблокирован доступ к боту навсегда ( не тратьте своё и ваше время) отзывы с таких' \
          ' аккаунтов не публикуются.Перед публикацией проверьте текст, правильно ли он скопирован, туда ли Вы отправили,' \
          ' после того как опубликовали, обновите страницу, сделайте скриншот где будет видно Ваш отзыв, ' \
          'что он на проверке и организацию на которую оставите отзыв. Если вы скинете в ответ на задание более ' \
          '1-й фотографии или фотографии которая не относится к заданию - блокировка на всегда.'

pravila = 'Правила пользование ботом:\n'\
'1. С каждой карточки не более 1 отзыва в день (исключение Яндекс  - 1.5 дня)\n'\
'2. В ответ на задание присылать не более 1-й фотографии (в случае нарушение - блокировка аккаунта на всегда)\n'\
'3. На каждое задание которое Вы берете, выделяется 20 минут, в том случае если Вы не успеете сделать задание, ' \
'доступ к подкатегорий Вам так же будет заблокирован навсегда (Это для того, что бы люди которые намерены будут помешать работе бота),' \
' поэтому ПОЖАЛУЙСТА проверяйте активность аккаунтов к работе, до того как зашли в бота.\n'\
'4. Выплаты: Выплаты осуществляются каждую пятницу, по итогам Вашей недели и ее активности в боте я вижу, ' \
'кто и сколько сделал отзывов, сколько опубликовалось и сколько не опубликовалось, поэтому пожалуйста не ' \
'пытайтесь меня обмануть)\n'\
'5. Цены: будут существовать две категории цен(на данный момент) 50 и 25 рублей, ' \
'в основном будут отзывы по 50 рублей за ШТ, будут более простые отзывы, за них я буду платить по 25р шт'


referal = 'Реферальные программы и поощрения:\n' \
          'В скором времени бот будет собирать всю информацию о Вашей активности, сколько Вы пригласили друзей, какая у них ' \
          'активность и тд. У таких пользователей будет возможность быть в канале приоритете, там будут задания, ' \
          'за которые я буду платить от 100р и сразу выплачивать(по Вашему желанию),' \
          ' другие более высокооплачиваемые задания.'

# стартовая клава
start_keyboard = telebot.types.ReplyKeyboardMarkup(True)
zarab_message = 'Зарабатывать🔥🔥🔥'
account_message = 'Мой аккаунт'
pravila_message = 'Правила'
start_keyboard.row(zarab_message, account_message)
start_keyboard.row(pravila_message)

# клава на владение акком одной из платформ
email_acсess_keyboard = telebot.types.ReplyKeyboardMarkup(True)
email_yes_message = 'Да😀'
email_no_message = 'Нет😩'
email_acсess_keyboard.row(email_yes_message, email_no_message)

# платформы, используемые в сообщении
for_message_platforms = ['Яндекс карты', 'Google карты', 'Restoclub', 'Zoon', 'Фламп', 'Отзовик', '2ГИС', 'Allcafe',
                         'Авито']
primer_platforms = ['Яндекс карты - 1', 'Google карты - 2', 'Restoclub - 3', 'Zoon - 4', 'Фламп - 5', 'Отзовик - 6',
                    '2ГИС - 7', 'Allcafe - 8', 'Авито - 9']

primer = '/add\nОтзыв о Мгу\n1\n50р\n1\nhttps://yandex.by/maps/org/mgu/15803908161/?ll=37.552516%2C55.685061&z=17.96'\
'\n Тебе нужно оставить три отзыва об этом здании. Отзывы придумывай сам, главное чтобы было реалистично. Как сделаешь'\
' присылай скрин'

platforms_ids = {'1': 'Яндекс карты', '2': 'Google карты', '3': 'Restoclub','4': 'Zoon','5': 'Фламп', '6': 'Отзовик',
                 '7': '2ГИС', '8': 'Allcafe', '9': 'Авито'}
sex = ['1 - Мужской', '2 - Женский', '3 - Любой']
sex_array = ['Мужской', 'Женский', 'Любой']
# клава по платформам
platforms_keyboard = telebot.types.ReplyKeyboardMarkup(True)
for platform in for_message_platforms:
    platforms_keyboard.row(platform)









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
select_messages = ['Вернуться к платформам', 'Вернуться в начало']
select_keyboard.row(select_messages[0], select_messages[1])

# Клавы админа
admin_keyboard = telebot.types.ReplyKeyboardMarkup(True)
admin_messages = ['Добавить новое задание', 'Доступные задания', 'Массовая рассылка']
admin_keyboard.row(admin_messages[0], admin_messages[1], admin_messages[2])

tasks_keyboard = telebot.types.ReplyKeyboardMarkup(True)
tasks_messages = ['Выполненные задания', 'Невыполненные задания']
tasks_keyboard.row(tasks_messages[0], tasks_messages[1])

exit_keyboard = telebot.types.ReplyKeyboardMarkup(True)
exit_keyboard.row('Назад')

# функции
def check_userid_in_database(id):
    try:
        connection = connect_to_db()
        cursor = connection.cursor()
        cursor.execute("SELECT user_id FROM users WHERE user_id=%s", (id,))
        data = cursor.fetchall()
        cursor.close()
        connection.close()
        if len(data) == 0:
            return True
        else:
            return False
    except Exception as ex:
        print("Ошибка в checkuserid")
        print(ex)
        cursor.close()



def check_pravila(user_id):
    try:
        connection = connect_to_db()
        cursor = connection.cursor()
        cursor.execute('select pravila from users where user_id=%s', (user_id,))
        data = cursor.fetchall()[0]['pravila']
        cursor.close()
        connection.close()
        if data == 0:
            return False
        elif data is None:
            print('checkpravila none')
            bot.send_message(user_id, 'Какая то ошибка, попробуй еще раз', reply_markup=start_keyboard)
        else:
            return True
    except Exception as ex3:
        print(ex3)
        print('error in checkpravila')


def add_user_pravila(user_id):
    try:
        connection = connect_to_db()
        cursor = connection.cursor()
        cursor.execute('update users set pravila = 1 where user_id=%s', (user_id,))
        connection.commit()
        cursor.close()
        connection.close()
    except Exception as ex3:
        print(ex3)
        print('error in adduserpravila')
        cursor.close()



def db_table_val(user_id: int):
    try:
        connection = connect_to_db()
        cursor1 = connection.cursor()
        if check_userid_in_database(user_id):
            cursor1.execute('INSERT INTO users (user_id,full_count,now_task_id,today_tasks,today_categories_ids, pravila) VALUES (%s,0,0,0,";",0)', (user_id,))
            connection.commit()
        cursor1.close()
        connection.close()
    except Exception as ex:
        print('Error in dbtableval')
        print(ex)



def add_sex_to_user(sex,user_id):
    try:
        connection = connect_to_db()
        cursor1 = connection.cursor()
        cursor1.execute('update users set sex =%s where user_id=%s', (sex, user_id))
        connection.commit()
        cursor1.close()
        connection.close()
    except Exception as ex:
        print('error in add sex to user')
        print(ex)



def select_user_info(user_id):
    try:
        connection = connect_to_db()
        cursor1 = connection.cursor()
        cursor1.execute('select * from users where user_id=%s', (user_id,))
        data = cursor1.fetchall()[0]
        try:
            result = 'Твой пол: '+sex_array[data['sex']-1] + '\nВсего выполнено заданий: '+str(data['full_count'])\
                 + '\nВыполнено заданий за сегодня: ' + str(data['today_tasks'])
            connection.commit()
            cursor1.close()
        except Exception:
            cursor1.close()
            return 'У нас пока нет информации о твоем аккаунте, ты только запустил бота)'
        connection.close()
        return result
    except Exception as ex:
        print('error in select user info')
        print(ex)



def add_user_category_now(category_id, user_id):
    try:
        connection = connect_to_db()
        cursor = connection.cursor()
        cursor.execute('update users set category_id=%s where user_id=%s', (category_id, user_id))
        connection.commit()
        cursor.close()
        connection.close()
    except Exception as ex:
        print('error in addusercategorynow')
        print(ex)


def select_tasks_ids_for_user(user_id):
    try:
        connection = connect_to_db()
        cursor1 = connection.cursor()
        cursor1.execute('select * from users where user_id=%s', (user_id,))
        data = cursor1.fetchall()[0]
        pattern = r'\d+'
        match = re.findall(pattern, str(data['today_categories_ids']))
        print('match', match)
        print(str(data['category_id']))
        if data['now_task_id'] > 0:
            cursor1.close()
            connection.close()
            return False
        elif data['today_tasks'] >= 3:
            cursor1.close()
            connection.close()
            return 'too_many'
        elif str(data['category_id']) in match:
            cursor1.close()
            connection.close()
            return 'banned'
        cursor1.execute('select id, category_id from tasks where vision = 1 and sex in (%s,3) and category_id=%s',
                        (data['sex'], (data['category_id'])))
        tasks = cursor1.fetchall()
        cursor1.close()
        connection.close()
        return [task['id'] for task in tasks]
    except Exception as ex:
        print(ex)
        print('error in selecttasksidsforuser')


def select_sorted_tasks(tasks_ids):
    try:
        connection = connect_to_db()
        cursor = connection.cursor()
        dataarr=[]
        for ids in tasks_ids:
            cursor.execute('select  name, sex, category_id, id from tasks where id=%s', (ids,))
            data = cursor.fetchall()[0]
            dataarr.append(data)
        cursor.close()
        connection.close()
        return dataarr
    except Exception as ex:
        print('error in selectsortedtasks')
        print(ex)


def select_user_now_task(user_id):
    try:
        connection = connect_to_db()
        cursor = connection.cursor()
        try:
            cursor.execute('select * from tasks where id in (select now_task_id from users where user_id=%s)', (user_id,))
            data = cursor.fetchall()[0]
        except Exception:
            cursor.execute('update users set now_task_id = 0 where user_id=%s', (user_id,))
            connection.commit()
            return 'Задание не найдено'
        cursor.execute('update tasks set vision = 0 where id=%s', (data['id'],))
        connection.commit()
        cursor.close()
        connection.close()
        zadaniye = 'Краткое описание: ' + data['name'] + '\nПлатформа: ' + platforms_ids[
            str(data['category_id'])] + '\nId задания: ' + str(data['id']) +\
                   '\nПол: ' + sex_array[data['sex'] - 1] + '\nОплата: ' + data['cost'] + '\n' + '\nСсылка: ' + data[
                       'url'] + '\nПолное описание: ' + data['descript']
        return zadaniye
    except Exception as ex:
        print(ex)
        print('error in selectusernowtask')


def select_user_now_task_id(user_id):
    try:
        connection = connect_to_db()
        cursor = connection.cursor()
        cursor.execute('select now_task_id from users where user_id=%s', (user_id,))
        task_id = cursor.fetchall()[0]['now_task_id']
        cursor.close()
        connection.close()
        return task_id
    except Exception as ex:
        print(ex)
        print('error in selectusernowtaskid')




def send_sorted_tasks(user_id,select):
    try:
        connection = connect_to_db()
        for task in select_sorted_tasks(select):
            sleep(0.1)
            inline_button = telebot.types.InlineKeyboardButton('Взяться за задание',
                                                               callback_data=f'user {task["id"]}')
            inline_keyboard = telebot.types.InlineKeyboardMarkup().add(inline_button)
            task_message = 'Платформа: ' + platforms_ids[str(task['category_id'])] + '\nЗаголовок: ' \
                           + task['name'] + '\nПол: ' + sex_array[task['sex'] - 1]
            bot.send_message(user_id, task_message, reply_markup=inline_keyboard)
        connection.close()
    except Exception as ex:
        bot.send_message(user_id, 'Упс..что то пошло не так, сообщи админу',
                         reply_markup=start_keyboard)
        print('error in sendsortedtasks')
        print(ex)





# функции админа
# добавление записей
def add_task(arr1):
    try:
        connection = connect_to_db()
        arr1 = [i.strip() for i in arr1]
        cursor = connection.cursor()
        cursor.execute('insert into tasks(name,category_id,cost,sex,url,descript,vision) '\
                       'values (%s,%s,%s,%s,%s,%s,true)', (arr1[1], arr1[2], arr1[3], arr1[4], arr1[5], arr1[6]))
        connection.commit()
        cursor.close()
        connection.close()
    except Exception as ex:
        print('error in addtask')
        print('ex')


def select_last_task():
    try:
        connection = connect_to_db()
        cursor = connection.cursor()
        cursor.execute('select * from tasks order by id DESC limit 1')
        data=cursor.fetchall()[0]
        cursor.execute('update categories set tasks_id = concat(tasks_id,%s,";") where id = %s', (str(data['id']),str(data['category_id'])))
        connection.commit()
        zadaniye ='Краткое описание: '+data['name']+'\nПлатформа: '+platforms_ids[str(data['category_id'])]+'\nId задания: '+str(data['id'])+\
                  '\nПол: '+sex_array[data['sex']-1]+'\nОплата: '+data['cost']+'\n'+'\nСсылка: '+data['url']+'\nПолное описание: '+data['descript']
        cursor.close()
        connection.close()
        return zadaniye
    except Exception as ex:
        print('error in selectlasttask')
        print(ex)



def select_all_tasks(flag):
    try:
        connection = connect_to_db()
        cursor = connection.cursor()
        if flag == 1:
            cursor.execute('select name, sex, category_id, id from tasks where vision = 1')
        else:
            cursor.execute('select name, sex, category_id, id from tasks where vision = 0')
        data = cursor.fetchall()
        cursor.close()
        connection.close()
        return data
    except Exception as ex:
        print(ex)
        print('error in selectalltasks')


def select_task(task_id):
    try:
        connection = connect_to_db()
        cursor = connection.cursor()
        cursor.execute('select * from tasks where id=%s', (task_id,))
        data = cursor.fetchall()[0]
        zadaniye = 'Краткое описание: ' + data['name'] + '\nПлатформа: ' + platforms_ids[
            str(data['category_id'])] + '\nId задания: ' + str(data['id']) + \
                   '\nПол: ' + sex_array[data['sex']-1] + '\nОплата: ' + data['cost'] + '\n' + '\nСсылка: ' + data[
                       'url'] + '\nПолное описание: ' + data['descript']
        connection.close()
        return zadaniye
    except Exception as ex:
        print(ex)
        print('error selecttask')



def update_after_task_upload(user_id):
    try:
        connection = connect_to_db()
        cursor = connection.cursor()
        cursor.execute('update users set now_task_id = 0,full_count = full_count+1,today_tasks=today_tasks+1'
                       ' where user_id = %s', (user_id,))
        connection.commit()
        cursor.close()
        connection.close()
    except Exception as ex:
        print(ex)
        print('error in updateaftertask...')



def send_mass_message(message_text):
    try:
        connection = connect_to_db()
        cursor = connection.cursor()
        cursor.execute('select user_id from users')
        data = cursor.fetchall()
        cursor.close()
        connection.close()
        for id_dict in data:
            user_id = id_dict['user_id']
            try:
                if user_id not in ADMINS:
                    bot.send_message(user_id, 'Рассылка от Админа!!!')
                    bot.send_message(user_id, message_text, reply_markup=start_keyboard)
                    sleep(0.1)
                else:
                    bot.send_message(user_id, 'Рассылка отправлена', reply_markup=admin_keyboard)
            except Exception:
                print('user with id', user_id,'has banned')
    except Exception as ex:
        print(ex)
        print('error in sendmass')



def update_description(description, task_id):
    try:
        connection = connect_to_db()
        cursor = connection.cursor()
        cursor.execute('update tasks set descript=%s where id=%s', (description, task_id))
        connection.commit()
        cursor.close()
        connection.close()
    except Exception as ex:
        print('error in update_descript')
        print(ex)




def send_full_task_admin(task_id,user_id):
    try:
        inline_button = telebot.types.InlineKeyboardButton('Удалить задание', callback_data=f'del {task_id}')
        inline_button1 = telebot.types.InlineKeyboardButton('Сделать видимым', callback_data=f'vis {task_id}')
        inline_button2 = telebot.types.InlineKeyboardButton('Сделать невидимым', callback_data=f'unvis {task_id}')
        inline_button3 = telebot.types.InlineKeyboardButton('Изменить описание', callback_data=f'edit {task_id}')
        inline_keyboard = telebot.types.InlineKeyboardMarkup().row(inline_button, inline_button1, inline_button2)
        inline_keyboard.row(inline_button3)
        bot.send_message(user_id, select_task(task_id), reply_markup=inline_keyboard)
    except Exception as ex2:
        print(ex2)
        print('error im sendfulltask')
        bot.send_message(user_id,'Какая то ошибка, не смог отправить тебе полное задание', reply_markup=admin_keyboard)

def deltask(task_id):
    try:
        connection = connect_to_db()
        cursor = connection.cursor()
        cursor.execute('delete from tasks where id=%s', (task_id,))
        connection.commit()
        cursor.close()
        connection.close()
    except Exception as exc:
        print('error in deltask')
        print(exc)



def vis(task_id):
    try:
        connection = connect_to_db()
        cursor = connection.cursor()
        cursor.execute('update tasks set vision = 1 where id=%s', (task_id,))
        connection.commit()
        cursor.close()
        connection.close()
    except Exception as ex:
        print('error in vis')
        print(ex)



def unvis(task_id):
    try:
        connection = connect_to_db()
        cursor = connection.cursor()
        cursor.execute('update tasks set vision=0 where id=%s', (task_id,))
        connection.commit()
        cursor.close()
        connection.close()
    except Exception as ex:
        print('error in unvis')
        print(ex)


def userquery(task_id,chat_id):
    try:
        connection = connect_to_db()
        cursor = connection.cursor()
        cursor.execute('select category_id from tasks where id=%s', (task_id,))
        category_id = cursor.fetchall()[0]['category_id']
        cursor.execute(
            'update users set now_task_id=(%s),today_categories_ids=concat(today_categories_ids,%s) where user_id = %s'
            , (task_id, str(category_id) + ';', chat_id))
        connection.commit()
        cursor.close()
        connection.close()
    except Exception as ex:
        print('err in user')
        print(ex)


def used(chat_id):
    try:
        connection = connect_to_db()
        cursor = connection.cursor()
        cursor.execute('select new_task_today from users where user_id=%s', (chat_id))
        new_task_today = cursor.fetchall()[0]['new_task_today']
        if new_task_today == 1:
            print('ты еблан')
            bot.send_message(chat_id, 'Ты уже отменял сегодня задание. Будь добр, выполни это.',
                             reply_markup=start_keyboard)
            cursor.close()
        else:
            cursor.execute('update users set now_task_id=0, new_task_today = 1, '
                           'today_categories_ids=substring(today_categories_ids,1,length(today_categories_ids)-2)'
                           'where user_id = %s', (chat_id,))

            connection.commit()
            bot.send_message(chat_id, 'Окей, посмотри другие задания',
                             reply_markup=start_keyboard)
            select = select_tasks_ids_for_user(chat_id)
            send_sorted_tasks(chat_id, select)
            cursor.close()
            connection.close()
    except Exception as ex:
        print('err in used')
        print(ex)





@bot.callback_query_handler(func=lambda callback_query: True)
def query_callback(callback_query):
    pattern = r'\d+'
    match = re.search(pattern, str(callback_query.data))
    task_id = match.group()
    cursor = connection.cursor()
    if str(callback_query.data).startswith('admin'):
        send_full_task_admin(task_id, user_id=callback_query.message.chat.id)
    elif str(callback_query.data).startswith('del'):
        deltask(task_id)
        bot.send_message(callback_query.message.chat.id, 'Задание удалено', reply_markup=admin_keyboard)
    elif str(callback_query.data).startswith('edit'):
        bot.send_message(callback_query.message.chat.id, 'Введи комманду /desc, айди задания и новое описание после него',
                         reply_markup=admin_keyboard)
        bot.send_message(callback_query.message.chat.id,
                         f'В данном случае /desc {task_id}', reply_markup=admin_keyboard)
    elif str(callback_query.data).startswith('vis'):
        vis(task_id)
        bot.send_message(callback_query.message.chat.id, f'Задание c айди {task_id} теперь видно всем', reply_markup=admin_keyboard)
    elif str(callback_query.data).startswith('unvis'):
        unvis(task_id)
        bot.send_message(callback_query.message.chat.id, f'Задание c айди {task_id} недоступно для всех',
                         reply_markup=admin_keyboard)
    elif str(callback_query.data).startswith('user'):
        inline_button = telebot.types.InlineKeyboardButton('Я уже выполнял это задание', callback_data=f'used {task_id}')
        inline_keyboard = telebot.types.InlineKeyboardMarkup().add(inline_button)
        bot.send_message(callback_query.message.chat.id, select_task(task_id), reply_markup=inline_keyboard)
        userquery(task_id, callback_query.message.chat.id)
        unvis(task_id)
        bot.send_message(callback_query.message.chat.id, 'Как сделаешь задание - обязательно пришли скрин выполнения',
                         reply_markup=start_keyboard)
    elif str(callback_query.data).startswith('used'):
        used(callback_query.message.chat.id)
    elif str(callback_query.data).startswith('allow'):
        bot.send_message(task_id,'Твое задание одобрили, в ближайшее время с тобой свяжется админ.',
                         reply_markup=start_keyboard)

    elif str(callback_query.data).startswith('abadon'):
        bot.send_message(task_id,
                         'Твое задание не одобрили.', reply_markup=start_keyboard)
        task_id = re.findall(pattern,str(callback_query.data))[1]
        vis(task_id)










@bot.message_handler(content_types=['text'])
def message_text_handler(message):

    user_id = message.from_user.id
    db_table_val(message.from_user.id)
    # admin
    if user_id in ADMINS:
        if message.text == '/start':
            db_table_val(message.from_user.id)
            bot.send_message(message.from_user.id, 'Здорова Хозяин', reply_markup=admin_keyboard)
        if message.text == admin_messages[0]:
            bot.send_message(message.from_user.id, 'Напиши команду /add, перейди на новую строку и построчно впиши '
                                                   'мне краткое описание задания(не более 40 символов), номер платформы,'
                                                   'цену задания, номер пола, ссылку, полное описание задания')
            bot.send_message(message.from_user.id, 'Доступные платформы:\n'+'\n'.join(primer_platforms))
            bot.send_message(message.from_user.id, 'Номера полов:\n' + '\n'.join(sex))

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
        if message.text.startswith('/desc'):
            try:
                pattern = r'\d+'
                match = re.search(pattern, str(message.text))
                task_id = match.group()
                description = message.text[message.text.find(task_id)+len(str(task_id))+1:]
                print(description)
                update_description(description, task_id)
                bot.send_message(user_id,'Успешно обновлено, теперь задание выглядит так:', reply_markup=admin_keyboard)
                send_full_task_admin(task_id, user_id)
            except Exception as ex1:
                print(ex1)
                bot.send_message(user_id,'Упс..ошибка, попробуй еще раз', reply_markup=admin_keyboard)

        if message.text == admin_messages[1]:
            bot.send_message(user_id, 'Выбери, какие задания хочешь видеть', reply_markup=tasks_keyboard)

        if message.text == 'Назад':
            bot.send_message(user_id, 'Возвращаю...', reply_markup=admin_keyboard)

        if message.text in tasks_messages:
            if message.text == tasks_messages[0]:
                tasks = select_all_tasks(0)
            else:
                tasks = select_all_tasks(1)
            try:
                for task in tasks:
                    sleep(0.1)
                    inline_button = telebot.types.InlineKeyboardButton('Подробнее', callback_data=f'admin {task["id"]}')
                    inline_keyboard = telebot.types.InlineKeyboardMarkup().add(inline_button)
                    task_message = 'Платформа: ' + platforms_ids[str(task['category_id'])] + '\nЗаголовок: '\
                                   + task['name'] + '\nПол: ' + sex_array[task['sex']-1]
                    bot.send_message(user_id, task_message, reply_markup=inline_keyboard)
                bot.send_message(user_id, 'Вот твои задания', reply_markup=exit_keyboard)
            except Exception as ex:
                bot.send_message(message.from_user.id, 'Упс..что то пошло не так, попробуй еще раз',reply_markup=admin_keyboard)
                print(ex)

        if message.text == admin_messages[2]:
            bot.send_message(message.from_user.id, 'Напиши боту комманду /send и сообщение после нее\n'
                                                   'Пример: /send Всем привет!')
        if message.text.startswith('/send'):
            send_mass_message(message.text[6:])


    else:

        if message.text == '/start':
            db_table_val(message.from_user.id)
            bot.send_message(message.from_user.id, start_message, reply_markup=start_keyboard)
            bot.send_message(message.from_user.id,attention_message , reply_markup=start_keyboard)
        elif message.text == pravila_message:
            bot.send_message(user_id, vazhno, reply_markup=start_keyboard)
            bot.send_message(user_id, pravila, reply_markup=start_keyboard)
            bot.send_message(user_id, referal, reply_markup=start_keyboard)
            add_user_pravila(user_id)

        elif message.text == account_message:
            bot.send_message(message.from_user.id,'Вот информация о твоем аккаунте', reply_markup=account_keyboard)
            bot.send_message(message.from_user.id, select_user_info(user_id), reply_markup=account_keyboard)
        elif message.text == account_messages[0]:
            bot.send_message(message.from_user.id, 'Возвращаю...', reply_markup=start_keyboard)

        elif message.text == zarab_message:
            if check_pravila(user_id):
                bot.send_message(message.from_user.id, 'Окей, у тебя есть аккаунт на одной из этих платформ?', reply_markup=email_acсess_keyboard)
                bot.send_message(message.from_user.id, ', '.join(for_message_platforms),reply_markup=email_acсess_keyboard)
            else:
                bot.send_message(message.from_user.id, 'Ты не прочитал правила. Пока не прочитаешь - задания недоступны.',
                                 reply_markup=start_keyboard)

        elif message.text in (email_yes_message,select_messages[0]):
            bot.send_message(message.from_user.id, 'Окей, на какой платформе хочешь выполнять задания?', reply_markup=platforms_keyboard)
        elif message.text in select_messages[1]:
            bot.send_message(user_id, 'Возвращаю...', reply_markup=start_keyboard)
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
                add_sex_to_user('1',user_id)
            else:
                add_sex_to_user('2',user_id)
            select = select_tasks_ids_for_user(user_id)
            if select == False:
                bot.send_message(message.from_user.id, 'Сначала сделай задание, за которое взялся',
                                 reply_markup=select_keyboard)
            elif select == 'too_many':
                bot.send_message(message.from_user.id, 'Ты сделал слишком много заданий за сегодня, приходи завтра',
                                 reply_markup=select_keyboard)
            elif select == 'banned':
                bot.send_message(user_id, 'Ты уже сегодня делал задание на этой платформе! Выбери другую!',
                                 reply_markup=select_keyboard)
            elif select is None:
                bot.send_message(message.from_user.id, 'Упс..Какая то ошибка, пробуй еще раз',
                                 reply_markup=select_keyboard)
            elif len(select) == 0:
                bot.send_message(message.from_user.id, 'Для тебя нет подходящих заданий',
                                 reply_markup=select_keyboard)
            else:
                send_sorted_tasks(user_id, select)

        # if message.text == (pk задания)
        #   if pk задания not in banned_categories для юзера
        #             выслать задание
        #             sql запрос задание выполняется

        else: bot.send_message(message.from_user.id, 'Я тебя не понимаю', reply_markup=start_keyboard)

@bot.message_handler(content_types=['photo', 'document'])
def photo_handler(message):
    sub_id=message.from_user.id
    task = select_user_now_task(message.from_user.id)
    if task == 'Задание не найдено':
        bot.send_message(sub_id, 'У тебя сейчас нет заданий на выполнении', reply_markup=start_keyboard)
        return
    bot.send_message(sub_id,'Молодец! Твое задание на проверке у админа. Как только твое задание проверят'
                                          '- тебе придет сообщение. Если все хорошо, с тобой лично свяжется админ для'
                                          ' оплаты',reply_markup=start_keyboard)
    task_id = select_user_now_task_id(message.from_user.id)
    inline_button = telebot.types.InlineKeyboardButton('Принять', callback_data=f'allow {sub_id}')
    inline_button1 = telebot.types.InlineKeyboardButton('Отклонить', callback_data=f'abadon {sub_id},{task_id}')
    inline_keyboard = telebot.types.InlineKeyboardMarkup().add(inline_button,inline_button1)
    if message.photo is not None:
        idphoto = message.photo[0].file_id
        for admin in ADMINS:
            bot.send_message(admin, f'Пользователь @{message.from_user.username} прислал скриншот на проверку\n'
                                    f'Вот его задание:\n' + task)
            bot.send_photo(admin, idphoto, reply_markup=inline_keyboard)
        update_after_task_upload(message.from_user.id)
    else:
        idphoto = message.document.file_id
        for admin in ADMINS:
            bot.send_message(admin, f'Пользователь @{message.from_user.username} прислал скриншот на проверку\n'
                                    f'Вот его задание:\n'+task)
            bot.send_document(admin, idphoto, reply_markup=inline_keyboard)
        update_after_task_upload(message.from_user.id)





def update_with_time():
    try:
        connection = connect_to_db()
        cursor = connection.cursor()
        cursor.execute('update users set today_tasks = 0, today_categories_ids = ";", new_task_today = 0')
        connection.commit()
        cursor.close()
        connection.close()
        sleep(60 * 60 * 24)

    except Exception as ex:
        print("Error")
        print(ex)


sql_time_update_thread = Thread(target=update_with_time)
sql_time_update_thread.start()

polling_thread = Thread(target=bot.polling, args=(True, 0))
polling_thread.daemon = True
polling_thread.start()





#
# while True:
#     sleep(10)
#     try:
#         print('success')
#         cursor = connection.cursor()
#         cursor.execute('select 1+1')
#         cursor.close
#         print('success')
#         # connection.close()
#         # connection = pymysql.connect(host=host,
#         #                              port=3306,
#         #                              user=user,
#         #                              password=password,
#         #                              database=db_name,
#         #                              cursorclass=pymysql.cursors.DictCursor
#         #                              )
#         #
#         # db_setting1 = 'SET SQL_SAFE_UPDATES = 0'
#         #
#         # connection.cursor().execute(db_setting1)
#         #
#         # connection.cursor().close()
#
#
#
#     except Exception as ex:
#         print("Error")
#         print(1)
#         print(ex)

