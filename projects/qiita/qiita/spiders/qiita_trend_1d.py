import scrapy


class QiitaTrend1dSpider(scrapy.Spider):
    name = 'qiita_trend_1d'
    allowed_domains = ['qiita.com']
    start_urls = ['https://qiita.com/']

    def parse(self, response):
        category = response.xpath('//a[@class="st-NewHeader_mainNavigationItem is-active"]/text()').get()
        titles = response.xpath('//h2/a/text()').getall()
        urls = response.xpath('//h2/a/@href').getall()
        
        yield {
            'category': category,
            'titles': titles,
            'urls': urls
        }