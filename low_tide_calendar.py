import os
import requests
from datetime import datetime, timedelta
from ics import Calendar, Event
import pytz
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def fetch_tide_data(lat, lon, start_date, end_date):
    api_key = os.getenv('WORLDTIDES_API_KEY')
    if not api_key:
        raise ValueError("WorldTides API key not found. Please set it in your .env file.")
    
    url = f"https://www.worldtides.info/api/v2?heights&lat={lat}&lon={lon}&start={start_date}&length={end_date-start_date}&key={api_key}"
    response = requests.get(url)
    return response.json()

# ... [rest of the functions remain the same] ...

def main():
    # Input GPS coordinates
    lat = input("Enter latitude (e.g., 13.0773): ")
    lon = input("Enter longitude (e.g., -59.6087): ")
    
    # Set date range (3 months from today)
    start_date = int(datetime.now().timestamp())
    end_date = int((datetime.now() + timedelta(days=90)).timestamp())
    
    # Fetch tide data
    tide_data = fetch_tide_data(lat, lon, start_date, end_date)
    
    # Create low tide events
    events = create_low_tide_events(tide_data)
    
    # Generate .ics file
    generate_ics_file(events, "low_tides.ics")
    
    print(f"Generated low_tides.ics with {len(events)} low tide events.")

if __name__ == "__main__":
    main()