import pandas as pd

class DataPreprocessing:
    @staticmethod
    def load_and_clean_data(file_path):
        data = pd.read_csv(file_path)
        data.dropna(inplace=True)
        data["date"] = pd.to_datetime(data["date"])
        data.set_index("date", inplace=True)
        return data
