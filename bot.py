import os
import sys
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

TOKEN = "8666812731:AAE5p-avCvw_ptdUWHK7bXc6og-ycv-A4s"
DEEPSEEK_API_KEY = "sk-3188092d3078430c88e51cb53c399c63"

async def start(update: Update, context):
    await update.message.reply_text("Привіт! Я бот на основі DeepSeek. Задавай мені будь-які запитання.")

async def handle_message(update: Update, context):
    user_message = update.message.text
    headers = {"Authorization": f"Bearer {DEEPSEEK_API_KEY}", "Content-Type": "application/json"}
    data = {"model": "deepseek-chat", "messages": [{"role": "user", "content": user_message}]}
    try:
        response = requests.post("https://api.deepseek.com/v1/chat/completions", headers=headers, json=data)
        reply = response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        reply = f"Помилка: {e}"
    await update.message.reply_text(reply)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Бот запущено!")
    app.run_polling()

if __name__ == "__main__":
    main()
