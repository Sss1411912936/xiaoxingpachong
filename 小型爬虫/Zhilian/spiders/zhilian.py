# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Zhilian.items import ZhilianItem
from scrapy_redis.spiders import RedisSpider

class ZhilianSpider(RedisSpider):

    # start_urls = ["https://sou.zhaopin.com/?pageSize=60&jl=北京"  + "&kw=python"  + "&kt=3&p=" + str(i) for i in range(int(input("起始：")), int(input("终止：")))]
    # redis_key = "zhilian:start_urls"


    name = 'zhilian'

    allowed_domains = ['zhaopin.com']


    # rules = (
    #     Rule(LinkExtractor(allow=r'p=\d+'), callback='parse_item', follow=True),
    # )
    def parse(self, response):
        # print(response)
        job_list = response.xpath("//div[@id='listContent']/div")
        # print(job_list)
        for job in job_list:
            item = ZhilianItem()
            item["name"] = job.xpath(".//div[contains(@class,'jobName')]//a/span/@title").extract_first()
            item["salary"] = job.xpath(".//p[contains(@class,'job__saray')]/text()").extract_first()
            item["fuli"] = job.xpath(".//div[contains(@class,'welfare')]/text()").extract()
            item["address"] = job.xpath(".//li[contains(@class,'demand')][1]/text()").extract_first()
            item["jingyan"] = job.xpath(".//li[contains(@class,'demand')][2]/text()").extract_first()
            item["company"] = job.xpath(".//a[contains(@class,'cname__title')][1]/text()").extract_first()

            next_url = job.xpath(".//div[contains(@class,'jobName')]//a/@href").extract_first()

            # yield item

            yield scrapy.Request(url=next_url,callback=self.parse_next,meta={"item":item})

    def parse_next(self,response):
        item = response.meta["item"]
        item["job_info"] = r"\n".join(response.xpath("//div[@class='pos-ul']/p").extract())
        item["company_info"] = r"\n".join(response.xpath("//div[@class='intro-content']/p/text()").extract())

        yield item
