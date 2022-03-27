import bot


def main():
    # question = input()
    this_bot = bot.Bot()
    this_bot.start()
    
    question = "какого черта?"
    this_bot.interact(question)


if __name__ == '__main__':
    main()
    print('Done!')
