import openai
import telebot

openai.api_key = "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"
bot = telebot.TeleBot("6013759684:AAEMK6UdDc5UVepKe6iFfpKThGxBjr9VghA")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the OpenAI bot! Send me a message and I'll respond with a prediction.")

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    prompt = message.text
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=50
    )
    if response.choices[0].text:
        bot.reply_to(message, response.choices[0].text.strip())
    else:
        bot.reply_to(message, "Error: " + response)

bot.polling()
