import yaml
import mlflow
import xgboost as xgb
from joblib import dump
from src.data_prep.preprocess import load_and_split_data

# Carrega parâmetros
with open("params.yaml") as f:
    params = yaml.safe_load(f)["train"]

# Carrega e separa dados
X_train, X_test, y_train, y_test = load_and_split_data("data/raw/data.csv", params["test_size"])

# Inicializa modelo
model = xgb.XGBClassifier(
    max_depth=params["max_depth"],
    n_estimators=params["n_estimators"]
)

# Log de experimento
mlflow.start_run()
model.fit(X_train, y_train)
acc = model.score(X_test, y_test)

mlflow.log_params(params)
mlflow.log_metric("accuracy", acc)

# Salva modelo
dump(model, "models/model.pkl")
mlflow.log_artifact("models/model.pkl")
mlflow.end_run()
