import requests
import time

# Replace with your valid Facebook access token
ACCESS_TOKEN = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'

def share_post(post_id):
    url = 'https://graph.facebook.com/me/feed'
    params = {
        'link': f'https://m.facebook.com/{post_id}',
        'published': '0',
        'access_token': ACCESS_TOKEN
    }
    resp = requests.post(url, params=params)
    if resp.ok:
        print(f"Shared post {post_id} successfully!")
    else:
        print(f"Failed to share post: {resp.text}")

if __name__ == '__main__':
    post_id = input("Enter Facebook post ID: ").strip()
    times = int(input("How many times to share? "))
    delay = float(input("Delay between shares (seconds): "))

    for i in range(times):
        share_post(post_id)
        time.sleep(delay)

    print("\nDone sharing!")
