import nltk
import random
# import sklearn
import text_preprocessing
import raw_data

c = text_preprocessing.Preprocess()
j = raw_data.Data()
BOT_CONFIG = j.get_data()

class Bot:
    def is_matching(self, text1, text2):
        text1 = c.normalize(text1)
        text2 = c.normalize(text2)
        distance = nltk.edit_distance(text1, text2)
        average_length = (len(text1) + len(text2)) / 2
        if average_length <= 1:
            average_length = 1
        return distance / average_length

    def get_intent(self, text): # understanding of intence
        all_intents = BOT_CONFIG['intents']

        for name, data in all_intents.items():
            for example in data['examples']:
                if self.is_matching(text, example):
                    return name
                
    def get_answer(self, intent):
        responses = BOT_CONFIG['intents'][intent]['responses']
        return random.choice(responses)

    def interact(text):
        intent = self.get_intent(text)

        if not intent:
            # подключить модель машинногоо бучения
            test = vectorizer.transform([text])
            intent = model.predict(test)[0] # по Х предсказать у, т е классифицировать

        print('Intent = ', intent)

        if intent:
            return get_answer(intent)


        failure_phrases = BOT_CONFIG('failure_phrases')
        random.choice(failure_phrases)
    