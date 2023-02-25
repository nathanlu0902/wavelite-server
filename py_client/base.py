import requests

endpoint="http://127.0.0.1:8000/api/10202/create"

data={
  "nickname":"nl"
}
response=requests.post(endpoint,json=data)
print(response)