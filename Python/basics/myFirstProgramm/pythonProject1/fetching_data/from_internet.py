from urllib import request
import json

# URL to fetch jokes
url = "https://official-joke-api.appspot.com/random_ten"

# Sending the request
r = request.urlopen(url)

# Read and decode the response once
data = r.read().decode('utf-8')

# Optionally, print the raw response (JSON string)
print(data)

# Parse the JSON data
json_data = json.loads(data)

# Define the Joke class
class Joke:
    def __init__(self, setup, punchline) -> None:
        self.setup = setup
        self.punchline = punchline

    def __str__(self):
        return f"Setup: {self.setup}\nPunchline: {self.punchline}"

# Create a list to hold jokes
jokes = []

# Populate the list with Joke objects
for j in json_data: # hold a directory joke
    setup = j["setup"]
    punchline = j.get("punchline")
    joke = Joke(setup, punchline)
    jokes.append(joke)

# Print the number of jokes
print(f"Got {len(jokes)} jokes")

# Print each joke
for joke in jokes:
    print(joke)

# Optional: Print additional response details
print(f"Status Code: {r.getcode()}")  # Get the HTTP status code
print(f"Headers: {r.info()}")         # Get the response headers
print(f"URL: {r.geturl()}")           # Get the URL of the request

