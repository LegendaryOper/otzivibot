import telebot

token = '5181846470:AAEQZCDqenxYj29lH25KXBxuwKoKCpASVwc'
ADMINS = [761983343]
bot = telebot.TeleBot(token)

start_message = 'Привет, я бот для заработка на выполнении простых заданий. Если хочешь заработать, нажимай на кнопку ниже'

# стартовая клава
start_keyboard = telebot.types.ReplyKeyboardMarkup(True)
zarab_message = 'Зарабатывать🔥🔥🔥'
rekviz_message = 'Ввести свои реквизиты'
account_message = 'Мой аккаунт'
start_keyboard.row(zarab_message,rekviz_message)

# клава на владение акком одной из платформ
email_acсess_keyboard = telebot.types.ReplyKeyboardMarkup(True)
email_yes_message = 'Да😀'
email_no_message = 'Нет😩'
email_acсess_keyboard.row(email_yes_message, email_no_message)

# платформы, используемые в сообщении
for_message_platforms = ['Яндекс', 'Google']

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
account_messages = ['Вернуться к заданиям', 'Изменить информацию об аккаунте']
account_keyboard.row(account_messages[0], account_messages[1])







@bot.message_handler(content_types=['text'])
def message_text_handler(message):
    print(message.text)
    if message.text == '/start':
        bot.send_message(message.from_user.id, start_message, reply_markup=start_keyboard)
    if message.text == account_message:
        bot.send_message(message.from_user.id,'Вот информация о твоем аккаунте', reply_markup=account_keyboard)
        # sql запрос спиздить фулл инфу об аккаунте
        pass
    if message.text == account_messages[0]:
        # вернуть обратно
        pass
    if message.text == account_messages[1]:
        #sql фулл перезапись данных юзера
        pass

    if message.text == zarab_message:
        bot.send_message(message.from_user.id, 'Окей, у тебя есть электронная почта?', reply_markup=email_acсess_keyboard)
    if message.text == rekviz_message:
        bot.send_message(message.from_user.id, 'Введи свои реквизиты(Qiwi,Webmoney,Сбер и т.д)')
        # как то спиздить инфу после этого сообщения
        # sql запрос на занесение реквизитов в бд
        bot.send_message(message.from_user.id, 'Окей, спасибо', reply_markup=start_keyboard)

        pass
    if message.text == email_yes_message:
        bot.send_message(message.from_user.id, 'Окей, на какой платформе хочешь выполнять задания?', reply_markup=platforms_keyboard)
    if message.text == email_no_message:
        bot.send_message(message.from_user.id, 'Для работы с нами тебе нужно иметь аккаунт хотя '
                                               'бы на одной из этих платформ:')
        bot.send_message(message.from_user.id, ', '.join(for_message_platforms))
        bot.send_message(message.from_user.id, 'Приходи, как зарегистрируешься', reply_markup=email_acсess_keyboard)
    if message.text in for_message_platforms:
        #sql запрос
        bot.send_message(message.from_user.id, 'Понял, какого ты пола?', reply_markup=sex_keyboard)
    if message.text in sex_messages:
        if message.text == message.text[0]:
            # sql запрос мужской пол
            pass
        else:
            # sql запрос женский пол
            pass
        bot.send_message(message.from_user.id, 'Держи доступные задания на этой платформе:', reply_markup=sex_keyboard)
        # sql запрос чтобы спиздить описание заданий по категории

    # if message.text == (описание задания)
    #         выслать задание
    #         sql запрос задание выполняется








bot.polling(none_stop=True, interval=0)
