from pages.base import WebPage
from pages.elements import WebElement, ManyWebElements
import os


class MainPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.ozon.ru/'

        super().__init__(web_driver, url)

    h1 = WebElement(xpath='//h1')

    h2 = WebElement(xpath='//h2')

    first_element_in_location = WebElement(xpath="//ul[@class='a6']/li[1]")

    location = WebElement(xpath="//button[@class='_1-6r']")

    location_input = WebElement(xpath="//input[@class='_16XE _2HHF']")

    top_fashion = WebElement(xpath="//ul[@class='c6c9']/li[1]")

    premium = WebElement(xpath="//ul[@class='c6c9']/li[2]")

    ozon_card = WebElement(xpath="//ul[@class='c6c9']/li[3]")

    live = WebElement(xpath='//a[@href="/live/"]')

    sale = WebElement(xpath='//a[@href="/info/actions/"]')

    brands = WebElement(xpath='//a[@href="/brand/"]')

    seller = WebElement(xpath="//a[@href='/seller/']")

    certificates_menu = WebElement(xpath='//a[@href="/context/detail/id/135382627/?perehod=menu"]')

    electronics = WebElement(xpath="//ul[@class='c6c9']/li[9]")

    main_apparel = WebElement(xpath='//a[@href="/info/main-apparel/"]')

    for_kids = WebElement(xpath="//ul[@class='c6c9']/li[11]")

    garden = WebElement(xpath="//ul[@class='c6c9']/li[12]")

    business = WebElement(xpath='//a[@href="/business/?perehod=header"]')

    appspromo = WebElement(xpath='//a[@href="/info/appspromo/"]')

    referral = WebElement(xpath='//a[@href="/referral/?perehod=header"]')

    make_money_with_us = WebElement(xpath='//a[@href="//business.ozon.ru/?perehod=header"]')

    certificates_header = WebElement(xpath='//a[@href="/context/detail/id/135382627/?perehod=header"]')

    desks_map = WebElement(xpath='//a[@href="/info/map/"]')

    postamat = WebElement(xpath='//a[@href="/postamat/"]')

    help = WebElement(xpath='//a[@href="//docs.ozon.ru/common/"]')

    free_delivery = WebElement(xpath='//a[@href="/my/deliveryPriceInfo"]')

    ozon_travel = WebElement(xpath="//ul[@class='c6c9']/li[13]")

    discount = WebElement(xpath="//ul[@class='c6c9']/li[14]")

    order_list = WebElement(xpath='//div[@url="/my/orderlist"]')

    favorites = WebElement(xpath='//a[@href="/my/favorites"]')

    cart = WebElement(xpath='//a[@href="/cart/"]')

    catalog_btn = WebElement(xpath='//div[@data-widget="catalogMenu"]')

    catalog_smartphones = WebElement(xpath='//a[@href="/category/smartfony-15502/"]')

    search_input = WebElement(xpath='//form[@action="/search"]/div[2]/input')

    search_btn = WebElement(xpath='//form[@action="/search"]/button')

    sort = WebElement(xpath='/html/body/div[1]/div/div[1]/div[3]/div[2]/div[2]/div[3]/div[1]/div/div/div/div[1]/div[1]')

    sort_by_price_low_to_high = WebElement(xpath='//div[@role="option"][3]')

    sort_by_price_high_to_low = WebElement(xpath='//div[@role="option"][4]')

    sort_by_new = WebElement(xpath='//div[@role="option"][2]')

    sort_by_popular = WebElement(xpath='//div[@role="option"][1]')

    sort_by_discount = WebElement(xpath='//div[@role="option"][5]')

    sort_by_rating = WebElement(xpath='//div[@role="option"][6]')

    products_prices = ManyWebElements(xpath='//div[@class="b5v4 a5d2 item a1d1"]//span')

    products = ManyWebElements(xpath='//div[@class="a0c4"]')

    products_discounts = ManyWebElements(xpath='//div[@class="b0e6 b0e7 a5d2 item a1d1"]//span')

    products_titles = ManyWebElements(xpath='//a[@class="tile-hover-target b3u9"]/span/span')

    search_not_found = WebElement(xpath='//div[@class="b6q3"]')

    first_line_footer = ManyWebElements(xpath='//footer/div/div/div/a[1]')

    second_line_footer = ManyWebElements(xpath='//footer/div/div/div/a[2]')

    third_line_footer = ManyWebElements(xpath='//footer/div/div/div/a[3]')

    forth_line_footer = ManyWebElements(xpath='//footer/div/div/div/a[4]')

    ozon_business_partner_footer = WebElement(xpath='//footer/div/div/div/a[@href="https://business.ozon.ru/partners?perehod=footer"]')

    ozon_business_footer = WebElement(xpath='//footer/div/div/div/a[@href="https://business.ozon.ru/?perehod=footer"]')

    what_to_sell_footer = WebElement(xpath='//footer/div/div/div/a[@href="https://seller.ozon.ru/what_to_sell/?perehod=footer"]')

    ecomschool_footer = WebElement(xpath='//footer/div/div/div/a[@href="https://www.ozon.ru/info/ecomschool"]')

    vk_footer = WebElement(xpath='//footer/div[1]/div/div[5]/div[2]/a[@href="https://vk.com/ozon"]')

    facebook_footer = WebElement(xpath='//footer/div[1]/div/div[5]/div[2]/a[@href="https://www.facebook.com/ozon.ru"]')

    social_networks_footer = ManyWebElements(xpath='//footer/div[1]/div/div[5]/div[2]/a')
