import requests

BASE = "http://127.0.0.1:5000/"

# response = requests.get(BASE + "helloworld/theName/25")
# print(response.json())


# response = requests.post(BASE + "helloworld")
# print(response.json())

# response = requests.get(BASE + "helloworld/mik")
# print(response.json())

# response = requests.get(BASE + "video/1")
# print(response.json())

# response = requests.put(BASE + "video/1", {"name":"adults", "views":None, "likes":102})
# print(response.json())

response = requests.put(BASE + "video/1", {"likes":102})
print(response.json())
input()
response = requests.get(BASE + "video/1", {"likes":102})
print(response.json())
