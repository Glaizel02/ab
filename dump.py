#-----------------[ MODULE ]-------------------#
import os
def modules():
	os.system('pkg update -y && pkg upgrade -y')
	os.system('clear')
	try: 
		import rich
	except ModuleNotFoundError:
		print("\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;97mRICH IS BEING INSTALLED \033[1;37m")
		os.system('pip install rich --quiet')
		print("\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;97mRICH HAS BEEN INSTALLED \033[1;37m")
	except:exit()
	try:
		import bs4
	except ModuleNotFoundError:
		print("\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;97mBS4 IS BEING INSTALLED \033[1;37m")
		os.system('pip install bs4 --quiet')
		print("\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;97mBS4 HAS BEEN INSTALLED \033[1;37m")
	except:exit()
	try:
		import requests
	except ModuleNotFoundError:
		print("\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;97mREQUESTS IS BEING INSTALLED \033[1;37m")
		os.system('pip install requests --quiet')
		print("\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;97mREQUESTS HAS BEEN INSTALLED \033[1;37m")
	except:exit()
	exit()
try:
	import requests,bs4,json,os,sys,random,datetime,time,re,multiprocessing,socket,marshal
	import os, requests, marshal, zlib, base64
	from bs4 import BeautifulSoup as bs
	from bs4 import BeautifulSoup
	import urllib3,rich,base64
	from rich.table import Table as me
	from rich.console import Console as sol
	from bs4 import BeautifulSoup as sop
	from concurrent.futures import ThreadPoolExecutor as tred
	from rich.console import Group as gp
	from rich.panel import Panel as nel
	from rich.panel import Panel
	from rich.tree import Tree
	from rich.panel import Panel as nel
	from rich.panel import Panel as panel
	from rich import print as cetak
	from rich.markdown import Markdown as mark
	from rich.columns import Columns as col
	from rich import print as prints
	from rich import pretty
	from rich.text import Text as tekz
	from time import localtime as lt	
	import os,requests,json,time,re,random,sys,uuid,string,subprocess,platform
	from concurrent.futures import ThreadPoolExecutor as ThreadPool
	pretty.install()
	CON=sol()
except ModuleNotFoundError:
	modules()	
#------------[ COLOR ]--------------#
P = '\x1b[1;97m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[38;5;50m'
Z = "\x1b[38;5;83m"
X = "\x1b[38;5;46m"
m = '\x1b[1;91m'
b = '\33[1;96m'	
#---------------------[ IP ]---------------------#
try:
	net = requests.get("http://ip-api.com/json/").json()["isp"]
	ipxx = requests.get("https://api.ipify.org").text    
except requests.exceptions.ConnectionError:
	print("\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;91mCHECK YOUR INTERNET")
	time.sleep(1)
	exit()
#------------------[ USER-AGENT ]-------------------#
def generate_user_agent():
    application_version = f"{random.randint(11, 77)}.0.0.{random.randrange(9, 49)}{random.randint(11, 77)}"
    application_version_code = str(random.randint(000000000, 999999999))
    ua = (
        f"[FBAN/FB4A;FBAV/{application_version};FBBV/{application_version_code};"
        "{density=3.75,width=1080,height=2400};FBLC/en_NZ;FBRV/{random.randint(000000000, 999999999)};"
        "FBCR/Etisalat Af;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/CPH2209;FBSV/10;FBOP/19;"
        "FBCA/armeabi-v7a:armeabi;]")
    return ua
#--------------------[ UA-UPDATE ]--------------#
Ua = generate_user_agent()
#------------------[ CUTS ]---------------#
def clear():
    os.system('clear')
    print(logo)
def back():
    menu()	
def contact():
    os.system('xdg-open https://www.facebook.com/profile.php?id=100001258908140')
    back()
def linex():
    print(f"\x1b[38;5;40m─────────────────────────────────────────────")
def animation(u):
    for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)    
