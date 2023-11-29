import requests

if __name__ == '__main__':

    BASE_URL = 'http://127.0.0.1:8080'
    SUBSCRIBE_URL = BASE_URL + '/subscribe'
    SEND_TOKEN_URL = BASE_URL + '/trello/?access_token='

    # get the token from the file token.txt
    with open('token.txt', 'r') as f:
        token = f.read()

    response = requests.post(SUBSCRIBE_URL, headers={'Authorization': 'Bearer ' + token}, json={"service": "trello", "service_args": {"return_url": "http://invalide"}})
    # the response is a redirect to the trello auth page can you print redirect url
    print(response.url)
    # make up a fake access token and send it to the server
    response = requests.get(SEND_TOKEN_URL + 'fake_token', headers={'Authorization': 'Bearer ' + token})
    print(response.json())