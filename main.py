import requests

def get_flight_cost(api_key, origin, destination, date):
    base_url = 'https://partners.api.skyscanner.net/apiservices/browseroutes/v1.0'
    endpoint = f'/{origin}/USD/en-US/{destination}/{date}'
    headers = {'apiKey': api_key}

    try:
        response = requests.get(base_url + endpoint, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        if 'Quotes' in data:
            if data['Quotes']:
                return data['Quotes'][0]['MinPrice']
            else:
                return "No available quotes for the specified route and date."
        else:
            return "Invalid response from the API."

    except requests.exceptions.RequestException as e:
        return f"Error fetching data: {e}"

if __name__ == "__main__":
    # Replace 'YOUR_API_KEY' with your actual Skyscanner API key
    api_key = 'YOUR_API_KEY'
    
    # Example query: Fetch the cost for a one-way flight from New York to Los Angeles on a specific date
    origin = 'JFK-sky'
    destination = 'LAX-sky'
    date = '2024-03-01'
    
    result = get_flight_cost(api_key, origin, destination, date)
    print(f"Cost of the flight from {origin} to {destination} on {date}: {result}")
