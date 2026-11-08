import time
import random
from flask import Flask, Response
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP Requests', ['method', 'endpoint', 'http_status'])
REQUEST_LATENCY = Histogram('http_request_duration_seconds', 'HTTP request latency in seconds', ['endpoint'])

@app.route('/')
def hello():
    start_time = time.time()
    status = random.choice([200, 200, 200, 200, 500])
    
    if status == 500:
        REQUEST_COUNT.labels(method='GET', endpoint='/', http_status=500).inc()
        return "Internal Server Error Simulation", 500
    
    time.sleep(random.uniform(0.1, 0.4)) 
    REQUEST_COUNT.labels(method='GET', endpoint='/', http_status=200).inc()
    
    latency = time.time() - start_time
    REQUEST_LATENCY.labels(endpoint='/').observe(latency)
    
    return "DevOps Observability Lab - Running Successfully on RHEL 9!", 200

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)