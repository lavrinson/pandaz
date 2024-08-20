from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from models import Session, User
from config import TELEGRAM_TOKEN


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    user_id = str(user.id)
    first_name = user.first_name
    last_name = user.last_name
    username = user.username

    # Получение профиля пользователя
    profile_photo = ''
    photos = await user.get_profile_photos()
    if photos.total_count > 0:
        profile_photo = photos.photos[0][0].file_id  # Получаем ID первой фотографии

    # Запись в базу данных
    session = Session()
    existing_user = session.query(User).filter_by(id=user_id).first()
    if existing_user:
        existing_user.first_name = first_name
        existing_user.last_name = last_name
        existing_user.username = username
        existing_user.profile_photo = profile_photo
    else:
        new_user = User(
            id=user_id,
            first_name=first_name,
            last_name=last_name,
            username=username,
            profile_photo=profile_photo
        )
        session.add(new_user)
    session.commit()
    session.close()

    await update.message.reply_text(f"Привет, {first_name}!")


def main():
    # Создайте экземпляр Application и передайте токен бота
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # Регистрация обработчика команд
    application.add_handler(CommandHandler("start", start))

    # Запуск бота
    application.run_polling()


if __name__ == '__main__':
    main()
