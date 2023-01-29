from telebot import TeleBot

# inisialisasi Token Bot Kita
bot = TeleBot('6095122638:AAGmzSmgqcs7dhGAd_Ohe_>
print('Done')
# Menghandle Pesan /start
@bot.message_handler(regexp='#testaja')
def welcome(message):
    # membalas pesan
    bot.reply_to(message, 'Halo bro, ada apa?')

while True:
    try:
        bot.polling()
    except:
        pass
