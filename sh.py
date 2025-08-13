import requests
import uuid
import random
import time

def random_fb_user_agent():
    fbav = f"{random.randint(49, 66)}.0.0.{random.randrange(20, 49)}{random.randint(11, 99)}"
    fbbv = str(random.randint(11111111, 77777777))
    fbrv = str(random.randint(1000000, 9999999))
    ua = (f"[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};"
          f"FBDM/{{density=3.0,width=1080,height=2107}};"
          f"FBLC/fr_FR;FBRV/{fbrv};FBCR/Ooredoo TN;"
          f"FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;"
          f"FBDV/MAR-LX1M;FBSV/9;FBOP/1;FBCA/arm64-v8a:]")
    return ua

def get_fb_access_token(email, password):
    accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'  # Facebook app token
    
    data = {
        'adid': str(uuid.uuid4()),
        'format': 'json',
        'device_id': str(uuid.uuid4()),
        'cpl': 'true',
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
        'Host': 'graph.facebook.com',
    }
    
    url = "https://b-graph.facebook.com/auth/login"
    
    try:
        response = requests.post(url, data=data, headers=headers, allow_redirects=False)
    except Exception as e:
        print(f"Request error: {e}")
        return None

    if response.status_code == 200:
        try:
            result = response.json()
        except Exception as e:
            print(f"JSON decode error: {e}")
            print("Raw response:", response.text)
            return None
        
        token = result.get('access_token')
        if token:
            print(f"Access token obtained: {token}")
            return token
        else:
            print("Login failed or access token not found.")
            print("Response:", result)
    else:
        print(f"HTTP error {response.status_code}")
        print("Response:", response.text)

    return None

def share_post(access_token, post_id):
    url = 'https://graph.facebook.com/me/feed'
    params = {
        'link': f'https://m.facebook.com/{post_id}',
        'published': '0',
        'access_token': access_token
    }
    response = requests.post(url, params=params)
    if response.ok:
        print(f"Shared post {post_id} successfully!")
    else:
        print(f"Failed to share post: {response.text}")

if __name__ == "__main__":
    print("Facebook Login + Share Script\n")

    email = input("Enter Facebook email/username: ").strip()
    password = input("Enter Facebook password: ").strip()

    print("\nLogging in...")
    token = get_fb_access_token(email, password)
    if not token:
        print("Could not retrieve access token. Exiting.")
        exit(1)

    post_id = input("\nEnter the Facebook post ID to share: ").strip()
    times = int(input("How many times to share? "))
    delay = float(input("Delay between shares (seconds): "))

    for i in range(times):
        share_post(token, post_id)
        time.sleep(delay)

    print("\nDone sharing!")
