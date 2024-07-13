import requests


mynums = {
    "num1":5,
    "num2": 69
    }

r = requests.post("http://127.0.0.1:8000/calc", json = mynums)

print(r.json())