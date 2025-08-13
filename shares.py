import sys
import time
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

API_KEY = "62f8ce9f74b12f84c123cc23437a4a32"
FB_URL  = "https://graph.facebook.com/v13.0/me/feed"

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
║{blue}                  API KEY: {yellow}{API_KEY}                    {purple}║
╚════════════════════════════════════════════════════════════════════════╝
{reset}""")

def post_to_facebook(token, post_id, share_number):
    try:
        payload = {
            'link': f"https://www.facebook.com/{post_id}",
            'published': '0',
            'privacy': '{"value":"SELF"}',
            'access_token': token
        }
        r = requests.post(FB_URL, data=payload, timeout=15)
        return (r.status_code == 200), share_number
    except Exception:
        return False, share_number

# --- line style helpers -------------------------------------------------

DASH_A = "-" * 29
DASH_B = "-" * 13

def success_line():
    # SUCCESSFULLY SHARED, -----------------------------  SUCCESSFULLY SHARED, -------------
    return (
        f"{green}SUCCESSFULLY SHARED{reset}, {gray}{DASH_A}{reset}  "
        f"{green}SUCCESSFULLY SHARED{reset}, {gray}{DASH_B}{reset}"
    )

def failed_line():
    return (
        f"{red}FAILED{reset}, {gray}{DASH_A}{reset}  "
        f"{red}FAILED{reset}, {gray}{DASH_B}{reset}"
    )

# -----------------------------------------------------------------------

def shar():
    clear_screen()
    virus_banner()

    access_tokens = input(f"{green}☣ Enter Access Tokens (comma separated): {gray}").split(',')
    print(f"{blue}{'═'*75}{reset}")

    post_id = input(f"{green}☣ Enter Post ID: {gray}")
    print(f"{blue}{'═'*75}{reset}")

    total_share = int(input(f"{green}☣ How Many Shares: {gray}"))
    print(f"{blue}{'═'*75}{reset}")

    delay = int(input(f"{green}☣ Delay Between Shares (sec): {gray}"))
    print(f"{blue}{'═'*75}{reset}")

    access_tokens = [t.strip() for t in access_tokens if t.strip()]
    total_live = len(access_tokens)
    print(f"{green}☣ Live Tokens: {gray}{total_live}{reset}")
    if total_live == 0:
        print(f"{red}[!] No valid tokens entered. Exiting...{reset}")
        return

    start_time = datetime.now()
    print(f"{yellow}☣ Start Time: {gray}{start_time.strftime('%Y-%m-%d %H:%M:%S')}{reset}")
    print(f"{cyan}☣ STATUS: Initializing viral infection...{reset}")
    time.sleep(1)

    stt = 0
    futures = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        # queue tasks with delay
        while stt < total_share:
            for token in access_tokens:
                if stt >= total_share:
                    break
                stt += 1
                futures.append(executor.submit(post_to_facebook, token, post_id, stt))
                time.sleep(delay)

        # print one line per result in the exact style requested
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
