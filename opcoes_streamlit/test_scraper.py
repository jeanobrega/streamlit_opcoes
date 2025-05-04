from scraper import ScraperModel
from datetime import datetime as dt
import pandas as pd
scraper = ScraperModel()
data=scraper.scrape_advfn_hist('BOVA11',frequency='DAILY',resolution='1Y')

print(data['data'].index[-1])




