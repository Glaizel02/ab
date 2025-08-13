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
        console.print(Panel(
            """
[green]1. Spam Share
[green]2. Token Getter
[red]3. Exit
            """,
            width=65,
            style="bold bright_white",
        ))
        choice = input("Select an option: ")

        if choice == "1":
            spam_share()
        elif choice == "2":
            token_getter()
        elif choice == "3":
            console.print("[red]Exiting...")
            break
        else:
            console.print("[red]Invalid choice! Try again.")
            time.sleep(2)

def spam_share():
    clear_screen()
    display_banner("SPAM SHARE")
    access_token = input("Enter your access token: ")
    share_url = input("Enter your post link: ")
    try:
        share_count = int(input("Enter Share Count: "))
    except ValueError:
        console.print("[red]Invalid number for share count. Returning to menu.")
        time.sleep(2)
        return
    time_interval = 0.5
    shared_count = 0

    def share_post():
        nonlocal shared_count
        url = f"https://graph.facebook.com/me/feed?access_token={access_token}"
        data = {"link": share_url, "privacy": {"value": "SELF"}, "no_story": "true"}
        headers = {"User-Agent": "Mozilla/5.0"}

        try:
            response = requests.post(url, json=data, headers=headers)
            response_data = response.json()
            post_id = response_data.get("id", "Unknown")
            shared_count += 1
            console.print(f"[green]Post shared: {shared_count}")
            console.print(f"[cyan]Post ID: {post_id}")
        except requests.exceptions.RequestException as e:
            console.print(f"[red]Failed to share post: {e}")

    for _ in range(share_count):
        share_post()
        time.sleep(time_interval)
    console.print("[green]Finished sharing posts.")
    input("\n[bold yellow]Press Enter to return to the main menu...[/bold yellow]")

def token_getter():
    clear_screen()
    display_banner("TOKEN GETTER")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    twofactor_code = input("Enter your 2-factor authentication code (Enter '0' if not applicable): ")

    result = make_request(email, password, twofactor_code)
    console.print(f"\n[bold green]Access Token: {result}[/bold green]")
    input("\n[bold yellow]Press Enter to return to the main menu...[/bold yellow]")

def make_request(email, password, twofactor_code):
    deviceID = str(uuid.uuid4())
    adid = str(uuid.uuid4())
    random_str = ''.join(random.choice(string.ascii_lowercase + "0123456789") for _ in range(24))

    form = {
        'adid': adid,
        'email': email,
        'password': password,
        'format': 'json',
        'device_id': deviceID,
        'locale': 'en_US',
        'api_key': '882a8490361da98702bf97a021ddc14d',
        'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
    }
    try:
        form['sig'] = hashlib.md5(("".join(f"{k}={form[k]}" for k in sorted(form)) + '62f8ce9f74b12f84c123cc23437a4a32').encode()).hexdigest()
        headers = { 'content-type': 'application/x-www-form-urlencoded' }
        url = 'https://b-graph.facebook.com/auth/login'

        response = requests.post(url, data=form, headers=headers)
        response_json = response.json()
        return response_json.get("access_token", "Failed to retrieve access token")
    except Exception:
        return "Error: Please check your account and password again!"

if __name__ == '__main__':
    main_menu()
