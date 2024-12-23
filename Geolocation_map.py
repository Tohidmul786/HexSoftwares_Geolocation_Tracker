

import requests
import folium

# Step 1: Fetch geolocation using the public IP address
def get_geolocation():
    url = 'https://ipinfo.io/json'  # API endpoint to get geolocation from IP address
    try:
        # Send request to ipinfo.io to get geolocation info
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            # Extract data from response
            ip_address = data.get("ip")
            city = data.get("city")
            region = data.get("region")
            country = data.get("country")
            loc = data.get("loc")  # Location (latitude, longitude)
            print("Your location has been tracked :- ")
            print(f"IP Address: {ip_address}")
            print(f"City: {city}")
            print(f"Region: {region}")
            print(f"Country: {country}")
            print(f"Location: {loc}")

            return loc
        else:
            print("Error fetching geolocation")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Step 2: Map the geolocation using Folium
def map_location(loc):
    if loc:
        # Split the loc into latitude and longitude
        latitude, longitude = map(float, loc.split(','))

        # Create a map centered around the geolocation
        location_map = folium.Map(location=[latitude, longitude], zoom_start=12)

        # Add a marker on the map
        folium.Marker([latitude, longitude], popup="Your Location").add_to(location_map)

        # Save the map as an HTML file
        location_map.save("location_map.html")
        print("Map saved as 'location_map.html'. Please open this file in a browser to view the map.")
    else:
        print("Location could not be found.")

# Main function
def main():
    loc = get_geolocation()  # Get the geolocation based on IP
    map_location(loc)  # Display the location on a map

if __name__ == "__main__":
    main()