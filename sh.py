import requests
import sys
import time
from concurrent.futures import ThreadPoolExecutor

# Fixed access token you provided
ACCESS_TOKEN = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'

def share(cookie, post_id):
    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate',
        'connection': 'keep-alive',
        'content-length': '0',
        'cookie': cookie,
        'host': 'graph.facebook.com',
        # You can add a user-agent header if you want:
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }
    try:
        url = f'https://graph.facebook.com/me/feed?link=https://m.facebook.com/{post_id}&published=0&access_token={ACCESS_TOKEN}'
        response = requests.post(url, headers=headers)
        # Optional: check response here if you want
        # print(response.json())
    except Exception as e:
        print(f"Error sharing post: {e}")

def clear_screen():
    # Clear terminal screen (works on Windows and Unix)
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def shar():
    green = '\x1b[38;2;0;255;0m'   # green color code
    blue = '\x1b[38;2;0;128;255m'   # blue color code

    clear_screen()
    # Your jovan() function not provided, so commenting out
    # jovan()

    input_cookies = input(f"     {green}Enter Cookie(s) separated by comma: \x1b[0m").split(',')
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    post_id = input(f"     {green}Enter Post ID: \x1b[0m")
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    total_share = int(input(f"    {green}How Many Shares: \x1b[0m"))
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    delay = float(input(f"    {green}Delay between shares (seconds): \x1b[0m"))
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    
    total_cookies = len(input_cookies)
    print(f'\x1b[38;2;173;255;47m[*] Number of cookies entered: \x1b[0m{total_cookies}')
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")

    if total_cookies == 0:
        print("No cookies provided. Exiting.")
        sys.exit()

    stt = 0

    with ThreadPoolExecutor(max_workers=50) as executor:
        futures = []
        while stt < total_share:
            for cookie in input_cookies:
                if stt >= total_share:
                    break
                futures.append(executor.submit(share, cookie.strip(), post_id))
                stt += 1
                print(f'\x1b[38;2;173;255;47mShares done: \x1b[0m{stt}', end='\r')
                time.sleep(delay)
            if stt >= total_share:
                break

    input('\n\x1b[38;2;173;255;47m[*] Press Enter to exit...\x1b[0m')

if __name__ == '__main__':
    shar()
