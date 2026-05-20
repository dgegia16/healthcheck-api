from fastapi import FastAPI
import psutil

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello from HealthCheck API"}

@app.get("/health")
def health():

    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent

    if cpu > 90 or memory > 90 or disk > 90:
        status = "unhealthy"
    elif cpu > 70 or memory > 70 or disk > 70:
        status = "degraded"
    else:
        status = "healthy"




    return {
        "status": status,
        "cpu_percent": cpu,
        "virtual_memory": memory,
        "disk_usage": disk
    }