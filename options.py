import re

VERSION = 1

DELAY = 5
PAGE_START = 21
PAGE_END = 21
MAX_COINS = 101
THREAD_COUNT = 2

CMC_URL = "https://coinmarketcap.com/?page={}"
EMAIL_REGEX = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')

BLACKLISTED_URLS = [
    'https://bscscan.com/', 
    'https://arbiscan.io/', 
    'https://github.com/',
    'https://drive.google.com/',
    'https://docs.google.com/',
    'https://docsend.com/',
    'https://twitter.com/',
    'https://explorer.chiliz.com/',
    'https://cardanoscan.io/',
    'https://polygonscan.com/',
    'https://www.chiliz.net/',
    'https://discord.com/',
    'https://solana.fm/',
    'https://vechainstats.com/',
    'https://snowtrace.io/',
    'https://scope.klaytn.com/',
    'https://tronscan.org/',
    'https://tracemove.io/',
    'https://t.me/',
    'https://wavesexplorer.com/',
    'https://firebasestorage.googleapis.com/'
]