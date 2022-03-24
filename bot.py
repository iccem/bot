import nltk
import random
import sklearn
import clear_text
import import_json

c = clear_text.Clear()
j = import_json.GetJSON()
BOT_CONFIG = j.get_json()

class Bot:
    def is_matching(text1, text2):
        text1 = c.normalize(text1)
        text2 = c.normalize(text2)
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
    