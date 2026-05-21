from fastapi import FastAPI
import psutil
import httpx
import time

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

@app.get("/health/services")
def check_services():

    urls = ["https://httpbin.org/status/200", "https://httpbin.org/status/500", "https://jsonplaceholder.typicode.com/posts/1"]
    response = []

    for url in urls:
        try:
            start = time.time()
            result = httpx.get(url, timeout=5)
            elapsed = round((time.time() - start) * 1000)
            response.append({
                "url": url,
                "status_code": result.status_code,
                "alive": result.status_code < 400,
                "required_time_ms": elapsed
            })
        except Exception:
            response.append({
                "url": url,
                "status_code": None,
                "alive": False,
                "error": "Could not connect",
                "required_time_ms": elapsed
            })


        
    return response

@app.get("/health/live")
def liveness():
    
    return {"status": "alive"}



@app.get("/health/ready")
def readiness():

    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent

    if cpu > 90 or memory > 90 or disk > 90:
        return {"status": "not ready"}
    return {"status": "ready"}