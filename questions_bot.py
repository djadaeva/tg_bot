import telebot
from telebot import types

# Создание экземпляра бота с токеном вашего бота
bot = telebot.TeleBot('5875356098:AAHjGOX-SgugwWwtl7YuID9Xe1b2t9VTkzU')

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    """Отправляет приветственное сообщение и клавиатуру с вопросами"""
    bot.send_message(message.chat.id, 'Привет! Я бот, готовый ответить на твои вопросы по QA.')
    show_question_keyboard(message.chat.id)

# Обработчик выбора вопроса из клавиатуры
@bot.callback_query_handler(func=lambda call: True)
def handle_question_choice(call):
    question_id = call.data
    answer = get_answer_by_question_id(question_id)
    bot.send_message(call.message.chat.id, answer)

# Функция для отображения клавиатуры с вопросами
def show_question_keyboard(chat_id):
    markup = types.InlineKeyboardMarkup()
    questions = ["Объясните термин «жизненный цикл программного обеспечения»", "Объясните термин «жизненный цикл разработки программного обеспечения»", "Объясните преимущество использования модели жизненного цикла разработки ПО (SDLC)"]

    for i, question in enumerate(questions):
        button = types.InlineKeyboardButton(text=question, callback_data=str(i))
        markup.add(button)

    bot.send_message(chat_id, "Выбери вопрос:", reply_markup=markup)

# Функция для получения ответа по идентификатору вопроса
def get_answer_by_question_id(question_id):
    answers = [
        'Жизненным циклом программного обеспечения (SLC) является период времени, начинающийся с момента появления концепции ПО и заканчивающийся тогда, когда использование ПО более невозможно. Жизненный цикл программного обеспечения обычно включает в себя следующие этапы: концепт, описание требований, дизайн, реализация, тестирование, инсталляция и наладка, эксплуатация и поддержка и, иногда, этап вывода из эксплуатации. Данные фазы могут накладываться друг на друга или проводиться итерационно. ',
        'Жизненным циклом разработки программного обеспечения (SDLC) является концепция, которая описывает комплекс мероприятий, выполняемых на каждом этапе (фазе) разработки программного обеспечения.',
        'В QA используются различные инструменты, такие как фреймворки для автоматизированного тестирования (например, Selenium, Appium), системы управления дефектами (например, Jira, Bugzilla), инструменты для нагрузочного тестирования (например, Apache JMeter) и другие.'
    ]
    return answers[int(question_id)]

# Запуск бота
bot.polling()
