import requests
import sys
from datetime import datetime, timedelta


def generate_token(username, password):
    payload = {
        'grant_type': 'password',
        'client_id': 'e4a9949fcfa04068f59abb5a658f2bac0a3428e4652315490b659d5ab3f35a9e',
        'client_secret': 'c75f14bbadc8bee3a7594412c31416f8300256d7668ea7e6e7f06727bfb9d220',
        'email': username, 
        'password': password
    }
    req = requests.post('https://owner-api.teslamotors.com/oauth/token', json=payload)
    if req.status_code == 200:
        response = req.json()
        created_at = datetime.fromtimestamp(response["created_at"])
        expires_in = timedelta(seconds=response["expires_in"])
        expiration_date = datetime.strftime(created_at + expires_in, "%B %d, %Y %H:%M:%S")
        print(f'Tesla Token: {response["access_token"]}')
        print(f'Expiration Date: {expiration_date}')
    elif req.status_code == 401:
        print('Incorrect username and/or password')
    else:
        print(req.reason)


if __name__ == '__main__':
    generate_token(sys.argv[1], sys.argv[2])


