import asyncio
from pyppeteer import launch
import requests
import pandas as pd

file = 'Splainer_links_Solr.csv'
dat = pd.read_csv(file)
codes = []

# async def main():
#     browser = await launch()
#     for url in dat["URL"]:
#         page = await browser.newPage()
#         await page.goto(url, {'waitUntil': 'networkidle0'})
#         solr_link = await page.querySelector('div.alert:nth-child(2) > div:nth-child(1) > a:nth-child(1)')
#         content = await page.evaluate('(element) => element.getAttribute("href")', solr_link)
#         r = requests.get(content)
#         code = r.status_code
#         codes.append(code)
#     await browser.close()
#     dat["Code"] = codes
#     dat.to_csv(file, index=False)
#     print(f"{sum([x != 200 for x in codes])} of {len(codes)} of splainer links failed.")

async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('http://splainer.io/#/es_?esUrl=http:%2F%2Flocalhost:9200%2Ftmdb%2F_search&esQuery=%7B%0A%20%20%22query%22:%20%7B%0A%20%20%20%20%20%20%22multi_match%22:%20%7B%0A%20%20%20%20%20%20%20%20%20%20%22query%22:%20%22will%20smith%22,%0A%20%20%20%20%20%20%20%20%20%20%22type%22:%20%22best_fields%22,%0A%20%20%20%20%20%20%20%20%20%20%22fields%22:%20%5B%22title%22,%20%22tagline%22,%20%22overview%22,%20%22cast%22%5D%0A%20%20%20%20%20%20%7D%0A%20%20%20%20%0A%20%20%7D%0A%7D%20%20%20%20%0A&fieldSpec=title%20cast%20directors%20release_date')
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())
