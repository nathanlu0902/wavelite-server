import requests

# endpoint="http://127.0.0.1:8000/api/10202/update"

# data={
#   "nickname":"nl",
#   "openid":"10202",
#   "gender":"m"
# }
# response=requests.put(endpoint,json=data)
# print(response.json())

endpoint="http://127.0.0.1:8000/api/10202/login"

response=requests.get(endpoint)
print(response.json())