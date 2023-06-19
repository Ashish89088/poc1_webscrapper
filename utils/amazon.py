from bs4 import BeautifulSoup
import requests

def amazonDataScrapper(prod_type, prod_count) :
    def get_title_amazon(soup) :
        try :
            # Outer Taging Object
            title = soup.find("span", attrs={"id" : "productTitle"})
            title_value = title.string
            title_string = title_value.strip()
        except AttributeError :
            title_string = "NA"
        return title_string


    def get_price_amazon(soup) :
        try :
            price = soup.find("span", attrs={"class" : "a-price aok-align-center"}).find(
                "span", attrs={"class" : "a-offscreen"}
            ).text.strip()
            if len(price) >= 10 :
                price = "NA"
        except AttributeError :
            try :
                # Trying for some deal price
                price = soup.find("span", attrs={"class" : "a-offscreen"}).string.strip()
                if len(price) >= 10 :
                    price = "NA"
            except :
                price = "NA"
        return price


    def get_rating_amazon(soup) :
        try :
            rating = soup.find("i", attrs={"class" : "a-icon a-icon-star a-star-4-5"}).string.strip()
        except AttributeError :
            try :
                rating = soup.find("span", attrs={"class" : "a-icon-alt"}).string.strip()
            except :
                rating = "NA"
        return rating


    def get_review_count_amazon(soup) :
        try :
            review_count = soup.find("span", attrs={"id" : "acrCustomerReviewText"}).string.strip()
        except AttributeError :
            review_count = "NA"
        return review_count


    def get_availability_amazon(soup) :
        try :
            available = soup.find("div", attrs={"id" : "availability"})
            available = available.find("span").string.strip()
        except AttributeError :
            available = "NA"
        return available
    
    # Code calling begins here......
    headers = {
        'User-Agent' : 'http://127.0.0.1:5000',
        'Accept-Language' : 'en-US'
    }
    url = f"https://www.amazon.com/s?k={prod_type}"
    webpage = requests.get(url, headers=headers)

    soup = BeautifulSoup(webpage.content, "lxml")

    links = soup.find_all("a", attrs={"class" : "a-link-normal s-no-outline"})
    links_list = []
    for link in links :
        links_list.append(link.get("href"))

    product_details_amazon = []

    for link in links_list[:prod_count] :
        new_webpage = requests.get("https://www.amazon.com" + link, headers=headers)
        new_soup = BeautifulSoup(new_webpage.content, "lxml")

        title = get_title_amazon(new_soup)
        price = get_price_amazon(new_soup)
        rating = get_rating_amazon(new_soup)
        review_count = get_review_count_amazon(new_soup)
        availability = get_availability_amazon(new_soup)

        product_details_amazon.append({
            "title" : title,
            "price" : price,
            "rating" : rating,
            "review_count" : review_count,
            "availability" : availability,
        })
        
    return product_details_amazon