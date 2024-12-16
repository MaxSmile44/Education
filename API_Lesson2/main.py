import os
from urllib.parse import urlparse, urlunparse

from dotenv import load_dotenv
import requests


def shorten_link(token, url):
    vk_url = 'https://api.vk.ru/method/utils.getShortLink'
    payload = {'v': '5.81', 'access_token': token, 'url': url}
    responce = requests.get(vk_url, params=payload)
    return responce.json()['response']['short_url']


def count_clicks(token, url):
    vk_url = 'https://api.vk.ru/method/utils.getLinkStats'
    payload = {'v': '5.81', 'access_token': token, 'key': url}
    responce = requests.get(vk_url, params=payload)
    return responce.json()


def is_shorten_link(url):
    return urlparse(url).netloc == 'vk.cc'


def main(token):
    url = input('Введите ссылку: ')
    url = 'https://' + url if not url.startswith('http') else url
    try:
        check_link = requests.get(url)
        if check_link.status_code == 200:
            if not is_shorten_link(url):
                short_link = shorten_link(token=token, url=url)
                print(f'Сокращенная ссылка: {short_link}')
            else:
                print(f'Количество переходов по ссылке: '
                      f'{count_clicks(token, urlparse(url).path[1:])['response']['stats'][0]['views']}')
        else:
            print('Такого адреса не существует')
    except (requests.exceptions.ConnectionError, requests.exceptions.MissingSchema, requests.exceptions.InvalidSchema):
        print('Такого адреса не существует')


if __name__ == '__main__':
    load_dotenv()
    vk_token = os.getenv("VK_TOKEN")
    main(vk_token)