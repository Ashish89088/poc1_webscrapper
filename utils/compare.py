from utils.flipkart import flipkartDataScrapper
from utils.amazon import amazonDataScrapper

def compareDataScrapper(product_type, count) :
    amazonData = amazonDataScrapper(product_type, count)
    flipkartData = flipkartDataScrapper(product_type, count)
    return amazonData + flipkartData
    