import requests

endpoint_login = "http://127.0.0.1:8000/api/v1/auth/"

auth_response = requests.post(
    endpoint_login, json={"username": "timka", "password": "1"}
)

print(auth_response.json())


if auth_response.status_code == 200:

    token = auth_response.json()["token"]

    headers = {"Authorization": f"Token {token}"}

    endpoint = "http://127.0.0.1:8000/api/v1/"

    get_response = requests.get(endpoint, headers=headers)

    print(get_response.json())