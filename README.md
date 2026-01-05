# fast-track-ci
# 🚀 Automated Testing Pipeline with Docker & CI/CD

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Docker](https://img.shields.io/badge/container-docker-blue)
![Python](https://img.shields.io/badge/python-3.9-yellow)
![Testing](https://img.shields.io/badge/testing-pytest-red)

## 📖 Introduction
This project demonstrates a robust **Continuous Integration (CI) pipeline** designed for Python-based automation frameworks. 

It solves the common "it works on my machine" problem by utilizing **Docker** for environment containerization and **GitHub Actions** for automated test orchestration.

## 🛠 Tech Stack
* **Language:** Python 3.9
* **Testing Framework:** Pytest
* **Containerization:** Docker (Alpine/Slim based)
* **CI/CD:** GitHub Actions
* **Version Control:** Git

## 🏗 Architecture
The pipeline follows a "Shift-Left" testing approach:
1.  **Code Push:** Developer pushes code to the `main` branch.
2.  **CI Trigger:** GitHub Actions workflow is automatically triggered.
3.  **Container Build:** A fresh Docker environment is provisioned using the `Dockerfile`.
4.  **Test Execution:** Tests run inside the isolated container to ensure consistency.
5.  **Reporting:** Results are reported back to the GitHub UI (Pass/Fail).

## 🚀 How to Run Locally

### Option 1: Using Docker (Recommended)
Ensure you have [Docker Desktop](https://www.docker.com/products/docker-desktop) installed.

1. **Build the Image:**
   ```bash
   docker build -t sdet-pipeline-demo .
2. **Run the Test Suite:**
   ```bash
   docker run sdet-pipeline-demo
### Option 2: Traditional Python Run
1. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
3. **Run tests:**
   ```bash
   pytest -v
