import os
from flask import Flask
from prometheus_client import Counter, generate_latest

PORT = int(os.environ.get("APP_PORT", 5000))
APP_NAME = os.environ.get("APP_NAME", "Exemplo Padrão")

app = Flask(__name__)

REQUEST_COUNT = Counter('app_requests_total', 'Total de requisições')

@app.route("/")
def home():
    REQUEST_COUNT.inc()
    return f"Aplicação de Exemplo ({APP_NAME}) rodando no Kubernetes!"

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {'Content-Type': 'text/plain; charset=utf-8'}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)