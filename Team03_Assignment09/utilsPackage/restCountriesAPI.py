#restCountriesAPI.py
# Name: Team03
# Assignment Number: Assignment 09
# Due Date: 4-04-2024
# Course/Section:IS 4010-002
# Semester/Year: Spring 2024
# Brief Description of the assignment: Research API's and extract interesting data
# Citations: https://restcountries.com/

import http.client
import json
from urllib.parse import quote

def REST_Countries(countryInput=None): 
    '''
    Connect to a API server and retrieve data about the specified country.

    Parameters:
    - countryInput (str): The name of the country to retrieve data for. If not provided, the user will be prompted for input.

    Returns:
    None

    '''
    
    if countryInput is None:
        # If no countryInput is provided, ask the user for input
        countryInput = input("What country do you want to know about? ")

    # Encode the country name
    encoded_country_name = quote(countryInput)

    # Define the base URL and endpoint
    base_url = "restcountries.com"
    endpoint = f"/v3.1/name/{encoded_country_name}"
    
    # Establish connection to the server
    conn = http.client.HTTPSConnection(base_url)
    
    # Send a GET request to the API
    conn.request("GET", endpoint)
    
    # Get the response from the server
    response = conn.getresponse()
    
    try:
        # Check if the request was successful (status code 200)
        if response.status == 200:
            # Read the response data
            data = response.read().decode('utf-8')
            
            # Parse the JSON response into a Python dictionary
            country_data = json.loads(data)
        
            # Extract some interesting data from the dictionary
            country_name = country_data[0]['name']['common']
            capital = country_data[0]['capital'][0]
            population = country_data[0]['population']
            languages = ', '.join(country_data[0]['languages'])
        
            # Print the extracted data in a friendly and informative format
            print("Country:", country_name)
            print("Capital:", capital)
            print("Population:", population)
            print("Languages:", languages)
        else:
            # If the request was unsuccessful, print the status code
            print("Failed to retrieve country. Status code:", response.status)
    except Exception as e:
        print("An error occurred:", e)

    # Close the connection
    conn.close()