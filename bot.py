# from multiprocessing.spawn import prepare
import nltk
import random
# import sklearn
# import text_preprocessing
# import raw_data
import preparation
# import vectorize
# import model
import logistic_regression

# c = text_preprocessing.Preprocess()
# j = raw_data.Data()
# BOT_CONFIG = j.get_data()
# v = vectorize.Vectorizer()
prepared_data = []

class Bot:
    def start(self):
        p = preparation.Preparation()
        prepared_data = p.prepare_bot()
        logistic_regression_model = logistic_regression.LogisticRegressionModel()
        #
        prepare_bot = logistic_regression_model.train_model(prepared_data)
        print(prepare_bot)
        # intent = logistic_regression_model.test_model(prepared_data, user_text)
        
    
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

    # def interact(self, text):
    #     intent = Bot.get_intent(self, text)

    #     if not intent:
    #         # подключить модель машинного бучения
    #         test = v.vectorizer.transform([text])
            
    #         # по Х предсказать у, т е классифицировать
    #         intent = model.predict(test)[0]

    #     print('Intent = ', intent)

    #     if intent:
    #         result = self.get_answer(intent)
    #         return result


    #     failure_phrases = BOT_CONFIG('failure_phrases')
    #     random.choice(failure_phrases)
    
    def interact(self, text):
    
        # подключить модель машинного бучения
        # test = v.vectorizer.transform([text])
        
        # по Х предсказать у, т е классифицировать
        # intent = model.predict(test)[0]

        # print('Intent = ', intent)

        # if intent:
        #     result = self.get_answer(intent)
        #     return result


        # failure_phrases = BOT_CONFIG('failure_phrases')
        # random.choice(failure_phrases)
        pass