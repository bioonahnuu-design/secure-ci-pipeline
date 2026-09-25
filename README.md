# 🛡️ Secure CI Pipeline Mini

[![Python Tests](https://github.com/bioonahnuu-design/secure-ci-pipeline/actions/workflows/ci.yml/badge.svg)](https://github.com/bioonahnuu-design/secure-ci-pipeline/actions/workflows/ci.yml)

A small FastAPI project for learning how to **build, test, and run an application through a CI workflow**. Every push to GitHub triggers automated tests, while Docker packages the API into a runnable container.

## ✨ What it does

| Part           | Purpose                                                  |
| -------------- | -------------------------------------------------------- |
| FastAPI        | Serves the application and health check endpoints        |
| Pytest         | Checks that both endpoints return the expected results   |
| Docker         | Packages and runs the API in a container                 |
| GitHub Actions | Runs the tests automatically on pushes and pull requests |

## 🔗 API endpoints

| Endpoint      | Example response                                      |
| ------------- | ----------------------------------------------------- |
| `GET /`       | `{"message":"Secure CI Pipeline Mini","status":"ok"}` |
| `GET /health` | `{"status":"healthy"}`                                |

The `/health` endpoint gives a quick way to check whether the running API responds.

## 🚀 Run locally

Requires Python 3.11.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

Open [http://localhost:8000/health](http://localhost:8000/health) or explore the interactive API docs at [http://localhost:8000/docs](http://localhost:8000/docs).

## 🐳 Run with Docker

From the project root:

```powershell
docker build -t secure-ci-mini:latest .
docker run --name ci-mini-app -p 8000:8000 secure-ci-mini:latest
```

Then visit [http://localhost:8000/health](http://localhost:8000/health).

To stop and start the same container later:

```powershell
docker stop ci-mini-app
docker start ci-mini-app
```

## 🧪 Run tests

```powershell
python -m pytest tests/ -v
```

Expected result: **2 passed** (`test_root` and `test_health`).

## ⚙️ How CI works

The workflow in `.github/workflows/ci.yml` runs when code is pushed or a pull request is opened. It checks out the code, sets up Python 3.11, installs `requirements.txt`, and runs pytest.

A green workflow means **these automated tests passed**. Security scans are a planned next step and are not part of the current workflow.

## 📁 Project structure

```text
secure-ci-pipeline/
├── .github/workflows/ci.yml  # Automated tests
├── app/main.py               # FastAPI application
├── tests/test_main.py        # Endpoint tests
├── Dockerfile                # Container build instructions
├── requirements.txt          # Python dependencies
└── README.md
```

## 🗺️ Next steps

- Add static code analysis with Semgrep.
- Add dependency vulnerability checks.
- Scan the Docker image with Trivy.

---

Built by **Nahnu Rohmania** as a hands-on DevSecOps learning project.
