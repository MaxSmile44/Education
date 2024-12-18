import os
from urllib.parse import urlparse, urlunparse

from dotenv import load_dotenv
import requests


def shorten_link(token, url):
    vk_url = 'https://api.vk.ru/method/utils.getShortLink'
    payload = {'v': '5.81', 'access_token': token, 'url': url}
    response = requests.get(vk_url, params=payload)
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as error:
        print(f'HTTP error occurred: {error}')
    decoded_response = response.json()
    if 'error' in decoded_response:
        raise requests.exceptions.HTTPError(decoded_response['error'])
    return response.json()['response']['short_url']


def count_clicks(token, url):
    vk_url = 'https://api.vk.ru/method/utils.getLinkStats'
    url = urlparse(url).path.replace('/', '').replace('vk.cc', '')
    payload = {'v': '5.81', 'access_token': token, 'key': url}
    response = requests.get(vk_url, params=payload)
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as error:
        print(f'HTTP error occurred: {error}')
    decoded_response = response.json()
    if 'error' in decoded_response:
        raise requests.exceptions.HTTPError(decoded_response['error'])
    return response.json()['response']['stats'][0]['views']


def is_shorten_link(token, url):
    try:
        count_clicks(token, url)
        return True
    except requests.exceptions.HTTPError:
        return False


def main():
    url = input('Введите ссылку: ')
    try:
        load_dotenv()
        token = os.environ["VK_TOKEN"]
    except KeyError as error:
        print(f'KeyError: {error}')
        raise SystemExit
    try:
        if is_shorten_link(token, url):
            print(f'Количество переходов: {count_clicks(token, url)}')
        else:
            print(f'Сокращенная ссылка: {shorten_link(token, url)}')
    except requests.exceptions.HTTPError as error:
        print(f'HTTP error occurred: {error}')
        raise SystemExit


if __name__ == '__main__':
    main()