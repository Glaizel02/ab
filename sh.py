import requests
import time

# Your valid user access token
ACCESS_TOKEN = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; Mobile) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36'
}

def parse_cookies(cookie_string):
    """
    Convert full cookie string into a dictionary
    Example input: 'datr=f-SbaIC_HCy3-ykfT8_Fmndl; c_user=61579086552462; xs=...'
    """
    cookies = {}
    parts = cookie_string.split(';')
    for part in parts:
        if '=' in part:
            name, value = part.strip().split('=', 1)
            cookies[name] = value
    return cookies

def share_post(post_id, cookies):
    url = 'https://graph.facebook.com/me/feed'
    params = {
        'link': f'https://m.facebook.com/{post_id}',
        'published': '0',
        'access_token': ACCESS_TOKEN
    }

    try:
        resp = requests.post(url, params=params, cookies=cookies, headers=HEADERS)
        if resp.ok:
            print(f"✅ Shared post {post_id} successfully!")
        else:
            print(f"❌ Failed to share post: {resp.text}")
    except Exception as e:
        print(f"Share error: {e}")

if __name__ == '__main__':
    cookie_string = input("Enter full Facebook cookie string: ").strip()
    cookies = parse_cookies(cookie_string)

    post_id = input("Enter Facebook post ID to share: ").strip()
    times = int(input("Number of times to share: "))
    delay = float(input("Delay between shares (seconds): "))

    for i in range(times):
        share_post(post_id, cookies)
        time.sleep(delay)

    print("\nAll done sharing!")
