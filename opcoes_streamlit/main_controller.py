#main_controller.py
from scraper import ScraperModel

class MainController:
    def __init__(self):
        self.model = ScraperModel()

    def scrape_and_display(self, url, tag, class_name):
        data = self.model.scrape_data(url, tag, class_name)
        return data
    
    def scrape_json(self,url):
        data = self.model.scrape_json(url)
        return data
    
    def scrape_advfn_hist(self,symbol,frequency='DAILY',resolution='1Y'):
        data = self.model.scrape_advfn_hist(symbol,frequency,resolution)
        return data