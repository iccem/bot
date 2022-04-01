import bot


def main():
    # question = input()
    # запуск бота
    # обучить : получить сырые данные, обучиться
    #взаимодействовать
    #
    
    this_bot = bot.Bot()
    question = "как прошел твой день?"
    print(question)
    this_bot.start(question)
    # this_bot.test_bot(question)
    
    # this_bot.interact(question)


if __name__ == '__main__':
    main()
    print('Done!')
