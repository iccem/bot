import re


class Preprocess:
    def filter(self, text):
        text = text.lower()
        punctuation = r'\W' # удалить все знаки препинания
        return re.sub(punctuation, "", text)
    
    
    def normalize(self, text):
        text = text.lower()
        punctuation = r'[ˆ\w\s]' # удалить все знаки препинания оставляя пробелы
        return re.sub(punctuation, "", text)
    