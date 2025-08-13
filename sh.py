import os
import time
import yaml
from termcolor import colored
from prettytable import PrettyTable
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

ACCOUNTS_FILE = "accounts.txt"
COOKIES_DIR = "cookies"
WAIT_TIME = 3

os.makedirs(COOKIES_DIR, exist_ok=True)

def save_cookies(driver, uid):
    cookies = driver.get_cookies()
    with open(os.path.join(COOKIES_DIR, f"{uid}.yml"), "w") as f:
        yaml.safe_dump(cookies, f)

def load_cookies(driver, uid):
    cookie_file = os.path.join(COOKIES_DIR, f"{uid}.yml")
    if not os.path.exists(cookie_file):
        return False
    with open(cookie_file, "r") as f:
        cookies = yaml.safe_load(f)
    for cookie in cookies:
        driver.add_cookie(cookie)
    return True

def log_status(uid, message, status_type="info"):
    if status_type == "success":
        print(colored("[SUCCESS]", "green"), uid, "-", message)
    elif status_type == "fail":
        print(colored("[FAILED]", "red"), uid, "-", message)
    else:
        print(colored("[INFO]", "cyan"), uid, "-", message)

def perform_action(account, action, target, quantity):
    uid, password = account.split("|")

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://www.facebook.com")
        logged_in = load_cookies(driver, uid)
        driver.get("https://www.facebook.com")
        time.sleep(WAIT_TIME / 2)

        if not logged_in:
            driver.get("https://www.facebook.com/login")
            time.sleep(WAIT_TIME)
            try:
                driver.find_element(By.ID, "email").send_keys(uid)
                driver.find_element(By.ID, "pass").send_keys(password)
                driver.find_element(By.NAME, "login").click()
            except:
                log_status(uid, "Login page elements not found", "fail")
                return
            time.sleep(WAIT_TIME * 2)

            page_source = driver.page_source.lower()
            current_url = driver.current_url.lower()

            if "checkpoint" in current_url:
                if "enter code" in page_source or "confirmation code" in page_source:
                    log_status(uid, "2FA required", "fail")
                else:
                    log_status(uid, "Checkpoint verification", "fail")
                return
            elif "disabled" in page_source or "account has been disabled" in page_source:
                log_status(uid, "Account disabled", "fail")
                return
            elif "incorrect" in page_source or "invalid" in page_source:
                log_status(uid, "Wrong credentials", "fail")
                return
            else:
                try:
                    driver.find_element(By.CSS_SELECTOR, '[aria-label="Facebook"]')
                    log_status(uid, "Login success", "success")
                    save_cookies(driver, uid)
                except:
                    log_status(uid, "Login verification failed", "fail")
                    return
        else:
            log_status(uid, "Logged in using cookies", "success")

        table = PrettyTable(["#", "Action", "Status"])
        for i in range(quantity):
            time.sleep(1)
            try:
                if action == "share":
                    driver.get(target)
                    time.sleep(WAIT_TIME)
                    driver.find_element(By.XPATH, "//span[contains(text(), 'Share')]").click()
                    time.sleep(WAIT_TIME / 2)
                    driver.find_element(By.XPATH, "//span[contains(text(), 'Share Now')]").click()
                    table.add_row([i+1, "Share", "✅"])
                elif action == "react":
                    driver.get(target)
                    time.sleep(WAIT_TIME)
                    driver.find_element(By.XPATH, "//span[contains(text(), 'Like')]").click()
                    table.add_row([i+1, "React", "✅"])
                elif action == "follow":
                    driver.get(target)
                    time.sleep(WAIT_TIME)
                    driver.find_element(By.XPATH, "//div[contains(text(), 'Follow')]").click()
                    table.add_row([i+1, "Follow", "✅"])
                elif action == "comment":
                    driver.get(target)
                    time.sleep(WAIT_TIME)
                    driver.find_element(By.XPATH, "//span[contains(text(), 'Comment')]").click()
                    time.sleep(WAIT_TIME / 2)
                    comment_field = driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Write a comment"]')
                    comment_field.send_keys(f"Boosted! 🔥 {i+1}")
                    comment_field.send_keys(u'\ue007')  # Enter key
                    table.add_row([i+1, "Comment", "✅"])
            except Exception as e:
                table.add_row([i+1, action.capitalize(), f"❌ {e}"])

        print(table)

    except Exception as e:
        log_status(uid, f"Error: {e}", "fail")
    finally:
        driver.quit()

# Load accounts
try:
    with open(ACCOUNTS_FILE, "r") as f:
        accounts = [line.strip() for line in f if line.strip()]
    if not accounts:
        print(colored("Error: accounts.txt is empty", "red"))
        exit()
except FileNotFoundError:
    print(colored(f"Error: {ACCOUNTS_FILE} not found", "red"))
    print(colored("Create it with uid|pass per line", "yellow"))
    exit()

# Example usage
# perform_action("email@example.com|password123", "share", "https://facebook.com/postlink", 2)
