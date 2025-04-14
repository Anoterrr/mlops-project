FROM python:3.13-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip && pip install poetry
RUN poetry install

CMD ["poetry", "run", "uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
