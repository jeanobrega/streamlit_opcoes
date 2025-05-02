# scraper.py
from urllib.request import Request,urlopen
import json
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup
class ScraperModel:
    def scrape_data(self, url, tag, class_name=None):
        try:
            html = urlopen(url)
        except HTTPError as e:
            return f"Erro HTTP: {e}"
        except URLError as e:
            return f"Erro de URL: {e}"
        except Exception as e:
            return f"Ocorreu um erro: {e}"

        try:
            soup = BeautifulSoup(html, 'html.parser')
            if class_name:
                elements = soup.find_all(tag, class_=class_name)
            else:
                elements = soup.find_all(tag)
            return [element.get_text(strip=True) for element in elements]
        except Exception as e:
            return f"Erro ao analisar o HTML: {e}"

    def scrape_json(self,url):
        try:
            req=Request(url,headers={'User-Agent': 'Mozilla'})
            with urlopen(req) as response:
                data = response.read()
                json_data = json.loads(data.decode('utf-8'))
            return json_data
        except Exception as e:
            return f"Erro ao obter dados: {e}"
        #return "scrape_json em construção! "
