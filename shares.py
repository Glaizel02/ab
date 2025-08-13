import sys
import time
import json
import requests
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

# Color codes
green  = "\033[92m"
blue   = "\033[94m"
yellow = "\033[93m"
red    = "\033[91m"
purple = "\033[95m"
cyan   = "\033[96m"
gray   = "\033[38;2;200;200;200m"
reset  = "\033[0m"

FB_SHARE_URL = "https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed"

def clear_screen():
    print("\033c", end="")

def virus_banner():
    print(f"""{purple}
╔════════════════════════════════════════════════════════════════════════╗
║{red}   ██▒   █▓ ██▓ ███▄ ▄███▓ ▒█████    ██████   ██████  ██▓ {purple}║
║{red}  ▓██░   █▒▓██▒▓██▒▀█▀ ██▒▒██▒  ██▒▒██    ▒ ▒██    ▒ ▓██▒ {purple}║
║{red}   ▓██  █▒░▒██▒▓██    ▓██░▒██░  ██▒░ ▓██▄   ░ ▓██▄   ▒██▒ {purple}║
║{red}    ▒██ █░░░██░▒██    ▒██ ▒██   ██░  ▒   ██▒  ▒   ██▒░██░ {purple}║
║{red}     ▒▀█░  ░██░▒██▒   ░██▒░ ████▓▒░▒██████▒▒▒██████▒▒░██░ {purple}║
║{green}        ✦✦ FACEBOOK AUTO SHARE TOOL - VIRUS EDITION ✦✦      {purple}║
╚════════════════════════════════════════════════════════════════════════╝
{reset}""")

def fbstate_to_cookies(fbstate_str):
    try:
        fbstate_json = json.loads(fbstate_str)
        cookie_dict = {}
        for item in fbstate_json:
            cookie_dict[item['name']] = item['value']
        return cookie_dict
    except Exception as e:
        print(f"{red}[!] Invalid fbstate format: {e}{reset}")
        return {}

def post_with_cookies(cookies, post_id, share_number):
    try:
        session = requests.Session()
        session.cookies.update(cookies)
        data = {
            "link": f"https://www.facebook.com/{post_id}",
            "privacy": "SELF"
        }
        r = session.post(FB_SHARE_URL, data=data, timeout=15)
        return (r.status_code == 200), share_number
    except Exception:
        return False, share_number

DASH_A = "-" * 29
DASH_B = "-" * 13

def success_line():
    return (
        f"{green}SUCCESSFULLY SHARED{reset}, {gray}{DASH_A}{reset}  "
        f"{green}SUCCESSFULLY SHARED{reset}, {gray}{DASH_B}{reset}"
    )

def failed_line():
    return (
        f"{red}FAILED{reset}, {gray}{DASH_A}{reset}  "
        f"{red}FAILED{reset}, {gray}{DASH_B}{reset}"
    )

def shar():
    clear_screen()
    virus_banner()

    fbstate_inputs = input(f"{green}☣ Enter fbstate JSON (comma separated for multiple accounts): {gray}").split(',')
    print(f"{blue}{'═'*75}{reset}")

    post_id = input(f"{green}☣ Enter Post ID: {gray}")
    print(f"{blue}{'═'*75}{reset}")

    total_share = int(input(f"{green}☣ How Many Shares: {gray}"))
    print(f"{blue}{'═'*75}{reset}")

    delay = int(input(f"{green}☣ Delay Between Shares (sec): {gray}"))
    print(f"{blue}{'═'*75}{reset}")

    cookies_list = [fbstate_to_cookies(f.strip()) for f in fbstate_inputs if f.strip()]
    total_live = len([c for c in cookies_list if c])
    print(f"{green}☣ Live Accounts: {gray}{total_live}{reset}")
    if total_live == 0:
        print(f"{red}[!] No valid fbstate entered. Exiting...{reset}")
        return

    start_time = datetime.now()
    print(f"{yellow}☣ Start Time: {gray}{start_time.strftime('%Y-%m-%d %H:%M:%S')}{reset}")
    print(f"{cyan}☣ STATUS: Initializing viral infection...{reset}")
    time.sleep(1)

    stt = 0
    futures = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        while stt < total_share:
            for cookies in cookies_list:
                if stt >= total_share:
                    break
                stt += 1
                futures.append(executor.submit(post_with_cookies, cookies, post_id, stt))
                time.sleep(delay)

        for future in as_completed(futures):
            ok, num = future.result()
            if ok:
                print(success_line())
            else:
                print(failed_line())

    end_time = datetime.now()
    duration = end_time - start_time
    print(f"\n{green}☣ Infection Complete! {stt} shares executed.{reset}")
    print(f"{yellow}☣ End Time: {gray}{end_time.strftime('%Y-%m-%d %H:%M:%S')}{reset}")
    print(f"{blue}☣ Total Duration: {gray}{duration}{reset}")
    input(f"{green}Press Enter to exit...{reset}")

if __name__ == "__main__":
    shar()
