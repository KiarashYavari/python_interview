# I/O-bound tasks are operations where the program spends
# a lot of time waiting for input/output operations to complete,
# such as reading from or writing to a file, network communication,
# or database queries.

# In this example, we'll use the requests library to download 
# multiple web pages concurrently using threads. 
# This simulates an I/O-bound task since the program will spend
# a significant amount of time waiting for the network responses.

import threading
import requests
import time

# List of URLs to download
urls = [
    "https://www.pcmag.com/news",
    "https://www.computerworld.com/news/",
    "https://www.technewsworld.com/",
    "https://www.computerweekly.com/resources/Business-intelligence-software",
    "https://www.wired.com/"
]

def download_url(url):
    print(f"Starting download: {url}")
    response = requests.get(url)
    print(f"Finished download: {url} with status code {response.status_code}")

if __name__ == "__main__":
    threads = []

    start_time = time.time()

    # Create and start a thread for each URL
    for url in urls:
        thread = threading.Thread(target=download_url, args=(url,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f"All downloads completed in {end_time - start_time} seconds")
