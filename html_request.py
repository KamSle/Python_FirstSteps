##first request in basic method using requests module -we access non easy hard to read data 
# 1
# import requests
# url = "http://www.google.com"
# response = requests.get(url)

# print(f"your request to {url} came back w/ status code {response.status_code}")
# print(response.text)

## request using headers 
# 2 
# import requests
# url = "https://icanhazdadjoke.com/"

# response = requests.get(url, headers={"Accept": "application/json"})  # that gives us json 

# data = response.json() # that gives us python (json turn to python) 

# print(data) # we get dictionary here
# print(data["joke"]) # we ask for value where key is joke
# print(f"status: {data['status']}")

## request using headers and params in order to query string
# 3

import requests
url = "https://icanhazdadjoke.com/search"

response = requests.get(
	url, 
	headers={"Accept": "application/json"}, ## get json
	params={"term": "cat", "limit": 1}  ## get jokes about cats and limit it to one joke
)

data = response.json() ## make it to python -> dictionary
#print(data)
p = data["results"][0]
#pp = p[0]
print(p["joke"]) # get the joke as 