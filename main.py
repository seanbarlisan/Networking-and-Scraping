import requests 
from requests.exceptions import HTTPError

URLs = ['https://www.google.com/', 'https://www.amazon.com/invalid']

for url in URLs:
    try:
        response = requests.get(url) # obtain the response from the GET request for URL
        response.raise_for_status() # raise the response status, can give errors if found
    except HTTPError as http_err: # if there is an error for the response
        print(f"HTTP error occurred: {http_err}")
    except Exception as err: # if there is an exception for the response
        print(f"Other error occurred: {err}")
    else:
        print("Success!")
        print(response.json)