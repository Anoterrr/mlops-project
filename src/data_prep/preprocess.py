import pandas as pd
from sklearn.model_selection import train_test_split

def load_and_split_data(path, test_size=0.2):
    df = pd.read_csv(path)
    X = df.drop("target", axis=1)
    y = df["target"]
    return train_test_split(X, y, test_size=test_size, random_state=42)
