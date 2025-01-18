from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class MLModel:
    def __init__(self, historical_data):
        self.data = historical_data

    def train_model(self):
        features = self.data[["open", "high", "low", "close", "volume"]]
        labels = self.data["target"]  # 1 for buy, -1 for sell, 0 for hold

        X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

        self.model = RandomForestClassifier()
        self.model.fit(X_train, y_train)

        predictions = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        print(f"Model Accuracy: {accuracy}")

    def predict(self, tick):
        return self.model.predict([tick[["open", "high", "low", "close", "volume"]]])
