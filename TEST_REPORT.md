# Code Editor – Test Report

## ✅ Submission Links

- **Frontend (Vercel):** https://code-editor-fastapi-32gnuly1c-sushma-sharons-projects.vercel.app
- **Backend (Render):** https://code-runner-backend-gtwu.onrender.com
- **GitHub Repo:** https://github.com/2001-su/code-editor

---

## 🔍 Test Summary

### 1. Run Code - Python

| Input Code | User Input | Output |
|------------|-------------|--------|
| `print("Hello, SkoolOfCode!")` | – | `Hello, SkoolOfCode!` |
| `name = input("Enter your name: "); print("Hi", name)` | `SkoolUser` | `Enter your name: Hi SkoolUser` |
| `for i in range(3): print(i)` | – | `0\n1\n2` |

### 2. Error Handling

| Input Code | Output |
|------------|--------|
| `print(1/0)` | `ZeroDivisionError: division by zero` |
| `x =` | `SyntaxError: invalid syntax` |

---

## 🧪 Test Verdict

✅ The code editor is functioning correctly for code execution, input handling, and error output via the backend API.

---

## 🧒 Designed For

Young coders – intuitive UI, responsive layout, input/output box, code highlighting.

