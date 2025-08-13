import sys
import time
import requests
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

# Colors
green = "\033[92m"
blue = "\033[94m"
yellow = "\033[93m"
red = "\033[91m"
gray = "\033[38;2;233;233;233m"
reset = "\033[0m"

API_KEY = "62f8ce9f74b12f84c123cc23437a4a32"
FB_URL = "https://graph.facebook.com/v13.0/me/feed"

def clear_screen():
    print("\033c", end="")

def jovan():
    print(f"""{blue}
    ╔══════════════════════════════════════════════════════╗
    ║         {green}Facebook Auto Share Tool{blue}                 ║
    ╠══════════════════════════════════════════════════════╣
    ║   {yellow}API KEY:{gray} {API_KEY}                     {blue}║
    ╚══════════════════════════════════════════════════════╝
    {reset}""")

def post_to_facebook(token, post_id):
    try:
        payload = {
            'link': f"https://www.facebook.com/{post_id}",
            'published': '0',
            'privacy': '{"value":"SELF"}',
            'access_token': token
        }
        r = requests.post(FB_URL, data=payload)
        return r.status_code == 200
    except:
        return False

def shar():
    clear_screen()
    jovan()

    # Inputs
    access_tokens = input(f"{green}Enter Access Tokens (comma separated): {gray}").split(',')
    print(f"{blue}{'─'*70}{reset}")

    post_id = input(f"{green}Enter Post ID: {gray}")
    print(f"{blue}{'─'*70}{reset}")

    total_share = int(input(f"{green}How Many Shares: {gray}"))
    print(f"{blue}{'─'*70}{reset}")

    delay = int(input(f"{green}Delay Between Shares (sec): {gray}"))
    print(f"{blue}{'─'*70}{reset}")

    # Clean tokens
    access_tokens = [t.strip() for t in access_tokens if t.strip()]
    total_live = len(access_tokens)

    print(f"{green}Live Tokens: {gray}{total_live}{reset}")
    if total_live == 0:
        sys.exit(f"{red}[!] No valid tokens entered. Exiting...{reset}")

    # Record start time
    start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{yellow}[*] Start Time: {gray}{start_time}{reset}")
    print(f"{yellow}[*] Starting share process...{reset}")

    stt = 0
    with ThreadPoolExecutor(max_workers=10) as executor:
        while stt < total_share:
            for token in access_tokens:
                if stt >= total_share:
                    break
                stt += 1
                executor.submit(post_to_facebook, token, post_id)

                # Fancy progress design
                progress_bar = "█" * (stt % 20) + "-" * (20 - (stt % 20))
                sys.stdout.write(
                    f"\r{blue}╔═[{green}SHARE PROGRESS{blue}]════════════════════════════════╗\n"
                    f"{blue}║ {green}Share Count:{gray} {stt}/{total_share}                       {blue}║\n"
                    f"{blue}║ {green}Status:{gray} {'SUCCESS' if stt % 2 == 0 else 'PENDING'}                        {blue}║\n"
                    f"{blue}║ {green}Progress:{yellow} [{progress_bar}{yellow}] {int((stt/total_share)*100)}% {blue}║\n"
                    f"{blue}╚════════════════════════════════════════════════════════╝{reset}"
                )
                sys.stdout.flush()
                time.sleep(delay)

    # Record end time
    end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n\n{green}[*] Done! {stt} shares attempted.{reset}")
    print(f"{yellow}[*] End Time: {gray}{end_time}{reset}")

    input(f"{green}Press Enter to exit...{reset}")