#------------------[ VERSION ]-----------------#
____Version____ = 'V/0.1'
#------------------[ LOGO ]-----------------#
logo =f"""
\x1b[38;5;46m████████ ███    ███ ██   ██  \x1b[1;97m• \x1b[38;5;46mETHAN KLEIN HUILEN
\x1b[38;5;46m   ██    ████  ████  ██ ██   \x1b[1;97m• \x1b[38;5;46mMR-TMX-404
\x1b[38;5;46m   ██    ██ ████ ██   ███    \x1b[1;97m• \x1b[38;5;46mPREMIUM
\x1b[38;5;46m   ██    ██  ██  ██  ██ ██   \x1b[1;97m• \x1b[38;5;46mFILE MAKING
\x1b[38;5;46m   ██    ██      ██ ██   ██  \x1b[1;97m• \x1b[38;5;46m{____Version____}
\x1b[38;5;40m─────────────────────────────────────────────
\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;97mTELEGRAM : https://t.me/open_source_gift
\x1b[38;5;40m─────────────────────────────────────────────"""
#--------------------[ ENTRY ]--------------#
def entr():
    clear()
    print("\x1b[1;97m[\x1b[38;5;46m1\x1b[1;97m] \x1b[1;97mLOGIN TOOL BY COOKIE")
    print("\x1b[1;97m[\x1b[38;5;46m2\x1b[1;97m] \x1b[1;97mWITHOUT COOKIE MENU ")
    print("\x1b[1;97m[\x1b[38;5;46m3\x1b[1;97m] \x1b[1;97mCONTACT ADMIN ")
    linex()
    ll = input('\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;97mCHOOSE : ')
    if ll == '1':
        login()
    elif ll == '2':        
        menu_next()
    elif ll == '3':        
        contact()
    else:
        linex()
        animation('\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;91mSELECT CORRECTLY')
        time.sleep(3)
        entr()
#--------------------[ LOGIN BY COOKIE ]--------------#    
ses = requests.Session()
def login():

	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = '# INTERNET CONNECTION PROBLEM, CHECK AND TRY AGAIN'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi334()

def login_lagi334():
 clear()
 try:
  print("\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;97mUSE INSTAGRAM ADDED COOKIE")
  linex()
  cookie=input(f'\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;97mENTER COOKIE :\x1b[38;5;46m ')
  linex()
  open(".cok.txt", "w").write(cookie)
  with requests.Session() as rsn:
   try:
    rsn.headers.update({
                    'Accept-Language': 'id,en;q=0.9',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
                    'Referer': 'https://www.instagram.com/',
                    'Host': 'www.facebook.com',
                    'Sec-Fetch-Mode': 'cors',
                    'Accept': '*/*',
                    'Connection': 'keep-alive',
                    'Sec-Fetch-Site': 'cross-site',
                    'Sec-Fetch-Dest': 'empty',
                    'Origin': 'https://www.instagram.com',
                    'Accept-Encoding': 'gzip, deflate',
                })
    response = rsn.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey_/', cookies={'cookie':cookie})
    if '"access_token":' in str(response.headers):
     token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
     print(f"\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;97mUR TOKEN : \x1b[38;5;46m{token}")
     open(".token.txt", "w").write(token)     
     linex();animation('\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[38;5;46mLOGIN SUCCESSFULLY');linex();xxz = input('\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;97mPRESS ENTER TO MENU');menu()
    else:
     print(''%(m, p))
   except:
    animation(f'\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;91mCOOKIE EXPIRED');linex();xxz = input('\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;97mPRESS ENTER TO BACK');back()
  print(f'');time.sleep(1)
  exit()
 except Exception as e:
  os.system("rm -f .token.txt")
  os.system("rm -f .cok.txt")
  animation('\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;91mSELECT CORRECTLY')
  print(e)
  exit()
#------------------[ MENU ]----------------#
def menu():
    clear()
    try:
        cok = open('.cok.txt','r').read()
        token = open('.token.txt','r').read()
    except (IOError,KeyError,FileNotFoundError):
        entr()
    try:
        info_datafb = ses.get(f"https://graph.facebook.com/me?fields=name,id&access_token={token}", cookies = {'cookies':cok}).json()
        id = info_datafb["id"]
        nama = info_datafb["name"]
    except requests.exceptions.ConnectionError:
        exit('\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;91mCHECK YOUR INTERNET')
    except KeyError:
        try:
            os.remove(".cok.txt")
            os.remove(".token.txt")
        except:
            pass  
    print(f'\x1b[1;97m[\x1b[38;5;46m1\x1b[1;97m] \x1b[1;97mCREATE MIX SERIES FILE\n\x1b[1;97m[\x1b[38;5;46m2\x1b[1;97m] \x1b[1;97mCREATE NEW SERIES FILE\n\x1b[1;97m[\x1b[38;5;46m3\x1b[1;97m] \x1b[1;97mCREATE FILE FROM FOLLOWERS\n\x1b[1;97m[\x1b[38;5;46m4\x1b[1;97m] \x1b[1;97mSEPARATE FILE IDS\n\x1b[1;97m[\x1b[38;5;46m5\x1b[1;97m] \x1b[1;97mREMOVE DUP ID\n\x1b[1;97m[\x1b[38;5;46m0\x1b[1;97m] \x1b[1;91mLOGOUT')
    linex()
    HEART = input('\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;97mCHOOSE : ')
    if HEART in ['111']:
        login()
        dump_massal()
    elif HEART in ['1']:
        dump_file()
    elif HEART in ['02','2']:
    	dump_new()
    elif HEART in ['03','3']:
    	print('COMING SOON')
    elif HEART in ['4','04']:
        saprate()
    elif HEART in ['5','05']:
        remove_dub()
    elif HEART in ['0']:    			
        os.system('rm -rf .cok.txt && rm -rf .token.txt');linex()
        animation('\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[38;5;46mSUCESSFULLY REMOVED COOKIE')
        entr()
    else:
        animation("\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;91mINVALID OPTION")
        back()
