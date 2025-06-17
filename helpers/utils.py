import joblib
import sklearn

def load_joblib_file(filepath):
    with open(filepath, 'rb') as file:
        return joblib.load(file)