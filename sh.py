import requests
from bs4 import BeautifulSoup
import time

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; Mobile) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36'
}

def get_fb_tokens(cookies):
    """Fetch fb_dtsg and jazoest tokens needed to post/share"""
    url = 'https://m.facebook.com/'
    resp = requests.get(url, cookies=cookies, headers=HEADERS)
    if not resp.ok:
        return None, None
    soup = BeautifulSoup(resp.text, 'html.parser')
    fb_dtsg = soup.find('input', {'name':'fb_dtsg'})
    jazoest = soup.find('input', {'name':'jazoest'})
    if fb_dtsg and jazoest:
        return fb_dtsg['value'], jazoest['value']
    return None, None

def share_post(post_id, cookies):
    fb_dtsg, jazoest = get_fb_tokens(cookies)
    if not fb_dtsg:
        print("❌ Failed to get fb_dtsg token, maybe cookies invalid.")
        return

    share_url = f'https://m.facebook.com/a/sharer.php?u=https://m.facebook.com/{post_id}'
    data = {
        'fb_dtsg': fb_dtsg,
        'jazoest': jazoest,
        'share': 'Share'
    }

    resp = requests.post(share_url, data=data, cookies=cookies, headers=HEADERS)
    if resp.ok:
        print(f"✅ Shared post {post_id} successfully!")
    else:
        print(f"❌ Failed to share post: status code {resp.status_code}")

if __name__ == '__main__':
    cookie_string = input("Paste full Facebook cookie string: ").strip()
    # Convert to dict
    cookies = {}
    for part in cookie_string.split(';'):
        if '=' in part:
            name, value = part.strip().split('=', 1)
            cookies[name] = value

    post_id = input("Enter Facebook post ID to share: ").strip()
    times = int(input("Number of times to share: "))
    delay = float(input("Delay between shares (seconds): "))

    for i in range(times):
        share_post(post_id, cookies)
        time.sleep(delay)

    print("\nAll done sharing!")