#------------------[ MENU NEXT ]----------------#
def menu_next():
    clear()
    print('\x1b[1;97m[\x1b[38;5;46m1\x1b[1;97m] \x1b[1;97mSEPARATE LINK')
    print('\x1b[1;97m[\x1b[38;5;46m2\x1b[1;97m] \x1b[1;97mREMOVE DUP ID')
    print('\x1b[1;97m[\x1b[38;5;46m3\x1b[1;97m] \x1b[1;97mBACK TO MENU')
    linex()
    nyx = input('\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;97mCHOOSE : ')
    if nyx == '111':
        login()
        dump_massal()
    elif nyx == '1':
        saprate()
    elif nyx == '2':
        remove_dub()
    elif nyx == '0':
    	back()
    else:
        animation("\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;91mINVALID OPTION")
        menu_next()
#----------------[ CREATE FILE ]-----------------#
import requests
import random
import time

file_name = ''

def dump_file():
    global file_name
    idxx = []  
    clear()
    try:
        token = open('.token.txt', 'r').read().strip()
        cok = open('.cok.txt', 'r').read().strip()
    except IOError:
        login()
    print('\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;97mENTER FILE NAME WITHOUT "/SDCARD/"');linex()
    naame = input('\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;97mFILE NAME : ')
    linex()
    file_name = '/sdcard/' + naame
    try:
        id_limit = int(input('\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;97mINPUT UID LIMIT : '))
        linex()
    except ValueError:
        animation("\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;91mSELECT CORRECTLY")
        return menu()
    if id_limit < 1 or id_limit > 100000000:
        animation("\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;91mLIMIT OUT OF RANGE")
        return menu()
    ses = requests.Session()
    uid = []
    id = []
    non_public_uids = []  
    color = [
        '\x1b[38;5;226m', '\x1b[38;5;46m', '\x1b[1;91m', 
        '\x1b[38;5;248m', '\x1b[38;5;44m', '\x1b[38;5;46m', 
        '\x1b[38;5;208m', '\x1b[38;5;46m', '\x1b[38;5;231m', 
        '\x1b[38;5;46m', '\x1b[1;91m'
    ]
    for SAURAVXX in range(id_limit):
        saurauuu_uidzz = input('\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;97mINPUT UID ' + str(SAURAVXX + 1) + ' : ')
        uid.append(saurauuu_uidzz)
    linex()
    wanna_limit = input('\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;97mWANNA LIMIT TO STOP (y/n): ').strip().lower()
    if wanna_limit == 'y':
        try:
            extract_limit = int(input('\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;91mSELECT LIMIT : '));linex()
        except ValueError:
            animation("\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;91mSELECT CORRECTLY")
            return menu()  
    else:
        extract_limit = 0
    try:
        speed = int(input('\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;97mENTER SPEED (1 TO 100) : '))
        if speed < 1 or speed > 100:
            raise ValueError
        speed = 101 - speed 
    except ValueError:
        animation("\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;91mSELECT CORRECTLY")
        return menu()
    total_extracted = 0
    all_private = True
    for userx in uid:
        head = {
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36'
        }
        params = {
            'access_token': token,
            'fields': 'friends'
        }
        try:
            url = requests.get(f'https://graph.facebook.com/{userx}', params=params, headers=head, cookies={'cookies': cok}).json()
            if 'error' in url:
                error_message = url['error'].get('message', '')
                if 'Unsupported get request' in error_message or 'privacy' in error_message:
                    non_public_uids.append(userx)  
                    continue
            all_private = False
            for xxx in url.get('friends', {}).get('data', []):
                abc = xxx['id']
                if abc not in id:
                    id.append(abc)
        except KeyError:
            pass
        except IOError:
            pass
        except requests.exceptions.ConnectionError:
            exit()
    if all_private:
        animation("\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;91mUID NOT PUBLIC")
        return menu()  
    linex()
    print('\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;97mTOTAL IDS DUMPED TO FILE : \x1b[38;5;46m' + str(len(id)))
    print('\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;97mUSE CTRL+Z TO STOP ')
    linex()
    for user_lado in id:
        mix_color = random.choice(color)
        if extract_limit > 0 and total_extracted >= extract_limit:  
            break
        print(f'\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;97m{mix_color}SUCCESSFULLY EXTRACTED FROM : {user_lado}')
        try:
            urlx = requests.get(f'https://graph.facebook.com/{user_lado}', params=params, headers=head, cookies={'cookies': cok}).json()
            for xyx in urlx.get('friends', {}).get('data', []):
                saurav_xx = xyx['id'] + '|' + xyx['name']
                with open(file_name, 'a') as f:
                    f.write(saurav_xx + '\n')
                if saurav_xx not in idxx:
                    idxx.append(saurav_xx)  
                    total_extracted += 1  
                    print(f"\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;97mTOTAL EXTRACTED : [{total_extracted}]   ", end='\r')
                    if extract_limit > 0 and total_extracted >= extract_limit:  
                        break  
        except KeyError:
            pass
        except IOError:
            pass
        except requests.exceptions.ConnectionError:
            exit()
        time.sleep(speed / 1000.0) 
    finish(idxx)

