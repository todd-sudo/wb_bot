import datetime
from typing import List

import requests

from config import DOMAIN, PAGE_SIZE


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
        response = requests.get(url=_url)
        data = response.json()
        if response and response.status_code == 200:
            break
        count += 1
    return data


def parse_products(products: List[dict]) -> str:
    message = ""
    for item in products:
        sku = item.get("sku")
        name = item.get("name")
        price = item.get("price")
        percentage = item.get("percentage")
        url = item.get("url")
        date_updated = item.get("date_updated")
        message += f"Код товара: {sku}\n{name}\nЦена: {price}" \
                   f"\nПроцент заниженной цены: {percentage}" \
                   f"\n{url}\n{date_updated}\n\n"

    return message
