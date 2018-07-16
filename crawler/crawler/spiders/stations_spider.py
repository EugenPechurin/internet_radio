from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
import re
from urllib.parse import urljoin
from crawler.items import StationItem, GenreItem


def parse_url(raw):
    return re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', raw)


class AbiturSpider(CrawlSpider):
    name = "stations_list"
    allowed_domains = ["www.internet-radio.com"]
    start_urls = ["http://www.internet-radio.com"]
    rules = [Rule(LinkExtractor(allow=r'https://www.internet-radio.com/stations/\w+/'), callback='parse_item')]
    visited_urls = []
    res = {}

    def parse_item(self, response):
        selector = Selector(response)
        if response.url not in self.visited_urls:
            self.visited_urls.append(response.url)
        stations_html = selector.xpath('/html/body/div[1]/div[1]/div[1]/table/tbody/tr')
        for station in stations_html:
            title = station.xpath('.//td/h4/a/text()').extract()
            pls_raw = station.xpath('.//td/small/a[@title="PLS Playlist File"]/@href').extract()
            pls = urljoin(response.url, pls_raw[0])
            m3u_raw = station.xpath('.//td/small/a[@title="M3U Playlist File"]/@href').extract()
            m3u = urljoin(response.url, m3u_raw[0])
            url_station_raw = station.xpath('.//td/h4/a/@href').extract()
            url_station = urljoin(response.url, url_station_raw[0])
            bit_rate = station.xpath('.//td/p/text()').extract()
            genres = station.xpath('.//td[3]/a').extract()
            # for genre in genres:
            #     print(genre)
            #     print(GenreItem.objects.get(title=genre))
            if title:
                station_data = {
                    'title': title[0],
                    'pls': pls or '',
                    'm3u': m3u or '',
                    'url_station': url_station or '',
                    'bit_rate': bit_rate[1].strip() or '',
                }

                return StationItem(station_data)