def finish(idxx):
    global file_name  
    linex()
    print(f'\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;97mTOTAL FETCHED IDS   : \x1b[38;5;46m{len(idxx)}')
    print(f'\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;97mDUMPED IDS SAVED IN : \x1b[38;5;46m{file_name}')
    linex()
    input('\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;97mPRESS ENTER TO GO BACK ')
    menu()
#------------------------------------[ NEW SERIES ONLY ]--------------------------------------#
import requests
import random
import time

file_name = ''

def dump_new():
    global file_name
    idxx = []  
    clear()
    try:
        token = open('.token.txt', 'r').read().strip()
        cok = open('.cok.txt', 'r').read().strip()
    except IOError:
        login()
    print('\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;97mENTER FILE NAME WITHOUT "/SDCARD/"');linex()
    naame = input('\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;97mFILE NAME : ')
    linex()
    file_name = '/sdcard/' + naame
    try:
        id_limit = int(input('\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;97mINPUT UID LIMIT : '))
        linex()
    except ValueError:
        animation("\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;91mSELECT CORRECTLY")
        return menu()
    if id_limit < 1 or id_limit > 100000000:
        animation("\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;91mLIMIT OUT OF RANGE")
        return menu()
    uid = []
    id = []
    color = [
        '\x1b[38;5;226m', '\x1b[38;5;46m', '\x1b[1;91m', 
        '\x1b[38;5;248m', '\x1b[38;5;44m', '\x1b[38;5;46m', 
        '\x1b[38;5;208m', '\x1b[38;5;46m', '\x1b[38;5;231m', 
        '\x1b[38;5;46m', '\x1b[1;91m'
    ]
    for SAURAVXX in range(id_limit):
        saurauuu_uidzz = input('\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;97mINPUT UID ' + str(SAURAVXX + 1) + ' : ')
        if saurauuu_uidzz.startswith(('6155', '6156')):
            uid.append(saurauuu_uidzz)
    linex()
    wanna_limit = input('\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;97mWANNA LIMIT TO STOP (y/n): ').strip().lower()
    if wanna_limit == 'y':
        try:
            extract_limit = int(input('\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;91mSELECT LIMIT : '));linex()
        except ValueError:
            animation("\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;91mSELECT CORRECTLY")
            return menu()
    else:
        extract_limit = 0
    try:
        speed = int(input('\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;97mENTER SPEED (1 TO 100) : '))
        if speed < 1 or speed > 100:
            raise ValueError
        speed = 101 - speed
    except ValueError:
        animation("\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;91mSELECT CORRECTLY")
        return menu()
    total_extracted = 0
    all_private = True
    for userx in uid:
        head = {
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36'
        }
        params = {
            'access_token': token,
            'fields': 'friends'
        }
        try:
            url = requests.get(f'https://graph.facebook.com/{userx}', params=params, headers=head, cookies={'cookies': cok}).json()
            if 'error' in url:
                continue
            all_private = False
            for xxx in url.get('friends', {}).get('data', []):
                abc = xxx['id']
                if abc not in id:
                    id.append(abc)
        except KeyError:
            continue
        except IOError:
            continue
        except requests.exceptions.ConnectionError:
            exit()
        time.sleep(speed / 1000.0)
    if all_private:
        animation("\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;91mUID NOT PUBLIC")
        return menu()  
    linex()
    print('\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;97mTOTAL IDS DUMPED TO FILE : \x1b[38;5;46m' + str(len(id)))
    print('\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;97mUSE CTRL+Z TO STOP ')
    linex()
    for user_lado in id:
        if extract_limit > 0 and total_extracted >= extract_limit:  
            break
        mix_color = random.choice(color)
        print(f'\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;97m{mix_color}SUCCESSFULLY EXTRACTED FROM : {user_lado}')
        try:
            urlx = requests.get(f'https://graph.facebook.com/{user_lado}', params=params, headers=head, cookies={'cookies': cok}).json()
            for xyx in urlx.get('friends', {}).get('data', []):
                saurav_xx = xyx['id'] + '|' + xyx['name']
                if saurav_xx.startswith(('6155', '6156')):
                    with open(file_name, 'a') as f:
                        f.write(saurav_xx + '\n')
                    if saurav_xx not in idxx:
                        idxx.append(saurav_xx)  
                        total_extracted += 1  
                        print(f"\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;97mTOTAL EXTRACTED : [{total_extracted}]   ", end='\r')
                        if extract_limit > 0 and total_extracted >= extract_limit:  
                            break  
        except KeyError:
            continue
        except IOError:
            continue
        except requests.exceptions.ConnectionError:
            exit()
        time.sleep(speed / 1000.0)        
    finish(idxx)

