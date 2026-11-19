import requests

url = "https://randomuser.me/api/"

# Send a get request to the API endpoint
response = requests.get(url)

# Check if API request was successful
status = response.status_code

if status != 200:
    print("API request was not successful!")
else:
    print(f"API request succeeded with status code: {status}")
    print("Response content:")

# Convert JSON data to Python dictionary
data = response.json()

user = data['results'][0]

# Print the user data
print(f"Name: {user['name']['first']} {user['name']['last']}")
print(f"Location: {user['location']['city']}")