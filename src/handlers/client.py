from aiogram.utils.markdown import hlink

import requests

from config import DOMAIN, PAGE_SIZE
from src.handlers.image import get_image_url


def get_products(sort: str, url: str = ""):
    """ Получает товары из API
    """
    _url = f"{DOMAIN}/api/parser/get-underprice-products" \
           f"/?sort={sort}&page_size={PAGE_SIZE}"
    if url:
        _url = url
    count = 0
    while True:
        if count > 10:
            return {}
        try:
            response = requests.get(url=_url)
        except requests.exceptions.SSLError:
            response = requests.get(url=_url, verify=False)
        data = response.json()
        if response and response.status_code == 200:
            break
        count += 1
    return data


# def parse_products(products: List[dict]) -> str:
#     message = ""
#     for item in products:
#         sku = item.get("sku")
#         name = item.get("name")
#         price = item.get("price")
#         percentage = item.get("percentage")
#         url = item.get("url")
#         date_updated = item.get("date_updated")
#         message += f"Код товара: {sku}\n{name}\nЦена: {price}" \
#                    f"\nПроцент заниженной цены: {percentage}" \
#                    f"\n{url}\n{date_updated}\n\n"
#
#     return message


def parse_products(item: dict) -> str:
    sku = item.get("sku")
    name = item.get("name")
    price = item.get("price")
    percentage = item.get("percentage")
    url = item.get("url")
    count_in_stock = item.get("count_in_stock")
    count_in_stock_old = item.get("count_in_stock_old")
    basic_sale = item.get("basic_sale")
    client_sale = item.get("client_sale")
    # TODO: price_no_sale - добавить цену из 1С
    price_no_sale = item.get("price_no_sale")
    basic_price = item.get("basic_price")
    is_active = item.get("is_active")
    if is_active:
        is_active = "Да"
    else:
        is_active = "Нет"
    date_updated = item.get("date_updated") #.split("T")
    # _date = date_updated[0]
    # _time = date_updated[1].split(".")[0]
    # date_updated = f"{_date} {_time}"
    image = get_image_url(sku)
    image = hlink("🖥 Изображение:", image)
    sku_link = hlink(sku, url)
    message = """
SKU: {0}
Название: {1}

Наша цена: {2} руб.
Цена со скидкой: {3} руб. ({4}%)
СПП: {5} руб. ({6}%)

Наличие на складе: {7}
Кол-во на складе: {8}/{9} шт.

Дата обновления: {10}

{11}

""".format(
        sku_link,
        name,
        price_no_sale,
        basic_price,
        basic_sale,
        price,
        client_sale,
        # percentage,
        is_active,
        count_in_stock,
        count_in_stock_old,
        date_updated,
        image,
    )

    return message