def finish(idxx):
    global file_name  
    linex()
    print(f'\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;97mTOTAL FETCHED IDS   : \x1b[38;5;46m{len(idxx)}')
    print(f'\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;97mDUMPED IDS SAVED IN : \x1b[38;5;46m{file_name}')
    linex()
    input('\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;97mPRESS ENTER TO GO BACK ')
    menu()
#-------------[ SEPRATE ID ]--------------------#
def saprate():
    clear()
    try:
        limit = int(input('\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;97mHOW MANY LINKS DO U WANT TO SEPARATE : '))
    except ValueError:
        limit = 1
    linex()
    print('\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;97mEXAMPLE : PUT YOUR FILE FOR SEPARATION')
    linex()
    print('\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;97mEXAMPLE : /sdcard/OLD.txt')
    linex()
    file_name = input('\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;97mFILE NAME : ')
    if not os.path.isfile(file_name):
        animation('\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;91mFILE NOT FOUND')
        linex()
        input('\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;97mPRESS ENTER TO BACK ')
        menu()
    linex()
    print('\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;97mPUT YOUR NEW FILE NAME')
    linex()
    print('\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;97mEXAMPLE : /sdcard/NEW.txt')
    linex()
    new_save = input('\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;97mNEW FILE NAME : ')
    linex()
    y = 0
    print('\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;97mEXAMPLE : 10001,10002,10003')
    linex()
    for k in range(limit):
        y += 1
        links = input('\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;97mPUT LINKS %s : ' % y)
        os.system(f'grep "{links}" {file_name} >> {new_save}')
    linex()
    print('\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;97mLINKS GRABBED SUCCESSFULLY')
    linex()
    print('\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;97mTOTAL GRABBED LINKS : ' + str(len(open(new_save).read().splitlines())))
    linex()
    print('\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;97mNEW FILE SAVE AS : \x1b[1;91m' + new_save)
    linex()
    input('\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;97mPRESS ENTER TO BACK ')
    menu()
#-------------[ DUB ID ]------------------#    
def remove_dub():
    clear()
    print(f"\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;97mDUBBLE LINKS CUTTER")
    linex()
    print('\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;97mEXAMPLE : /sdcard/rizzzy.txt')
    linex()
    file_path = input('\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;97mFILE NAME : ')
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
        with open(file_path, "w") as file:
            file.writelines(set(lines))
        linex()
        print("\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;97mSUCCESSFULLY REMOVED DUBBLE UIDS ")
        linex()
        print("\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;97mYOUR TOTAL IDZ :\x1b[1;91m " + str(len(open(file_path).read().splitlines())))
    except FileNotFoundError:
        animation("\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;91mFILE NOT FOUND")
    except Exception as e:
        print(f"\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;91mAN ERROR OCCURRED: {e}")
    linex()
    input('\x1b[1;97m[\x1b[38;5;46m§\x1b[1;97m] \x1b[1;97mPRESS ENTER TO BACK ')
    menu()
#-----------------------[ END ]--------------------#
menu()
