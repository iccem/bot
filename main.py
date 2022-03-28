import bot


def main():
    # question = input()
    # запуск бота
    # обучить : получить сырые данные, обучиться
    #взаимодействовать
    #
    this_bot = bot.Bot()
    this_bot.start()
    
    question = "какого черта?"
    this_bot.interact(question)


if __name__ == '__main__':
    main()
    print('Done!')
