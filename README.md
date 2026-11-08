# 🚀 Production-Grade DevOps Observability Lab

A fully containerized, production-grade observability stack built with **Flask, Prometheus, Grafana, Node Exporter, and Alertmanager**, featuring secure credential management and automated Slack alerting.

---

## 🏗️ Architecture & Tech Stack

* **Application:** Flask (Python web application simulating HTTP 500 errors to trigger alerts).
* **Metrics & Monitoring:** Prometheus (scrapes application and system metrics).
* **Node Exporter:** Collects system-level hardware and OS metrics.
* **Visualization:** Grafana (pre-configured dashboards for system health and app metrics).
* **Alerting & Notification:** Alertmanager (routes firing alerts to Slack securely using Docker Secrets).
* **Containerization:** Docker & Docker Compose (`monitoring-net` bridge network).

---

## 📂 Project Directory Structure

```text
devops-observability-lab/
├── alertmanager/
│   └── alertmanager.yml         # Alertmanager routing and Slack receiver config
├── app/
│   ├── app.py                   # Flask app with randomized HTTP 500 status codes
│   ├── Dockerfile
│   └── requirements.txt
├── docs/
│   └── screenshots/             # Dashboard and Slack alert snapshots
├── grafana/
│   └── dashboards/              # Grafana dashboard configurations
├── prometheus/
│   ├── alert.rules.yml          # Prometheus alerting rules (e.g., HighErrorRate)
│   └── prometheus.yml           # Prometheus scrape configs
├── secrets/
│   └── slack_webhook_url        # Secure Slack Webhook secret (excluded from Git)
├── .env                         # Local environment variables
├── .gitignore                   # Excludes sensitive files and credentials
├── docker-compose.yml           # Orchestration manifest for the entire stack
└── README.md

🔒 Security Best Practice (Secret Management)
To prevent exposing sensitive credentials (like the Slack Webhook URL) on GitHub, this lab utilizes Docker Secrets mount configuration (api_url_file):

The Slack Webhook URL is stored locally inside secrets/slack_webhook_url.

The secrets/ directory and .env are strictly ignored via .gitignore.

Alertmanager reads the credential file securely at runtime inside the container without hardcoding it into the configuration files.

⚙️ Getting Started & Local Deployment
1. Prerequisites
Docker & Docker Compose installed on your machine.

A Slack Incoming Webhook URL.

2. Clone the Repository
git clone [https://github.com/EslamRagab2024/devops-observability-lab.git](https://github.com/EslamRagab2024/devops-observability-lab.git)
cd devops-observability-lab

3. Run the Stack
Start all services in detached mode using Docker Compose:
docker compose up -d --build

Testing & Verification
Generate Traffic & Trigger Errors:
Run the following loop to generate HTTP requests and induce error rates (HTTP 500) to trigger alerts:
for i in {1..1500}; do curl -s -o /dev/null http://localhost:5000/; sleep 0.1; done
Verify Prometheus Alerts:
Open Prometheus in your browser to check the firing alerts:

URL: http://localhost:9090/alerts

Check Slack Notifications:
Confirm that [FIRING] and [RESOLVED] notifications are successfully received in your designated Slack channel.

📊 Access Endpoints
Flask App: http://localhost:5000

Prometheus: http://localhost:9090

Grafana: http://localhost:3000 (Default credentials: admin / admin)

Alertmanager: http://localhost:9093
