from rest_framework import status
from rest_framework.test import RequestsClient
from string import ascii_uppercase, ascii_lowercase, digits
from random import sample

client = RequestsClient()

response = client.post(
    url='http://127.0.0.1:8000/api/create-short-link/',
    json={"url": "twitch.com"}
)

assert response.json().get('url') == 'https://twitch.com'
assert response.status_code == status.HTTP_201_CREATED

response = client.get(url=f'http://127.0.0.1:8000/api/{response.json().get("short_link")}')

assert response.json().get('url') == 'https://twitch.com'
assert response.status_code == status.HTTP_200_OK

response = client.post(
    url='http://127.0.0.1:8000/api/create-custom-short-link/',
    json={
        "url": "dsdsd.codsdm", 
        "custom_short_link": "asdasdsa"
        }
)

assert response.json().get('error') == 'Unable to shorten that link. It is not a valid url.'
assert response.status_code != status.HTTP_201_CREATED

custom_short_link = ''.join(sample(ascii_uppercase + ascii_lowercase + digits, 10))

response = client.post(
    url='http://127.0.0.1:8000/api/create-custom-short-link/',
    json={
        "url": "twitch.com", 
        "custom_short_link": f"{custom_short_link}"
        }
)

assert response.json().get('url') == 'https://twitch.com'
assert response.json().get('custom_short_link') == custom_short_link
assert response.status_code == status.HTTP_200_OK

response = client.get(url=f'http://127.0.0.1:8000/api/{custom_short_link}')

assert response.json().get('url') == 'https://twitch.com'
assert response.status_code == status.HTTP_200_OK
