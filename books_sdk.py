import requests


class TokenError(Exception):
    pass


def check_token(token):
    params = {'token': token}
    endpoint = 'https://d5dsaolj35tv1tdu7fmd.apigw.yandexcloud.net/books/check_token'
    response = requests.get(endpoint, params=params)
    if response.status_code in [401, 403]:
        raise TokenError(response.text)
    response.raise_for_status()
    return response.ok


def get_book_by_id(token, book_id):
    params = {'token': token}
    endpoint = f'https://d5dsaolj35tv1tdu7fmd.apigw.yandexcloud.net/books/{book_id}'
    response = requests.get(endpoint, params=params)
    if response.status_code in [401, 403]:
        raise TokenError(response.text)
    response.raise_for_status()
    return response.json()


def get_author(book):
    return book['author']