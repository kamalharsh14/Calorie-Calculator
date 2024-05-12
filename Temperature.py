import requests
from selectorlib import Extractor


class Temperature:
    yml_path = 'temperature.yaml'
    base_url = 'https://www.timeanddate.com/weather/'

    def __init__(self, country, city):
        self.country = country
        self.city = city

    def _build_url(self):
        url = self.base_url + self.country + "/" + self.city
        return url

    def _scrape(self):
        url = self._build_url()
        extractor = Extractor.from_yaml_file(self.yml_path)
        response = requests.get(url)
        content = response.text
        raw_extract = extractor.extract(content)
        return raw_extract

    def get(self):
        scraped_content = self._scrape()
        temp = float(scraped_content['temp'].replace("\xa0°C", ""))
        return temp
