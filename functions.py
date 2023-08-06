import requests

from time import sleep
from bs4 import BeautifulSoup, NavigableString
from options import (
    CMC_URL, 
    PAGE_START, 
    PAGE_END, 
    DELAY, 
    MAX_COINS, 
    BLACKLISTED_URLS,
    EMAIL_REGEX
)

def start_contains(text: str, compare: list[str]) -> bool:
    for x in compare:
        if text.startswith(x):
            return True
    return False

def scrape_cmc_coin_urls(page: int) -> list:
    print(f"> Scraping coin list: {CMC_URL.format(page)}")

    req = requests.get(CMC_URL.format(page))
    soup = BeautifulSoup(req.content, 'lxml')
    tables = soup.select('table td:nth-child(3) a.cmc-link')

    return ["https://coinmarketcap.com" + x['href'] for x in tables]

def scrape_website_url_from_cmc_page(url: str) -> str | None:
    print(f"> Scraping CMC currency url: {url}")

    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'lxml')
    link_el = soup.select_one('[rel="nofollow noopener"]')

    return link_el['href'] if link_el else None

def scrape_cmc_pages() -> list[str]:
    website_urls = []
    for i in range(PAGE_START, PAGE_END + 1):
        for i, cmc_page_url in enumerate(scrape_cmc_coin_urls(i)):
            website_url = scrape_website_url_from_cmc_page(cmc_page_url)
            sleep(DELAY)

            if i > MAX_COINS:
                return website_urls

            if (
                website_url 
                and not start_contains(website_url, BLACKLISTED_URLS) 
                and not website_url.endswith('.pdf')
            ):
                website_urls.append(website_url)

    return website_urls

# =======================================
def scrape_email_from_html(soup: BeautifulSoup) -> str:
    mailto_els = soup.find_all('a', href=True)
    mailto_hrefs = [x['href'] for x in mailto_els if x['href'].startswith('mailto')]
    text_email_el = soup.find(text=EMAIL_REGEX)

    email_text = ''
    mailto_text = ''

    if text_email_el:
        if isinstance(text_email_el, NavigableString):
            email_text = str(text_email_el).strip()
        else:
            email_text = text_email_el.text.strip()
    if len(mailto_hrefs) > 0:
        mailto_text = mailto_hrefs[0].replace('mailto:', '').strip()

    email = ''
    if email_text == mailto_text:
        email = email_text
    else:
        email = '; '.join([email_text, mailto_text])

    return email if len(email) < 64 else ''

def scrape_telegram_from_html(soup: BeautifulSoup) -> str:
    telegram_els = soup.find_all('a', href=True)
    telegram_hrefs = [x['href'] for x in telegram_els if x['href'].startswith('https://t.me')]

    if len(telegram_hrefs) > 0:
        return telegram_hrefs[0]
    return ''
