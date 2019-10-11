import telebot

TOKEN = '905290337:AAE-ElOZLEYQWuIivG5OMWee4OYFox_'
bot = telebot.TeleBot(TOKEN)



@bot.message_handler(commands = ['start','go'])

def start_handler(message):
	bot.send_message(message.chat.id, 'Я готов.')


@bot.message_handler(commands = ['help','hw','day',])	

def command_handler(message):
	command = message.text
	chat_id = message.chat.id
	if command == '/help':  bot.send_message(chat_id, "Команды:\n. /help - Команды\n. /start - начать\n. /go - начать\n. /hw - Домашнее задание\n. /ln - Д/З по предметам\n. /day - Д/З по дням\n. Курбан гений")

	elif command == '/help@h0mew0rk_bot':  bot.send_message(chat_id, "Команды:\n. /help - Команды\n. /start - начать\n. /go - начать\n. /hw - Домашнее задание\n. /ln - Д/З по предметам\n. /day - Д/З по дням\n. Курбан гений")
		
	
	elif command == '/hw':	bot.send_message(chat_id, "(/day)По дням.\n(/ln)По предметам.(бета)")

	elif command == '/hw@h0mew0rk_bot':	bot.send_message(chat_id, "(/day)По дням.\n(/ln)По предметам.(бета)")
		
	
	elif command == '/day':	bot.send_message(chat_id, "(/i)Понедельник.\n(/ii)Вторник.\n(/iii)Среда.\n(/iv)Четверг.\n(/v)Пятница")

	elif command == '/day@h0mew0rk_bot':	bot.send_message(chat_id, "(/i)Понедельник.\n(/ii)Вторник.\n(/iii)Среда.\n(/iv)Четверг.\n(/v)Пятница")

	else:
		bot.send_message(chat_id, "команды не существует")
		
		
@bot.message_handler(commands = ['ln','i','ii','iii','iv','v'])	

def day_command_handler(message):
	command = message.text
	chat_id = message.chat.id
	
	if command == '/i': bot.send_message(chat_id, "Предметы на Понедельник:\n(/mathl)Мат.анализ - (Лекция).\n(/fiz)Физра.\n(/rusk)Русский язык.")

	elif command == '/ii': bot.send_message(chat_id, "Предметы на Вторник:\n(/eng1g)Ин.яз(1г)\n'(/eng2g)Ин.яз(2г)' \n(/arch)Архитектура выч. сис.")

	elif command == '/iii': bot.send_message(chat_id, "Предметы на Среда:\n(/mathp)Мат.анализ - (Практика).\n(/hist)История.\n(/arch)Архитектура выч.сис.(четная неделя).")

	elif command == '/iv': bot.send_message(chat_id, "Предметы на Четверг:\n(/opl)Основы Программирования - (Лекция).\n(/opp)Основы Программирования - (Практика)(1,2 группа.).\n(/eng1g)Ин.яз(1гр)\n(/eng2g)Ин.яз(2гр)")

	elif command == '/v': bot.send_message(chat_id, "Предметы на Пятница:\n(/mathl)Мат.анализ - (Лекция)\n(/mathp)Мат.анализ - (Практика).\n(/aigl)Алгебра и гео. - (Лекция)\n(/aigp)Алгебра и гео. - (Практика).")
	

	elif command == '/ln': bot.send_message(chat_id,"""
		1)(/mathl)Мат.анализ - (Лекция).
		2)(/mathp)Мат.анализ - (Практика).
		3)(/rusk)Русский язык.
		4)(/fiz)Физ-ра.
		5)(/eng1g)Ин.яз.1(гр)
		5)(/eng2g)Ин.яз.2(гр)
		6)(/arch)Архитектура выч.сис.
		7)(/hist)История.
		8)(/opl)Основы Программирования - (Лекция).
		9)(/opp)Основы Программирования - (Практика).
		10)(/aigl)Алгебра и гео. - (Лекция).
		11)(/aigp)Алгебра и гео. - (Практика).""")

	elif command == '/ln@h0mew0rk_bot': bot.send_message(chat_id,"""
		1)(/mathl)Мат.анализ - (Лекция).
		2)(/mathp)Мат.анализ - (Практика).
		3)(/rusk)Русский язык.
		4)(/fiz)Физ-ра.
		5)(/eng1g)Ин.яз.1(гр)
		5)(/eng2g)Ин.яз.2(гр)
		6)(/arch)Архитектура выч.сис.
		7)(/hist)История.
		8)(/opl)Основы Программирования - (Лекция).
		9)(/opp)Основы Программирования - (Практика).
		10)(/aigl)Алгебра и гео. - (Лекция).
		11)(/aigp)Алгебра и гео. - (Практика).""")
	
	
	else:	
		bot.send_message(chat_id,"Этой команды не существует")

@bot.message_handler(commands = ['mathl','mathp','rusk','fiz','eng2g','eng1g','arch','hist','opl','opp','aigl','aigp'])	

def homework_command_handler(message):
	command = message.text
	chat_id = message.chat.id

	if command == '/mathl': bot.send_message(chat_id, "Домашней пока нет...")

	elif command == '/mathp': bot.send_message(chat_id, """Задачи на нахождение производной: https://ibb.co/pyjYHRb""")

	elif command == '/rusk': bot.send_message(chat_id, "Это и Лингофон: https://ibb.co/pXMVpvH")
	
	elif command == '/fiz': bot.send_message(chat_id, "Бесполезный предмет, ты типа удивлен?")
	
	elif command == '/eng1g': bot.send_message(chat_id, "Учить сценки.")

	elif command == '/eng2g': bot.send_message(chat_id, "Домашней пока нет...")

	elif command == '/arch': bot.send_message(chat_id, "Операции на ассемблере: https://ibb.co/tsVx1Ym , https://ibb.co/dbMNbbV , https://ibb.co/zFB4P81")

	elif command == '/hist': bot.send_message(chat_id, """Вопросы: 
		1)Модернизация России в начале XBIIIв. Реформы Петра и их содержание
		2)Россия в эпоху дворцовых переворотов
		3)Правление Екатерины II. https://ibb.co/album/kOjtOv""")

	elif command == '/opl': bot.send_message(chat_id, "Книга по Делфи 7: https://www.rulit.me/author/bobrovskij-s-i/delphi-7-uchebnyj-kurs-download-free-443035.html")

	elif command == '/opp': bot.send_message(chat_id, "Только практика, только хардкор")

	elif command == '/aigl': bot.send_message(chat_id, "Последняя тема: Матрицы, операции над матрицами.")

	elif command == '/aigp': bot.send_message(chat_id, " Вот эти задачи:https://ibb.co/album/mRd1tv" )
	
	else:
		bot.send_message(chat_id, "Kоманды не существует")		



@bot.message_handler(content_types = ['text','photo'])

def text_handler(message):
	text = message.text.lower()
	chat_id = message.chat.id

	
	if text == 'привет':
		bot.send_message(chat_id, "Привет, я бот Homework, Мой создатель гений, и скоро благодаря мне тебе не придется искать домашку у других, или ждать их ответа всё будет тут")		


	
	elif text == 'курбан гений':
		bot.reply_to(message, "Согласен он гений")	
	

	elif text == 'фото':
		bot.send_message(chat_id, [""])

	elif text == 'добро пожаловать':
		bot.send_message(chat_id, "Здарова, че тут так кисло?")
	elif text == 'ты создан чтобы служить':
		bot.send_message(chat_id, "Я че типо раб твой?")
	elif text == 'ага':
		bot.send_message(chat_id, "Ну ок.")


bot.polling(none_stop = True, interval = 0)







