from threading import Thread
import json
import chromedriver_autoinstaller

from bs4 import BeautifulSoup
from selenium.webdriver import Chrome, ChromeOptions
from functions import (scrape_cmc_pages, scrape_email_from_html, scrape_telegram_from_html)
from options import (
    PAGE_START, 
    PAGE_END,
    THREAD_COUNT,
    VERSION
)

chromedriver_autoinstaller.install()

options = ChromeOptions()
options.add_argument("lang=en-GB")
options.add_argument("start-maximized")
options.add_argument("--headless")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

DRIVERS = [Chrome(options=options) for _ in range(0, THREAD_COUNT)]
RESULTS = []

def scrape_chunk(urls: list[str]):
    threads: list[Thread] = []
    for i, url in enumerate(urls):
        thread = Thread(target=scrape_socials_from_website, args=(DRIVERS[i], url))
        
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

def scrape_socials_from_website(driver: Chrome, url: str) -> dict:
    print(f"> Scraping socials: {url}")

    driver.get(url)
    socials = {'website': url, 'email': '', 'telegram': ''}
    
    soup = BeautifulSoup(driver.page_source, 'lxml')
    
    try:
        socials['email'] = scrape_email_from_html(soup)
        socials['telegram'] = scrape_telegram_from_html(soup)
    except Exception as e:
        print(f'Erorr while scraping data: {e}')

    RESULTS.append(socials)

print('=' * 32)
print(f'Promo Socials Scraper (v{VERSION})')
print('=' * 32)

website_urls = scrape_cmc_pages()
for i in range(0, len(website_urls), THREAD_COUNT):
    scrape_chunk(website_urls[i:i + THREAD_COUNT])

with open(f'data/pages-{PAGE_START}-{PAGE_END}.json', 'w', encoding='utf-8') as f:
    json.dump(RESULTS, f, indent=3)

print('=' * 16)
print('> DONE')
print('=' * 16)