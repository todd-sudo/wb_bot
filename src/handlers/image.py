import requests


headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) "
                  "Gecko/20100101 Firefox/102.0"
}


def create_url_img(p_sku: str) -> str:
    """ Генерирует ссылку на изображение WB
    """
    nil_str = '0000'
    if len(p_sku) == 7:
        img_id_str = p_sku[:4] + nil_str[:3]
    elif len(p_sku) > 7:
        _p_sku_last = p_sku[-4:]
        img_id_str = p_sku.replace(_p_sku_last, "") + nil_str
    elif len(p_sku) == 6 and p_sku[:3][-1] == "0":
        img_id_str = p_sku[:2] + nil_str
    else:
        img_id_str = p_sku[:3] + nil_str
    url = f"https://images.wbstatic.net/big/new/" \
          f"{img_id_str}/{p_sku}-1.jpg"
    return url


def get_image_url(sku: str) -> str:
    count = 0
    while True:
        if count > 10:
            return ""
        url = f"https://napi.wildberries.ru/api/catalog/{sku}/detail.aspx"
        response = requests.get(url=url, headers=headers)
        if response and response.status_code == 200:
            data = response.json()
            data = data.get("data")
            if data:
                colors = data.get("colors")
                if colors:
                    image = colors[0].get("previewUrl", None)
                    if not image:
                        image = create_url_img(sku)
                    return image
            return ""
        count += 1


