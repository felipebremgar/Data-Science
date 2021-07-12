import scrapy


class WhiskeySpider(scrapy.Spider):
    name = 'whisky'
    allowed_domains = ['www.whiskyshop.com']
    start_urls = ['https://www.whiskyshop.com/scotch-whisky']
    
    def parse(self, response):
        for products in response.css('div.product-item-info'):
            try:
                yield {
                    'Nome': products.css('a.product-item-link::text').get(),
                    'Preço': products.css('span.price::text').get().replace('£', ''),
                    'Link': products.css('a.product-item-link').attrib['href'],
                }

            except:
                yield {
                    'Nome': products.css('a.product-item-link::text').get(),
                    'Preço': 'sold out',
                    'Link': products.css('a.product-item-link').attrib['href'],
                }

        next_page = response.css('a.action.next').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)