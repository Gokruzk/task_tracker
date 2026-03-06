# 🚀 Task Tracker - Full Stack Dockerized
---

## 🏗️ Architectural Overview

The system is designed with scalability and security in mind:

* **Frontend Isolation:** Built using a **Multi-stage Docker build**. The code is compiled in a Node.js environment and then served by a high-performance, lightweight **Nginx** server.
* **Secure API:** A Django-powered REST API that implements strict data isolation (multi-tenancy), ensuring users can only access their own data.
* **Database Reliability:** Utilizes **PostgreSQL 16 (Alpine)** for persistent data storage with optimized ICU collation for Docker environments.
* **Reverse Proxy:** Nginx handles SPA routing (History Mode) and acts as a gateway to the backend.

[Image of Docker multi-stage build workflow for a frontend application]

---

## 🛠️ Tech Stack

| Component | Technology |
| :--- | :--- |
| **Backend** | Python 3.13 + Django 5.x + DRF |
| **Frontend** | Vue 3 + Vite + Vuetify + Yarn |
| **Database** | PostgreSQL 16 (Alpine) |
| **Web Server** | Nginx |
| **Containerization** | Docker & Docker Compose |

---

## ⚙️ Environment Configuration

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Gokruzk/task_tracker
    cd task-tracker
    ```

2.  **Setup `.env` file:**
    Create a `.env` files based en .env_template.txt 
    > **Note for DevOps:** If your `SECRET_KEY` contains `$` symbols, you **must** escape them with `$$` to prevent Docker Compose interpolation errors.
    > 
---

## 🚀 Quick Start (Docker Compose)

Launch the entire stack (Database, API, and Web) with a single command:

```bash
docker compose up --detach
