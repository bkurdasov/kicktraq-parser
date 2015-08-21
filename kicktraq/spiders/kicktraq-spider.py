import urlparse
from scrapy.contrib.loader import ItemLoader
from scrapy.http import Request
from kicktraq.items import KicktraqItem
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector


class KicktraqSpider(BaseSpider):
    """my spider """
    name = "kicktraq-spider"
    start_urls = ['http://www.kicktraq.com/archive/']
    allowed_domains = ['kicktraq.com']

    def parse(self, response):
        '''Parse main page and extract sequential page link.'''
        '''
        self.log('Downloaded page.', log.DEBUG)
        if response.meta['depth'] > 5:
            self.log('Categories depth limit reached (recursive links?). Stopping further following.', log.WARNING)
        '''
        hxs = HtmlXPathSelector(response)
        links = hxs.xpath('//div[@class="paging"]//a/@href').extract()
        #print '>>>', links
        for link in links:
            pagelink = urlparse.urljoin('http://www.kicktraq.com/archive/',link)
            #print '>>>',pagelink
            yield Request(pagelink, callback = self.parse)
        itemdivs = hxs.select('//div[@class="projects"]/div/div[@class="project-infobox"]')
        for itemdiv in itemdivs:
            item = KicktraqItem()
            item['project'] = itemdiv.xpath('h2/a/text()').extract()
            item['description'] = itemdiv.xpath('div[not(@class)]/text()').extract()
            item['category'] = itemdiv.xpath('div[@class="project-cat"]/a[1]/text()').extract()
            item['subcategory'] = itemdiv.xpath('div[@class="project-cat"]/a[2]/text()').extract()
            item['status'] = itemdiv.xpath('div[@class="project-infobits"]/div/div/div/h5/text()').extract()
            '''
            item['backers'] = itemdiv.xpath('div[@class="project-infobits"]/div[@class="project-details"]/text()[1]').extract().split(':')[-1].strip()
            item['raised'] = itemdiv.xpath('div[@class="project-infobits"]/div[@class="project-details"]/text()[2]').extract()
            item['goal'] = itemdiv.xpath('div[@class="project-infobits"]/div[@class="project-details"]/text()[2]').extract()
            item['avg_daily_funding'] = '' #itemdiv.xpath('h2/a/text()').extract()
            item['start'] = itemdiv.xpath('div[@class="project-infobits"]/div[@class="project-details"]/text()[3]').extract()
            item['end'] = itemdiv.xpath('div[@class="project-infobits"]/div[@class="project-details"]/text()[3]').extract()
            '''
            yield item