import requests
import time

# Your valid user access token
ACCESS_TOKEN = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; Mobile) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36'
}

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
    # Ask user to enter cookies
    print("Enter your Facebook cookies:")
    c_user = input("c_user: ").strip()
    datr = input("datr: ").strip()
    xs = input("xs: ").strip()

    COOKIES = {
        'c_user': c_user,
        'datr': datr,
        'xs': xs
    }

    post_id = input("Enter Facebook post ID to share: ").strip()
    times = int(input("Number of times to share: "))
    delay = float(input("Delay between shares (seconds): "))

    for i in range(times):
        share_post(post_id, COOKIES)
        time.sleep(delay)

    print("\nAll done sharing!")
