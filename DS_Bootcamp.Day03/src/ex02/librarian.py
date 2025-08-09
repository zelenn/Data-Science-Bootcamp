#!/usr/bin/env python3
import os
import sys
import subprocess

def main():
    required_env_name = "orphanfu"

    # 1. Проверим, в правильном ли мы окружении:
    current_venv = os.environ.get("VIRTUAL_ENV", None)
    if not current_venv or required_env_name not in current_venv:
        raise EnvironmentError("You are not in the correct virtual environment!")

    # 2. Установить библиотеки одной командой через requirements
    # Но сначала сформируем contents requirements:
    # Два пакета без версии, чтобы брались последние
    req_content = """beautifulsoup4
pytest
"""
    with open("temp_requirements.txt", "w") as f:
        f.write(req_content)

    subprocess.check_call([f"{current_venv}/bin/pip", "install", "-r", "temp_requirements.txt"])

    # 3. Вывести список установленных библиотек и сохранить в requirements.txt
    result = subprocess.check_output([f"{current_venv}/bin/pip", "freeze"])
    print(result.decode("utf-8"))

    with open("requirements.txt", "wb") as fw:
        fw.write(result)

    # 4. Заархивировать папку окружения
    subprocess.check_call(["tar", "-cf", "orphanfu_env.tar", current_venv])

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
        sys.exit(1)
