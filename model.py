from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import import_json

j = import_json.GetJSON()
BOT_CONFIG = j.get_json()

X = [] # texts input

y = [] # classes

# задача модели: по Х научиться находить У

for name, data in BOT_CONFIG['intents'].items():
  for example in data['examples']:
    X.append(example)
    y.append(name)
    

vectorizer = CountVectorizer() # можно указать настройки как преобразовывать
vectorizer.fit(X) # передать набор текстов, чтобы векторайзер их проанализировал
# CountVectorizer()

X_vectorized = vectorizer.transform(X) # трансформирует тексты в наборы чисел - в вектора

from sklearn.linear_model import LogisticRegression

model = LogisticRegression() # настроить
model.fit(X_vectorized, y) # модель научиться по Х определять у

test = vectorizer.transform(['как настроение у тебя сегодня'])
model.predict(test) # по Х предсказать у, т е классифицировать

model.score(X_vectorized, y) # метрика качества. чем больше тем лучше



