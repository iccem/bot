from sklearn.linear_model import LogisticRegression
import vectorize

v = vectorize.Vectorizer()
X_vectorized = v.vectorize()

class Model:
    model = LogisticRegression() # настроить
    model.fit(X_vectorized, y) # модель научиться по Х определять у

    test = v.vectorizer.transform(['как настроение у тебя сегодня'])
    model.predict(test) # по Х предсказать у, т е классифицировать

    # model.score метрика качества. чем больше тем лучше
    model.score(X_vectorized, y)
    # print(model.score(X_vectorized, y))


