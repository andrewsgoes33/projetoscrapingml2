import scrapy


class MercadolivreSpider(scrapy.Spider):
    name = "mercadolivre"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/notebooks"]

    def parse(self, response):
        
        products = response.css('div.poly-card__content')
        
        for product in products:
            
            prices = product.css('span.andes-money-amount__fraction::text').getall()
            
            yield {'brand' : product.css('span.poly-component__brand::text').get(),
                   'name' : product.css('h2.poly-box.poly-component__title a::text').get(),
                   'seller' : product.css('span.poly-component__seller::text').get(),
                   'old_price' : prices[0] if len(prices) > 0 else None,
                   'new_price' : prices[1] if len(prices) > 0 else None,
                   'reviews_rating' : product.css('span.poly-reviews__rating::text').get(),
                   'reviews_total' : product.css('span.poly-reviews__total::text').get()
            
            }
        