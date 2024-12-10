import requests


def get_weather(place):
    url = 'https://wttr.in/{}?lang=ru&M&n&q&T'.format(place)
    response = requests.get(url)
    response.raise_for_status()
    return response.text


if __name__ == '__main__':
    print(get_weather('Лондон'), get_weather('аэропорт Шереметьево'), get_weather('Череповец'))