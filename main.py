import nltk
import random
import data_draft
import clear_text

c = clear_text.Clear()




    
if __name__ == '__main__':
    question = input()
    # question = 'как дела'
    
    def match_text(text1, text2):
        text1 = c.filter(text1)
        text2 = c.filter(text2)
        distance = nltk.edit_distance(text1, text2)
        average_length = (len(text1) + len(text2)) / 2
        return distance / average_length

    for pair in data_draft.database:
      if match_text(question, pair["question"]) < 0.4:
          answer = random.choice(pair["answer"])
          print(answer)

# data_draft.BOT_CONFIG['intents'].keys()

# import json

# config_file = open('/content/big_bot_config.json', 'r')
# BOT_CONFIG = json.load(config_file)

# import re
# import nltk
# import random
# import sklearn



# def is_matching(text1, text2):
#   text1 = normalize(text1)
#   text2 = normalize(text2)
#   distance = nltk.edit_distance(text1, text2)
#   average_length = (len(text1) + len(text2)) / 2
#   if average_length <= 1:
#      average_length = 1
#   return distance / average_length

# def get_intent(text): # understanding of intence
#   all_intents = BOT_CONFIG['intents']

#   for name, data in all_intents.items():
#     for example in data['examples']:
#       if is_matching(text, example):
#         return name
    
# def get_answer(intent):
#     responses = BOT_CONFIG['intents'][intent]['responses']
#     return random.choice(responses)

# def bot(text):
#     intent = get_intent(text)

#     if not intent:
#         # подключить модель машинногоо бучения
#         test = vectorizer.transform([text])
#         intent = model.predict(test)[0] # по Х предсказать у, т е классифицировать

#     print('Intent = ', intent)

#     if intent:
#         return get_answer(intent)


# failure_phrases = BOT_CONFIG('failure_phrases')
# random.choice(failure_phrases)
  
