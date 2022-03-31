from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

class LogisticRegressionModel:
    
    
    
    # def train_model(self, train_data):
        
    #     X_vectorized = train_data[0]
    #     y = train_data[1]
    #     # модель учится по Х определять у
    #     self.model.fit(X_vectorized, y)
        
        
    def test_model(self, text, train_data):
        model = LogisticRegression()
        vectorizer = CountVectorizer()
        X_vectorized = train_data[0]
        y = train_data[1]
        # модель учится по Х определять у
        model.fit(X_vectorized, y)
        # self.train_model(self, train_data)
        # local_vectorizer = CountVectorizer()
        # test = local_vectorizer.transform(['как настроение у тебя сегодня'])
        test = vectorizer.transform([text])
        intent = model.predict(test)[0]
        # test = self.vectorizer.transform(['как настроение у тебя сегодня'])
        # self.model.predict(test) # по Х предсказать у, т е классифицировать
        return intent
