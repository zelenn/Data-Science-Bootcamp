#!/usr/bin/env python3
import os

def main():
    venv_path = os.environ.get('VIRTUAL_ENV', None)
    if venv_path is None:
        print("No active virtual environment found.")
    else:
        print(f"Your current virtual env is {venv_path}")

if __name__ == '__main__':
    main()
