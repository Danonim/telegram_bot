import telebot

TOKEN = "5778137158:AAEUpmj3Gw6tamDHdarLAFYj_kxxA7xRReY"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def count(message):
    num_of_chars = len(message.text)
    bot.send_message(message.chat.id, str(num_of_chars))

bot.infinity_polling()
