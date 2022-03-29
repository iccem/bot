from sklearn.linear_model import LogisticRegression
import vectorize

class Model:
    
    def train(self, data_model):
        v = vectorize.Vectorizer()
        
        X_vectorized = data_model[0]
        y = data_model[1]
        
        model = LogisticRegression()
        model.fit(X_vectorized, y) # модель учится по Х определять у



        test = v.vectorizer.transform(['как настроение у тебя сегодня'])
        model.predict(test) # по Х предсказать у, т е классифицировать

        # model.score метрика качества. чем больше тем лучше
        model.score(X_vectorized, y)
        
        print(model.score(X_vectorized, y))


