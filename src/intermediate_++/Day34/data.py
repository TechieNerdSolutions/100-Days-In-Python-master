import requests

parameters = {
    "amount": 50,
    "category": 18,
    "type": "boolean",
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]
print(question_data)
