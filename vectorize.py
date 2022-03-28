from tkinter import NO
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
# import raw_data

# j = raw_data.Data()
# BOT_CONFIG = j.get_data()
BOT_CONFIG = None

X = [] # texts input
y = [] # classes


# задача модели: по Х научиться находить У
class Vectorizer():

    # тексты векторизовать - преобразовать в числа
    # можно указать настройки как преобразовывать
    vectorizer = CountVectorizer() 
    
    # def get_data(self):
    #     return BOT_CONFIG
    
    def vectorize(self, BOT_CONFIG):
        BOT_CONFIG = self.get_data()
        
        for name, data in BOT_CONFIG['intents'].items():
            for example in data['examples']:
                X.append(example)
                y.append(name)
                
            
            # передать набор текстов, чтобы векторайзер их проанализировал
            self.vectorizer.fit(X) 
            # CountVectorizer()


        # трансформирует тексты в наборы чисел - в вектора
        X_vectorized = self.vectorizer.transform(X) 
        return X_vectorized, y
