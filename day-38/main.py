import requests
from datetime import datetime

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


json_response = response.json()
now = datetime.now()
formatted_date = now.strftime("%d/%m/%Y")
formatted_time = now.strftime("%H:%M:%S")


google_sheet_endpoint = "https://api.sheety.co/e21a8e91526b16245a7b34dab6850543/myWorkouts/workouts"


for exercise in json_response["exercises"]:
    workout_sheets = {
        "workout": {
            "date": formatted_date,
            "time": formatted_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    sheet_response = requests.post(url=google_sheet_endpoint, json=workout_sheets)
    print(sheet_response.status_code)
    print(sheet_response.text)