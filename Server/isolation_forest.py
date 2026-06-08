import os
import joblib
import pandas as pd
from sklearn.ensemble import IsolationForest

MODEL_PATH = "isolation_model.pkl"

class IDSIsolationForest:

    def __init__(self):
        self.model = IsolationForest(contamination=0.1)

    def extract_features(self, file_path):
        size = os.path.getsize(file_path)

        with open(file_path, "rb") as f:
            content = f.read()

        byte_sum = sum(content)
        byte_mean = byte_sum / len(content) if len(content) > 0 else 0

        return [[size, byte_sum, byte_mean]]

    def train(self):
        data = [
            [1000, 50000, 50],
            [2000, 80000, 40],
            [1500, 60000, 45]
        ]

        df = pd.DataFrame(data)
        self.model.fit(df)

        joblib.dump(self.model, MODEL_PATH)

    def predict(self, file_path):
        if not os.path.exists(MODEL_PATH):
            self.train()

        model = joblib.load(MODEL_PATH)
        features = self.extract_features(file_path)

        pred = model.predict(features)

        return "ATTACK" if pred[0] == -1 else "NORMAL"