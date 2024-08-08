import requests
import json
import re

def getPublicIP():
    # Get the IP address using an external service
    response = requests.get('http://checkip.dyndns.com/')
    # Extract the IP address using regex
    return re.search(r'Address: (\d+\.\d+\.\d+\.\d+)', response.text).group(1)

# Getting IP address
IP = getPublicIP()

# Getting Location
url = f'http://ipinfo.io/{IP}/json'
response = requests.get(url)
data = response.json()  # Use .json() method to parse JSON response

# Extracting location details
city = data.get('city', 'N/A')
region = data.get('region', 'N/A')
country = data.get('country', 'N/A')
location = data.get('loc', 'N/A')
org = data.get('org', 'N/A')

# Printing Extracted Details
print(f"City: {city}")
print(f"Region: {region}")
print(f"Country: {country}")
print(f"Location: {location}")
print(f"Organization: {org}")
