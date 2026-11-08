# Production-Ready DevOps Observability Stack

An end-to-end local observability and monitoring solution built with **Python (Flask)**, **Prometheus**, **Grafana**, and **Alertmanager**, containerized using **Docker Compose** on **Red Hat Enterprise Linux 9 (RHEL 9)**.

This project demonstrates core Site Reliability Engineering (SRE) and DevOps principles, including microservice metric instrumentation, custom PromQL SLI/SLO dashboards, automated rule-based alerting, and VM storage management.

---

## Architecture Overview
[ Flask Application ] ---> Exposes /metrics ---> [ Prometheus ] ---> Visualizes ---> [ Grafana ]
|                                              |
+-- (Triggers Alerts) -------------------------+
* **Application Layer:** Lightweight Python Flask Web Server instrumented with `prometheus_client`.
* **Metrics Collector:** Prometheus scraping custom application metrics every 15 seconds.
* **Visualization Layer:** Grafana provisioning dynamic dashboards for Request Rates (RPS) and Error Percentages.
* **Alerting Mechanism:** Pre-configured Prometheus alert rules for high error rates and instance unavailability.

---

## Tech Stack & Tools

* **OS / Environment:** Red Hat Enterprise Linux 9 (RHEL 9), VMware Workstation
* **Containerization:** Docker & Docker Compose
* **Languages & Frameworks:** Python (Flask), PromQL
* **Monitoring & Observability:** Prometheus v2.51, Grafana v10.4

---

## Features & Implementation Details

1. **Custom Application Instrumentation:**
   * Tracks total HTTP requests broken down by status codes and HTTP methods (`http_requests_total`).
   * Measures HTTP request latency histograms.

2. **SLI / SLO Dashboards:**
   * **Throughput (RPS):** `sum(rate(http_requests_total[1m]))`
   * **Error Rate (%):** `sum(rate(http_requests_total{http_status=~"5.."}[1m])) / sum(rate(http_requests_total[1m])) * 100`

3. **Prometheus Alerting Rules:**
   * `HighErrorRate`: Triggers if the 5xx status code error rate exceeds 5% over a 5-minute window.
   * `InstanceDown`: Triggers if any target service becomes unreachable (`up == 0`).

---

## Getting Started

### Prerequisites

* Docker & Docker Compose installed on RHEL 9 (or Linux host).
* Git for version control.

### Quick Start

1. Clone the repository:
   ```bash
   git clone [https://github.com/EslamRagab2024/devops-observability-lab.git](https://github.com/EslamRagab2024/devops-observability-lab.git)
   cd devops-observability-lab
Launch the full stack:
docker compose up -d
Access the endpoints:

Flask App: http://localhost:5000

App Metrics: http://localhost:5000/metrics

Prometheus UI: http://localhost:9090

Grafana Dashboard: http://localhost:3000 (Default login: admin / admin)

