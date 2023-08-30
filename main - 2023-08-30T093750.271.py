import requests

def get_traffic_data(address):
    api_key = "your_api_key"  # Replace with your actual MassDOT API key
    base_url = "https://api.example.com/massdot/traffic"  # Replace with the actual API endpoint

    # Construct the API request URL
    params = {
        "address": address,
        "api_key": api_key
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code)
        return None

def main():
    address = "123 Main Street, Boston, MA"  # Replace with the desired address
    traffic_data = get_traffic_data(address)

    if traffic_data:
        print("Traffic Data for", address)
        print("Total Vehicles:", traffic_data.get("total_vehicles", "N/A"))
        print("Average Speed:", traffic_data.get("average_speed", "N/A"))
    else:
        print("Failed to retrieve traffic data.")

if __name__ == "__main__":
    main()
