import requests

#api endpoint -- fake JSON API for testing my environment
url = "https://jsonplaceholder.typicode.com/posts1"

# Send a get request to the API endpoint
response = requests.get(url)

# Check if API request was successful
print(response.status_code)

# Convert JSON data to Python dictionary
data = response.json()


# Print the data
print(data)