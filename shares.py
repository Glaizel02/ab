import os
import sys
import time
import requests
import re
from concurrent.futures import ThreadPoolExecutor

# --- API and Access Token Keys ---
# App ID and Secret Key from your provided token.
APP_ID = "350685531728"
API_KEY = "62f8ce9f74b12f84c123cc23437a4a32"

# A valid access token for sharing is typically a combination of these.
# For sharing on a user's behalf, a User Access Token is often required,
# but this script now uses the App Access Token you provided.
VALID_ACCESS_TOKEN = f"{APP_ID}|{API_KEY}"

# --- Color Codes from your file ---
green = "\033[1;32m"
blue = "\033[1;34m"
red = "\033[1;31m"
yellow = "\033[1;33m"
white = "\033[1;37m"
reset = "\033[0m"

# --- Helper Functions from your trial.py file ---

def clear_screen():
    """
    Clears the console screen, checking for different operating systems.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def jovan():
    """
    This function prints the elaborate banner from your provided code.
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
