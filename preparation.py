import raw_data
import vectorize


class Preparation():
    # self.raw_json = None
    
    def load_raw_data(self):
        data = raw_data.Data()
        return data.get_data()
        
    
    def prepare_data__vectorize(self):
        v = vectorize.Vectorizer()
        return v.vectorize()
    
    def train_model(self):
        # return trained model
        data_model = self.prepare_data__vectorize()
        X_vectorized = data_model[0]
        y = data_model[1]
        pass
    