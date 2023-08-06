# CMC - Project Scrapper

This script gets a coin's website URL on CoinMarketCap and scrapes it's socials. (Email, Telegram) 

## Options

- Delay = Time between each coin market cap page request. <b>Lowering this may get you blocked<b>
- Thread count = Essentially how many websites to load at the same time, because some websites need some time to load. <b>If your internet speed is slow, keep the value at 1 or 2<b>
- Max coins = How many coins to scrape per page.
- Blacklisted urls = On some pages, the website url of a coin is a third-party site where the needed info is not on there, so we ignore them.
- Page start/end are self-explanatory.