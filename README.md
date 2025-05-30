# 🧠 Code Editor – SkoolOfCode Assignment Submission

## 🔗 Live Demo Links

* **Frontend (Vercel):**
  [https://code-editor-fastapi-32gnuly1c-sushma-sharons-projects.vercel.app](https://code-editor-fastapi-32gnuly1c-sushma-sharons-projects.vercel.app)

* **Backend (Render):**
  [https://code-runner-backend-gtwu.onrender.com](https://code-runner-backend-gtwu.onrender.com)

* **GitHub Repository:**
  [https://github.com/2001-su/code-editor](https://github.com/2001-su/code-editor)

---

## 📁 Project Structure

* `frontend/` – React-based VS Code-style code editor UI
* `backend/` – FastAPI service for executing Python code

Each folder includes a `README.md` for setup instructions.

---

## 📋 Test Report

See [`TEST_REPORT.md`](./TEST_REPORT.md) for sample inputs, outputs, and error handling.

---

## ✅ Features

* Online code editor with Python support
* Input/output terminal panel
* Docker-based secure code execution
* CORS-enabled frontend-backend integration
* Designed for young coders (clean UI, safe execution)

---

## 🚀 Run Locally (Optional)

### Backend (FastAPI + Docker)

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend (React)

```bash
cd frontend
npm install
npm run dev
```

---

## 📣 Submission Notes

* Docker build was optional and skipped for deployment.
* Both frontend and backend are live and integrated.
* All code committed and pushed to GitHub.
