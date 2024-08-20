import nest_asyncio
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Применение nest_asyncio
nest_asyncio.apply()


# Обработчик команды /start
async def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    await update.message.reply_text(f'Привет, {user.first_name}!')


# Главная функция
async def main() -> None:
    # Создание приложения и добавление обработчиков
    application = Application.builder().token("7005144767:AAE0VP2nkpvEr-I_X78oAYn9_LT5VYEbAxo").build()

    # Регистрация обработчика команды /start
    application.add_handler(CommandHandler("start", start))

    # Запуск бота
    await application.run_polling()


# Запуск основного кода
if __name__ == "__main__":
    asyncio.run(main())
