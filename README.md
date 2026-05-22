# System Healthcheck API


A REST API that checks health status of the system

## Endpoints

- 'GET /' - API info
- 'GET /health' - Health status of the system with the cpu | memory | disk percentages
- 'GET /health/services' - checks the health status of the specific url
- 'GET /health/live' - checks if the process is running
- 'GET /health/ready' - checks if the process is ready to handle traffic


## Run Locally

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Open http://localhost:8000/docs for Swagger UI.


## Docker

```bash
docker build -t healthcheck-api .
docker run -p 8000:8000 healthcheck-api
```

## Kubernetes

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```


## CI/CD

GitHub Actions runs on every push to main — tests the app and builds the Docker image.