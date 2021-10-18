import telebot
import  requests 
import datetime
covid_api  = 'https://covid-api.mmediagroup.fr/v1/cases?country={country}'
token = '2083733119:AAGM_oZpvl94kx_ak4QbN1dM5G6xp02O6-U'

# covid = requests.get(covid_api)
# covid_json = covid.json()
# print(covid_json['All']['confirmed'])

# print(type(covid_json))

bot = telebot.TeleBot(token)



@bot.message_handler(commands=['start','старт'])
def send_start(message):
    bot.send_message(message.chat.id, "Hi I am COVID-BOT")


@bot.message_handler(content_types="text")
def send_data(message):    
    covid = requests.get(covid_api.format(country=message.text.title()))
    covid_json =covid.json()
    data = f"количество заболевших короновирусом в  {message.text.title()}: {covid_json['All']['confirmed']}"
    bot.send_message(message.chat.id, data)
    # bot.send_message(message.chat.id,'HI, I am COVID19-bot')
    # bot.send_message(message.chat.id, covid_json['All']['confirmed'])

print("Bot is working!")
bot.infinity_polling()
# import telebot
# import psycopg2

# #>-------------------------------------------------------------<#

# name1 = ""
# surname = ""
# age = ""

# database = 'd/z'
# user = 'postgres'
# password = 'a4'
# host = '127.0.0.1'
# port = '5432'

# connection =  psycopg2.connect(
#     database = database,
#     user = user, 
#     password = password,
#     host = host,
#     port = port 
# )

# cursor = connection.cursor()


# token = "2083733119:AAGM_oZpvl94kx_ak4QbN1dM5G6xp02O6-U"
# bot = telebot.TeleBot(token)

# @bot.message_handler(commands=["start", "старт"])
# def greetings(message):
#     markup = telebot.types.ReplyKeyboardMarkup()
#     button1 = telebot.types.KeyboardButton("Начать заполнение анкеты")
#     button2 = telebot.types.KeyboardButton("Прекратить работу бота")
#     markup.add(button1, button2)

#     user = message.from_user.first_name
#     bot.send_message(message.chat.id, "Приветсвую, "+user+" Хотите ли вы записаться на пробный урок?", reply_markup=markup)

# @bot.message_handler(content_types=["text"])
# def name(message):
#     if message.text == "Прекратить работу бота":
#         bot.send_message(message.chat.id, "Удачи!")
#     else:
#         sent_msg = bot.send_message(message.chat.id, "Введите Ваше имя.")
#         bot.register_next_step_handler(sent_msg, second_name)

# def second_name(message):
#     if message.text == "Прекратить работу бота":
#         bot.send_message(message.chat.id, "Удачи!")
#     else:
#         name1 = message.text 
#         sent_msg = bot.send_message(message.chat.id, "Введите Вашу фамилию.")
#         bot.register_next_step_handler(sent_msg, age_boy, name1)

# def age_boy(message, name1):
#     if message.text == "Прекратить работу бота":
#         bot.send_message(message.chat.id, "Удачи!")
#     else:
#         surname = message.text
#         sent_msg = bot.send_message(message.chat.id, "Введите Ваш Возраст")
#         bot.register_next_step_handler(sent_msg, final_anketa, name1, surname)

# def final_anketa(message, name1, surname):
#     if message.text == "Прекратить работу бота":
#         bot.send_message(message.chat.id, "Удачи!")
#     else:
#         age = int(message.text)
# #>-------------------------------------------------------------<#
#         cursor.execute(f"INSERT INTO people (name, second_name, age) VALUES ('{name1}', '{surname}', {age})")
#         connection.commit()
#         cursor.close()
#         connection.close()
# #>-------------------------------------------------------------<#
#         bot.send_message(message.chat.id, f"И так, подведем итоги. \nВы - {name1} {surname}, Вам {age}. \nНо что более важно, мы внесли вас в базу данных на пробный урок, приходите в 15:00 в субботу по Адресу Бобова 14.")

# print("1")
# bot.infinity_polling()