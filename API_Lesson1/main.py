import requests


def get_weather(place):
    url = 'https://wttr.in/{}'.format(place)
    payload = {'lang': 'ru', 'M': '', 'n': '', 'q': '', 'T': ''}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    return response.text


if __name__ == '__main__':
    locations = ['Лондон', 'аэропорт Шереметьево', 'Череповец']
    for location in locations:
        print(get_weather(location))