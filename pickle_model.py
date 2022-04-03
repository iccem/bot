import pickle # сохранить модель - с помощью библиотеки

f = open('bot_model.bin', 'wb')
pickle.dump(model, f)
f.close()

ff = open('bot_model.bin', 'rb')
loaded_model = pickle.load(ff)

