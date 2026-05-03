# Render Deployment Design for Capital Vision Dashboard

## 1. Overview
This document specifies the deployment configuration for the Capital Vision Dash application on Render's web service platform. The deployment relies on manual configuration via the Render Dashboard.

## 2. Architecture & Environment
- **Platform:** Render Web Service
- **Runtime:** Python
- **Application Server:** Gunicorn (WSGI)
- **Application Framework:** Dash (Flask)

## 3. Build Configuration
- **Dependencies:** The application dependencies will be managed via `requirements.txt` located in the repository root.
- **Verification:** Ensure `gunicorn` is listed in `requirements.txt`.
- **Build Command:**
  ```bash
  pip install -r requirements.txt
  ```

## 4. Runtime Configuration
- **Start Command:**
  ```bash
  gunicorn --chdir ./dashboard app:server --bind 0.0.0.0:$PORT
  ```
- **Context:** The `--chdir` flag is necessary because the application's entry point (`app.py`) and its relative resources (e.g., `data/banks-n-nonbanking.csv`) reside in the `dashboard/` directory. 
- **Port Binding:** Gunicorn is bound to `0.0.0.0:$PORT` to allow Render to route external HTTP traffic to the application.

## 5. Environment Variables & Secrets
- The project currently contains `.env` files (one in the root, one in `dashboard/`).
- **Action:** All key-value pairs from these `.env` files must be manually replicated in the Render Dashboard's "Environment Variables" section to ensure the application has the necessary runtime configurations.
