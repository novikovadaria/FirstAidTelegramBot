from bot import Bot
from tools import Tools



def main():

    input("Нажми Enter ")

    config = Tools.load_config()
    bot_replies = Tools.load_replies()
    my_bot = Bot(config, bot_replies, "issues")

    my_bot.init()

if __name__ == '__main__':
    main()