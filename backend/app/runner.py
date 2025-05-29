import os
import subprocess
import tempfile
import shutil
import sys

def run_code_in_docker(code: str, user_input: str = "") -> dict:
    folder_path = tempfile.mkdtemp(prefix="codeexec_")

    try:
        # Write code and input files
        code_file = os.path.join(folder_path, "main.py")
        input_file = os.path.join(folder_path, "input.txt")

        with open(code_file, "w", encoding="utf-8") as f:
            f.write(code)

        with open(input_file, "w", encoding="utf-8") as f:
            f.write(user_input)

        abs_folder_path = os.path.abspath(folder_path)

        if sys.platform == "win32":
            drive, tail = os.path.splitdrive(abs_folder_path)
            drive_letter = drive.rstrip(":").lower()
            docker_mount_path = f"/{drive_letter}{tail.replace(os.sep, '/')}"
            docker_path = r"C:\Program Files\Docker\Docker\resources\bin\docker.exe"
        else:
            docker_mount_path = abs_folder_path
            docker_path = "docker"

        docker_cmd = [
            docker_path, "run", "--rm",
            "-v", f"{docker_mount_path}:/usr/src/app",
            "-w", "/usr/src/app",
            "python:3.9",
            "bash", "-c", "cat input.txt | python main.py"
        ]

        result = subprocess.run(docker_cmd, capture_output=True, text=True, timeout=10)

        return {
            "output": result.stdout,
            "error": result.stderr
        }

    except subprocess.TimeoutExpired:
        return {"output": "", "error": "Execution timed out"}
    except Exception as e:
        return {"output": "", "error": str(e)}
    finally:
        shutil.rmtree(folder_path, ignore_errors=True)
