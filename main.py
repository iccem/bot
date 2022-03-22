import nltk
import re
import random

def filter(text):
    text = text.lower()
    punctuation = r'\W' # удалить все знаки препинания
    return re.sub(punctuation, "", text)


def match_text(text1, text2):
    text1 = filter(text1)
    text2 = filter(text2)
    distance = nltk.edit_distance(text1, text2)
    average_length = (len(text1) + len(text2)) / 2
    return distance / average_length


database = [
            {
                "question": "Как дела",
                "answer": ["Дела отлично", "Так себе", "Лучше всех"]
            },
            {
                "question": "Как тебя зовут",
                "answer": "Меня зовут Скилбокс. А как тебя зовут?"
            },
            {
                "question": "Какого цвета небо",
                "answer": "Небо голубого цвета"
            }
]

question = input()

for pair in database:
  if match_text(question, pair["question"]) < 0.4:
    answer = random.choice(pair["answer"])
    print(answer)
    
BOT_CONFIG = {
  "intents": {
    "hello": {
      "examples": ['Привет', 'Добрый день'],
      'responses': ['И тебе привет', 'Йоу']
    },
    "bye": {
      "examples": ['пока', 'До свидания'],
      'responses': ['И тебе пока', 'счастливо']
    },
    "how_are_you": {
      "examples": ['как дела', 'чего делаешь'],
      'responses': ['да ниче', 'кино смотрю']
    },
  },
      "failure_phrases": ['ниче не понял', 'шта?']
}


BOT_CONFIG['intents'].keys()

import json

config_file = open('/content/big_bot_config.json', 'r')
BOT_CONFIG = json.load(config_file)

import re
import nltk
import random
import sklearn

def normalize(text):
    text = text.lower()
    punctuation = r'[ˆ\w\s]' # удалить все знаки препинания оставляя пробелы
    return re.sub(punctuation, "", text)

def is_matching(text1, text2):
  text1 = normalize(text1)
  text2 = normalize(text2)
  distance = nltk.edit_distance(text1, text2)
  average_length = (len(text1) + len(text2)) / 2
  if average_length <= 1:
     average_length = 1
  return distance / average_length

def get_intent(text): # understanding of intence
  all_intents = BOT_CONFIG['intents']

  for name, data in all_intents.items():
    for example in data['examples']:
      if is_matching(text, example):
        return name
    
def get_answer(intent):
    responses = BOT_CONFIG['intents'][intent]['responses']
    return random.choice(responses)

def bot(text):
    intent = get_intent(text)

    if not intent:
        # подключить модель машинногоо бучения
        test = vectorizer.transform([text])
        intent = model.predict(test)[0] # по Х предсказать у, т е классифицировать

    print('Intent = ', intent)

    if intent:
        return get_answer(intent)


failure_phrases = BOT_CONFIG('failure_phrases')
random.choice(failure_phrases)
  
