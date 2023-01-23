import dotenv

from tgbot_package import bot


def main():
    dotenv.load_dotenv()
    bot.telegram_bot()


if __name__ == '__main__':
    main()
