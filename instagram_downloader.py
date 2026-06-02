from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import selenium.common.exceptions
import time
from bs4 import BeautifulSoup as bs
import requests
import os
from dotenv import load_dotenv  # ✅ for .env file

# --- Load environment variables ---
load_dotenv()
username = os.getenv("INSTAGRAM_USERNAME")
password = os.getenv("INSTAGRAM_PASSWORD")
target_user = os.getenv("TARGET_USER")

url = f'https://www.instagram.com/{target_user}/'

# Track downloaded links
downloaded_links = set()

def start_browser():
    global chrome
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    chrome = webdriver.Chrome(options=options)

def open_url():
    chrome.get("https://www.instagram.com/")
    time.sleep(4)

def login(username, your_password):
    usern = chrome.find_element(By.NAME, "username")
    usern.send_keys(username)
    passw = chrome.find_element(By.NAME, "password")
    passw.send_keys(your_password)
    passw.send_keys(Keys.RETURN)
    time.sleep(5)

    try:
        notn = chrome.find_element(By.XPATH, "//button[contains(text(),'Not Now')]")
        notn.click()
        time.sleep(2)
    except selenium.common.exceptions.NoSuchElementException:
        pass

    chrome.get(url)
    time.sleep(4)

def download_images():
    user_name = url.rstrip("/").split("/")[-1]
    if not os.path.isdir(user_name):
        os.mkdir(user_name)

    last_height = chrome.execute_script("return document.body.scrollHeight")
    count = 1

    while True:
        html = chrome.page_source
        soup = bs(html, "html.parser")

        # ✅ Post containers with images
        post_divs = soup.find_all("div", {"class": "_aagv"})  # grid images

        for div in post_divs:
            img_tag = div.find("img")
            if not img_tag:
                continue

            img_url = img_tag.get("src")

            # Skip duplicates
            if not img_url or img_url in downloaded_links:
                continue

            try:
                response = requests.get(img_url, timeout=10)
                img_path = os.path.join(user_name, f"content{count}.jpg")
                with open(img_path, "wb") as f:
                    f.write(response.content)
                print(f"✅ Saved: {img_path}")
                downloaded_links.add(img_url)
                count += 1
            except Exception as e:
                print(f"⚠️ Error saving image: {e}")

        # Scroll down
        chrome.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

        new_height = chrome.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    print("🎉 Finished downloading user’s uploaded images.")

# --- Driver Code ---
if __name__ == "__main__":
    start_browser()
    open_url()
    login(username, password)
    download_images()
    chrome.close()
