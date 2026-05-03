# Render Deployment Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Provide the exact steps needed to deploy the Dashboard to Render via their web interface, as no code changes are required.

**Architecture:** Render Web Service running Gunicorn and serving a Dash (Flask) application.

**Tech Stack:** Python, Gunicorn, Dash

---

### Task 1: Verify Dependencies

**Files:**
- Read: `requirements.txt`

- [ ] **Step 1: Verify Gunicorn is present**

Run: `grep gunicorn requirements.txt`
Expected: `gunicorn==22.0.0` (or similar version)

*Since `gunicorn` is already present, no code modification is needed.*

### Task 2: Configure Render Dashboard (Manual User Action)

**Files:** None (Action performed in web browser)

- [ ] **Step 1: Create a new Web Service**
Navigate to dashboard.render.com, click "New", and select "Web Service".

- [ ] **Step 2: Connect Repository**
Connect this GitHub repository to Render.

- [ ] **Step 3: Configure Settings**
Set the following values in the service settings:
- **Environment:** `Python 3`
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn --chdir ./dashboard app:server --bind 0.0.0.0:$PORT`

- [ ] **Step 4: Set Environment Variables**
In the "Environment" tab of your Render service, add the key-value pairs found in your local `.env` and `dashboard/.env` files.

- [ ] **Step 5: Deploy**
Click "Save Changes" or "Deploy". Watch the logs to verify successful startup.