import requests


APP_ID = "app_c5675b8137bb46a2a331a26a"
API_KEY = "nix_live_laVhbwIv4ZJ6VAy53Lr2t5L2lAHg9vwG"


main_url_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"


headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}


exercise_params = {
    "query": input("Tell me which exercises you did: ")
}


response = requests.post(url=main_url_endpoint, json=exercise_params, headers=headers)
print(response.text)
