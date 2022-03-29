from telnetlib import NOP
import raw_data
import vectorize
import model


class Preparation():
    
    def __init__(self):
        self.BOT_CONFIG = None
        self.data_model = None

    # self.raw_json = None
    # BOT_CONFIG = None
    # data_model = None
    
    def _load_raw_data(self):
        data = raw_data.Data()
        self.BOT_CONFIG = data.get_data()
        
    
    def _prepare_data__vectorize(self):
        v = vectorize.Vectorizer()
        
        # X_vectorized, y
        # self.data_model = v.vectorize(self.BOT_CONFIG)
        return v.vectorize(self.BOT_CONFIG)
    
    # def _train_model(self):
    #     m = model.Model()
    #     m.train(self.data_model)
    #     # return trained model
    #     # data_model = self.prepare_data__vectorize()
    #     # X_vectorized = data_model[0]
    #     # y = data_model[1]
    #     pass
    
    def prepare_bot(self):
        self._load_raw_data()
        self.data_model = self._prepare_data__vectorize()
        return self.data_model