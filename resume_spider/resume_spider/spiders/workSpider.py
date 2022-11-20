import pdfkit
import scrapy
import os.path


class WebSpider(scrapy.Spider):
    name = 'work_spider'
    start_urls = ['https://www.work.ua/resumes/?page=1']

    def parse(self, response):
        for link in response.css('div.resume-link a::attr(href)'):
            yield response.follow(link, callback=self.parse_resume)

        for i in range(10):
            next_page = f'https://www.work.ua/resumes/?page={i}/'
            yield response.follow(next_page, callback=self.parse)

    def parse_resume(self, response):
        if response.xpath('//p/span/text()').extract()[1] == "PRO":
            file_name = str(response.css('a.complain::attr(data-rid)').get()) + ".pdf"
            path = "D:\"
            options = {"load-error-handling": "ignore"}
            if not os.path.exists(str(path + file_name + ".pdf")):
                pdfkit.from_url(str(response.url + "/print"), str(path + file_name), options=options)
