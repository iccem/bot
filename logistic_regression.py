from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

class LogisticRegressionModel:
    
    model = LogisticRegression()
    vectorizer = CountVectorizer()
    
    
    def train_model(self, train_data):
        
        X_vectorized = train_data[0]
        y = train_data[1]
        # модель учится по Х определять у
        self.model.fit(X_vectorized, y)
        
        
    def test_model(self, train_data, text):
        self.train_model(train_data)
        # test = self.vectorizer.transform(['как настроение у тебя сегодня'])
        test = self.vectorizer.transform([text])
        intent = self.model.predict(test)
        return intent
