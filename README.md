# MLOps Template 🚀

Pipeline de Machine Learning com:

- 🧠 scikit-learn / xgboost
- 📦 DVC para versionamento de dados e modelos
- 📊 MLflow para tracking de experimentos
- 🚀 FastAPI para servir modelo
- 🐳 Docker + Poetry para ambiente gerenciado

## Como usar

```bash
poetry install
poetry shell
dvc repro
mlflow ui
poetry run uvicorn src.api.main:app --reload

## Pré-requisitos

- Python 3.10+
- [Poetry](https://python-poetry.org/)
- Clone o repositório e instale:

```bash
poetry install
poetry run dvc init     # ou make dvc-init
