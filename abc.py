import os
import sys
import subprocess
import re
import random
import threading
import time
import uuid
import requests


W = '\033[97;1m'
R = '\033[91;1m'
G = '\033[92;1m'
Y = '\033[93;1m'
B = '\033[94;1m'
P = '\033[95;1m'
S = '\033[96;1m'
N = '\x1b[0m'
LI_YELLOW = '\033[93m'
LI_GREEN = '\033[92m'
NOTE = '\x1b[38;5;203m'
PURPLE ='\x1b[38;5;46m'
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\x1b[38;5;46m'
YELLOW = '\033[1;33m'
c = '\033[1;34m'
ORANGE = '\033[1;35m'
BLACK ="\033[1;30m"
EXTRA ='\x1b[38;5;208m'
CYAN ='\033[1;96m'
red = '\x1b[1;31m'
yellow = '\x1b[1;33m'
blue = '\x1b[1;34m'
cyan = '\x1b[1;36m'
white = '\x1b[1;37m'
black = '\x1b[1;30m'
c = '\x1b[1;35m'
grey = '\x1b[1;90m'
orange = '\x1b[1;91m'
lime = '\x1b[1;92m'
sky_blue = '\x1b[1;94m'
purple = '\x1b[1;95m'
turquoise = '\x1b[1;96m'
c = '\033[1;96m'
w = '\033[1;97m'
wh = '\033[1;97m'
wh = "\033[1;37m"
ye = "\033[1;33m"
red = "\033[1;31m"
reset = '\033[0m'
r = '\033[0m'
RESET = "\033[0m"


def check_install_requests():
    required_packages = ['requests', 'chardet', 'urllib3', 'idna', 'certifi']
    try:
        import requests
        for pkg in required_packages[1:]:
            __import__(pkg)
    except ImportError as e:
        print(f"⚠️ Missing required package: {e.name}")
        try:
            subprocess.run([sys.executable, "-m", "pip", "uninstall", "-y", *required_packages],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", *required_packages])
            print("✅ Packages installed successfully")
        except Exception as install_error:
            print(f"❌ Failed to install packages: {install_error}")
            sys.exit(1)

def check_for_updates():
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        result = subprocess.run(["git", "pull"], capture_output=True, text=True)
        if result.returncode == 0:
            if "Already up to date" in result.stdout:
                print("✅ You're running the latest version")
            else:
                print("🔄 Successfully updated to the latest version")
                print("Please restart the application")
        else:
            print(f"⚠️ Update check failed: {result.stderr.strip()}")
    except Exception as e:
        print(f"⚠️ Error during update check: {str(e)}")

def W_ueragnt():
    chrome_version = random.randint(80, 99)
    webkit_version = random.randint(500, 599)
    safari_version = random.randint(400, 499)
    windows_version = random.randint(8, 10)
    is_win64 = random.choice([True, False])
    if is_win64:
        return f'Mozilla/5.0 (Windows NT {windows_version}.0; Win64; x64) AppleWebKit/{webkit_version}.0 (KHTML, like Gecko) Chrome/{chrome_version}.0.0.0 Safari/{safari_version}.0'
    return 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'


def get_device_info(default_carrier='SMART'):
    sim_id = ''
    android_version = subprocess.check_output('getprop ro.build.version.release', shell=True).decode('utf-8').replace('\n', '')
    model = subprocess.check_output('getprop ro.product.model', shell=True).decode('utf-8').replace('\n', '')
    build = subprocess.check_output('getprop ro.build.id', shell=True).decode('utf-8').replace('\n', '')
    fblc = 'en_GB'
    try:
        fbcr_list = subprocess.check_output('getprop gsm.operator.alpha', shell=True).decode('utf-8').split(',')
        if fbcr_list[0]:
            fbcr = fbcr_list[0].replace('\n', '')
            sim_id += fbcr
        elif len(fbcr_list) > 1:
            fbcr = fbcr_list[1].replace('\n', '')
            sim_id += fbcr
        else:
            fbcr = default_carrier
            sim_id += fbcr
    except:
        fbcr = default_carrier
        sim_id += fbcr
    fbmf = subprocess.check_output('getprop ro.product.manufacturer', shell=True).decode('utf-8').replace('\n', '')
    fbbd = subprocess.check_output('getprop ro.product.brand', shell=True).decode('utf-8').replace('\n', '')
    fbdv = model
    fbsv = android_version
    fbca = subprocess.check_output('getprop ro.product.cpu.abilist', shell=True).decode('utf-8').replace(',', ':').replace('\n', '')
    fbdm = f'density=2.0,height={subprocess.check_output("getprop ro.hwui.text_large_cache_height", shell=True).decode("utf-8").replace("\n", "")},width={subprocess.check_output("getprop ro.hwui.text_large_cache_width", shell=True).decode("utf-8").replace("\n", "")}'
    return {
        'android_version': android_version,
        'model': model,
        'build': build,
        'fblc': fblc,
        'fbmf': fbmf,
        'fbbd': fbbd,
        'fbdv': fbdv,
        'fbsv': fbsv,
        'fbca': fbca,
        'fbdm': fbdm
    }

device = get_device_info()

def Manual():
    user_choice = input(f"  Input y or leave blank if it's an account. If it's a page, input n (y/Y/yes/Yes or n/N/no/No or d/D/default/Default): {r}")
    
    user = input(f"USER ID/EMAIL: ")
    
    passw = input(f"PASSWORD: ")
    
    threading.Thread(target=cuser, args=(user, passw, user_choice)).start()

def ManFile():
    file = input('「?」Put file path: ')
    if os.path.isfile(file):
        user_choice = input(f" {ye}Input y or leave blank if it's an account. If it's a page, input n (y/Y/yes/Yes or n/N/no/No or d/D/default/Default): {r}")
        
        with open(file, 'r') as f:
            for line in f:
                user_pass = line.strip().split('|')
                if len(user_pass) == 2:
                    threading.Thread(target=cuser, args=(user_pass[0], user_pass[1], user_choice)).start()
                    time.sleep(2)
                else:
                    print(f"{RED}Invalid format in line: {line.strip()}")
    else:
        print(f' \033[1;31m「!」File location not found ')


def cuser(user, passw, user_choice):
    accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
    device_id = str(uuid.uuid4())
    family_device_id = str(uuid.uuid4())
    advertiser_id = str(uuid.uuid4())
    data = {...}
    headers = {...}

    try:
        response = requests.post("https://graph.facebook.com/auth/login", headers=headers, data=data, allow_redirects=False, timeout=30)
        pos = response.json() if response.text else {}
        if "session_key" in pos:
            handle_success(user, pos, user_choice)
        else:
            try_alternative_endpoints(user, passw, user_choice, device_id, family_device_id)
    except Exception as e:
        print(f"{RED}「Error」--> {user} failed due to: {e}")
        
def Auto():
    os.system('cls' if os.name == 'nt' else 'clear')
    directory = '/sdcard'
    if not os.path.exists(directory):
        directory = os.path.expanduser('~')

    txt_files = [f for f in os.listdir(directory) if f.endswith('.txt')]
    if not txt_files:
        print(f'\033[1;31m「!」No .txt files found in {directory}')
        return

    
    for i, filename in enumerate(txt_files, start=1):
        print(f"「{r}{i}」  {filename}")

    try:
        
        choice = int(input(f'「{r}Choose 」{r}»  : '))
        if 1 <= choice <= len(txt_files):
            selected_file = os.path.join(directory, txt_files[choice - 1])
            if os.path.isfile(selected_file):
                user_choice = input(f"{ye} Input y or leave blank if it's an account. If it's a page, input n (y/Y/yes/Yes or n/N/no/No or d/D/default/Default): {r}")
                
                with open(selected_file, 'r') as file:
                    for line in file:
                        user_pass = line.strip().split('|')
                        if len(user_pass) == 2:
                            threading.Thread(target=cuser, args=(user_pass[0], user_pass[1], user_choice)).start()
                            time.sleep(2)
                        else:
                            print(f"{RED}Invalid format in line: {line.strip()}")
            else:
                print(f'\033[1;31m「!」File not found ')
        else:
            print(f'{RED}「!」Invalid option.{r}')
    except ValueError:
        print(f'{RED}「!」Invalid input.{r}')

def start_tool():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("「1」MANUAL THROUGH INPUT")
    print("「2」MANUAL THROUGH FILE")
    print("「3」AUTOMATIC THROUGH OPTION")
    print('「0」BACK TO MENU!')
    
    me = input('「Choose」 : ')
    if me == '1':
        Manual()
    elif me == '2':
        ManFile()
    elif me == '3':
        Auto()
    elif me == '0' or me == '00':
        menu()
    else:
        print(f' {RED}「!」Invalid option. ')

start_tool()
