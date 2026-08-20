import requests
from bs4 import BeautifulSoup

def parse_dns(query):
    url = f"https://www.dns-shop.ru/catalog/17a89a3916404e77/operativnaya-pamyat-dimm/?q={query}"
    headers = {
        'Referer': url,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        'Upgrade-Insecure-Requests': '1',
        'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    results = []
    # Основной парсинг по карточкам товаров:
    for product in soup.select('.catalog-product'):
        title = product.select_one('.catalog-product__name')
        price = product.select_one('.product-buy__price')
        title_text = title.get_text(strip=True) if title else 'Нет названия'
        price_text = price.get_text(strip=True) if price else 'Нет цены'
        results.append(f"{title_text} | {price_text}")
    # Если карточек нет — возможно страница выдала одну позицию (не в списке, а сразу)
    if not results:
        title = soup.select_one('.catalog-product__name')
        price = soup.select_one('.product-buy__price')
        title_text = title.get_text(strip=True) if title else 'Нет названия'
        price_text = price.get_text(strip=True) if price else 'Нет цены'
        results.append(f"{title_text} | {price_text}")
    return results if results else ["Товар не найден или возникла ошибка."]

def parse_onlinetrade(query):
    url = f"https://www.onlinetrade.ru/catalogue/komplektuyushchie_c168/operativnaya_pamyat_c2222.html?query={query}"
    headers = {
        'Referer': url,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    results = []
    for product in soup.select('.listing-item'):
        title = product.select_one('.catalog__displayedName')
        price = product.select_one('.catalog__price')
        title_text = title.get_text(strip=True) if title else 'Нет названия'
        price_text = price.get_text(strip=True) if price else 'Нет цены'
        results.append(f"{title_text} | {price_text}")
    return results if results else ["Товар не найден или возникла ошибка."]

def parse_citilink(query):
    url = f"https://www.citilink.ru/search/?text={query}&category=116"
    headers = {
        'Referer': url,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    results = []
    for product in soup.select('.ProductCardVertical'):
        title = product.select_one('.ProductCardVertical__name')
        price = product.select_one('.ProductCardVertical__price-current')
        title_text = title.get_text(strip=True) if title else 'Нет названия'
        price_text = price.get_text(strip=True) if price else 'Нет цены'
        results.append(f"{title_text} | {price_text}")
    return results if results else ["Товар не найден или возникла ошибка."]

def parse_komus(query):
    url = f"https://www.komus.ru/search/default.do?query={query}"
    headers = {
        'Referer': url,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    results = []
    for product in soup.select('.goods__item_wrapper'):
        title = product.select_one('.goods__item_title')
        price = product.select_one('.price')
        title_text = title.get_text(strip=True) if title else 'Нет названия'
        price_text = price.get_text(strip=True) if price else 'Нет цены'
        results.append(f"{title_text} | {price_text}")
    return results if results else ["Товар не найден или возникла ошибка."]

def parse_xcom(query):
    url = f"https://www.xcom-shop.ru/search/?query={query}"
    headers = {
        'Referer': url,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    results = []
    for product in soup.select('.product-card'):
        title = product.select_one('.product-card__name')
        price = product.select_one('.product-card__price--value')
        title_text = title.get_text(strip=True) if title else 'Нет названия'
        price_text = price.get_text(strip=True) if price else 'Нет цены'
        results.append(f"{title_text} | {price_text}")
    return results if results else ["Товар не найден или возникла ошибка."]

if __name__ == "__main__":
    query = input("Введите артикул или название товара: ")

    all_results = []
    shops = [
        ("DNS", parse_dns),
        ("Onlinetrade", parse_onlinetrade),
        ("Ситилинк", parse_citilink),
        ("Комус", parse_komus),
        ("X-com shop", parse_xcom)
    ]

    for name, func in shops:
        print(f"\n{name}:")
        results = func(query)
        for line in results:
            print(line)
            all_results.append(f"{name}: {line}\n")

    with open("results.txt", "w", encoding="utf-8") as f:
        f.writelines(all_results)
