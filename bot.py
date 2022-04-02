import preparation
import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

class Bot:
    
    def start(self, text):
        p = preparation.Preparation()
        BOT_CONFIG = p.load_raw_data()
    
        X = [] # texts input
        y = [] # classes

        for name, data in BOT_CONFIG['intents'].items():
            for example in data['examples']:
                X.append(example)
                y.append(name)
                
        vectorizer = CountVectorizer() # можно указать настройки как преобразовывать
        # vectorizer = TfidfVectorizer() # можно указать настройки как преобразовывать
        vectorizer.fit(X) # передать набор текстов, чтобы векторайзер их проанализировал
                
        X_vectorized = vectorizer.transform(X) # трансформирует тексты в наборы чисел - в вектора

        # TweedieRegressor
        model = LogisticRegression(
            penalty='l2', tol=0.0005, class_weight='balanced', solver='newton-cg', max_iter=50,
            multi_class='ovr'
            # , verbose=0, warm_start=False, n_jobs=None, l1_ratio=None
            ) # настроить
        model.fit(X_vectorized, y) # модель научиться по Х определять у
        
        # test = vectorizer.transform(['как настроение у тебя сегодня'])
        # model.predict(test) # по Х предсказать у, т е классифицировать
        
        m = model.score(X_vectorized, y) # метрика качества. чем больше тем лучше
        print(m)
        
        test = vectorizer.transform([text])
        intent = model.predict(test)[0] # по Х предсказать у, т е классифицировать
        

        print('Intent = ', intent)
        
        responses = BOT_CONFIG['intents'][intent]['responses']
        print(random.choice(responses))