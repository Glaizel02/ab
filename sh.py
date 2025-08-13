import requests
import uuid
import random
import time

def random_fb_user_agent():
    fbav = f"{random.randint(49,66)}.0.0.{random.randrange(20,49)}{random.randint(11,99)}"
    fbbv = str(random.randint(11111111,77777777))
    fbrv = str(random.randint(1000000,9999999))
    ua = (f"[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};"
          f"FBDM/{{density=3.0,width=1080,height=2107}};"
          f"FBLC/en_US;FBRV/{fbrv};FBCR/;FBMF/;FBBD/;FBPN/com.facebook.katana;"
          f"FBDV/;FBSV/;FBOP/1;FBCA/arm64-v8a:]")
    return ua

def fetch_access_token(email, password):
    # Correct token with raw pipe character
    accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
    data = {
        'adid': str(uuid.uuid4()),
        'format': 'json',
        'device_id': str(uuid.uuid4()),
        'family_device_id': str(uuid.uuid4()),
        'credentials_type': 'device_based_login_password',
        'email': email,
        'password': password,
        'access_token': accessToken,
        'generate_session_cookies': '1',
        'method': 'auth.login',
    }
    headers = {
        'User-Agent': random_fb_user_agent(),
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'graph.facebook.com'
    }
    url = 'https://b-graph.facebook.com/auth/login'

    try:
        resp = requests.post(url, data=data, headers=headers, allow_redirects=False)
        result = resp.json()
    except Exception as e:
        print(f"Login error: {e}")
        return None

    token = result.get('access_token')
    if token:
        print(f"✅ Access token obtained: {token}")
        return token
    else:
        err = result.get('error', {}).get('message', 'Unknown error')
        print(f"❌ Failed to fetch token: {err}")
        return None

def share_post(access_token, post_id):
    url = 'https://graph.facebook.com/me/feed'
    params = {
        'link': f'https://m.facebook.com/{post_id}',
        'published': '0',
        'access_token': access_token
    }
    try:
        resp = requests.post(url, params=params)
        if resp.ok:
            print(f"✅ Shared post {post_id} successfully!")
        else:
            print(f"❌ Failed to share post: {resp.text}")
    except Exception as e:
        print(f"Share error: {e}")

if __name__ == '__main__':
    print("Facebook Auto Login + Share Script\n")
    email = input("Enter Facebook email: ").strip()
    password = input("Enter Facebook password: ").strip()
    
    token = fetch_access_token(email, password)
    if not token:
        print("Cannot continue without a valid access token. Exiting.")
        exit()

    post_id = input("Enter Facebook post ID to share: ").strip()
    times = int(input("Number of times to share: "))
    delay = float(input("Delay between shares (seconds): "))

    for i in range(times):
        share_post(token, post_id)
        time.sleep(delay)

    print("\nAll done sharing!")
