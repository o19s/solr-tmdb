import asyncio
from pyppeteer import launch
import requests
import pandas as pd

file = 'splainer_links_solr.csv'
dat = pd.read_csv(file)
codes = []

async def main():
    browser = await launch()
    for url in dat["URL"]:
        page = await browser.newPage()
        await page.goto(url, {'waitUntil': 'networkidle0'})
        solr_link = await page.querySelector('div.alert:nth-child(2) > div:nth-child(1) > a:nth-child(1)')
        content = await page.evaluate('(element) => element.getAttribute("href")', solr_link)
        r = requests.get(content)
        code = r.status_code
        codes.append(code)
    await browser.close()
    dat["Code"] = codes
    dat.to_csv(file, index=False)
    print(f"{sum([x != 200 for x in codes])} of {len(codes)} of splainer links failed.")


asyncio.get_event_loop().run_until_complete(main())
