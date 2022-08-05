import requests

resp = requests.post("http://localhost:3500/predict-leaves-or-thorns")

print(resp.text)