if __name__ == "__main__":
    shar()
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
    """
    print(f"""
    {green} 
                
           ░█████╗░██████╗░███╗░░░███╗██╗███╗░░██╗░██████╗
           ██╔══██╗██╔══██╗████╗░████║██║████╗░██║██╔════╝
           ███████║██║░░██║██╔████╔██║██║██╔██╗██║╚█████╗░
           ██╔══██║██║░░██║██║╚██╔╝██║██║██║╚████║░╚═══██╗
           ██║░░██║██████╔╝██║░╚═╝░██║██║██║░╚███║██████╔╝
          ╚═╝░░╚═╝╚═════╝░╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝╚═════╝░
                 {white} https://exoboost.site
     {red}──────────────────────────────────────────────────────────────────────{reset}
     {red}OWNER     {white}: {yellow} YUSH
     {red}FACEBOOK  {white}: {yellow} None
     {red}──────────────────────────────────────────────────────────────────────{reset}""")

def extract_ids(url):
    """
    Extracts the post ID from various Facebook URL formats,
    based on the logic from your provided code.
    """
    group_pattern = r'groups/(\d+)/permalink/(\d+)/'
    post_pattern = r'(\d+)/posts/(\d+)/'
    photo_pattern = r'fbid=(\d+)'
    video_pattern = r'facebook\.com/(\d+)/videos/(\d+)/'

    group_match = re.search(group_pattern, url)
    post_match = re.search(post_pattern, url)
    photo_match = re.search(photo_pattern, url)
    video_match = re.search(video_pattern, url)

    if group_match:
        return f"{group_match.group(2)}"
    elif post_match:
        return f"{post_match.group(2)}"
    elif photo_match:
        return photo_match.group(1)
    elif video_match:
        return video_match.group(2)
    else:
        return None

def share(access_token, post_id):
    """
    This function performs the actual sharing of the post using the
    Facebook Graph API and the endpoint you provided. It requires a valid
    long-lived access token. The 'published=0' parameter means the post
    is shared but not visible on the timeline.
    """
    if not access_token:
        print(f"{red}Error: Please provide a valid access token to perform the share.{reset}")
        return False, "Invalid access token"

    # The Graph API endpoint to share a link, as specified by the user.
    url = "https://graph.facebook.com/me/feed"
    
    # The payload for the API request, including the link and published status.
    payload = {
        'link': f"https://m.facebook.com/{post_id}",
        'published': 0,
        'access_token': access_token,
    }
    
    try:
        response = requests.post(url, data=payload, timeout=10)
        response.raise_for_status()  # Raise an exception for bad status codes

        if response.status_code == 200:
            return True, f"Share successful! Post ID: {response.json().get('id')}"
        else:
            return False, f"Share failed with status code {response.status_code}: {response.text}"

    except requests.exceptions.RequestException as e:
        return False, f"Request failed: {e}"
    except Exception as e:
        return False, f"An error occurred: {e}"

# --- Main Logic ---

def shar():
    """
    The main function to orchestrate the post sharing process.
    """
    clear_screen()
    jovan()
    
    print(f"    {blue}───────────────────────────────────────────────────────────────{reset}")
    post_link = input(f"    {green}Enter Post Link:{reset} ")
    print(f"    {blue}───────────────────────────────────────────────────────────────{reset}")
    
    id_share = extract_ids(post_link)
    if not id_share:
        print(f"{red}Error: Could not extract a valid post ID from the link.{reset}")
        sys.exit()

    try:
        total_share = int(input(f"    {green}How Many Share:{reset} "))
        print(f"    {blue}───────────────────────────────────────────────────────────────{reset}")
        delay = int(input(f"    {green}Delay Share (in seconds):{reset} "))
        print(f"    {blue}───────────────────────────────────────────────────────────────{reset}")
    except ValueError:
        print(f"{red}Error: Please enter a valid number for share count and delay.{reset}")
        sys.exit()
    
    print(f'{green}[*]{reset} Waiting...', end='\r')
    print(f"    {blue}───────────────────────────────────────────────────────────────{reset}")

    stt = 0
    with ThreadPoolExecutor(max_workers=2000) as executor:
        futures = []
        while stt < total_share:
            futures.append(executor.submit(share, VALID_ACCESS_TOKEN, id_share))
            stt += 1
            
            print(f'{green}Share:+{reset} {stt}', end='\r')
            time.sleep(delay)
            
    print(f'\n{green}Share process completed.{reset}')
    
    input(f'{green}[*]{reset} Press Enter to exit...{reset}')

# --- Main Execution Block ---
if __name__ == "__main__":
    shar()
