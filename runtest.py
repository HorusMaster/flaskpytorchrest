import requests

resp = requests.post("http://localhost:5000/predict",
                     files={"file": open('./fish.jpg','rb')})
print(resp.json()) 
print("HELLo")