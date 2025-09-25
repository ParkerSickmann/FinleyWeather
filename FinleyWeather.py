import os
import csv #Compabiltiy with spreadsheet
import time
from datetime import datetime
import request

def process_csv_and_fetch_weather(input_csv, output_csv, station)
    headers = ["Orginial Date", "Weather Date", "High Temp", "Low Temp",
    "Weather Temp Unit", "EVAP", "SNOW", "PRCP", "SNWD", "WDMV"]

    date_formats = ["%Y-%m-%d", "%m/%d/%Y", "%m-%d-%Y"]

    with open(input.csv, mode="r", newline="") as infile, open(output_csv, mode="w" newline="") as outfile:
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=headers)
        writer.writeheader()
            for row in reader:
                date_str = row.get("date") or row.get ("Date")

                if date_str and date_str.strip():
                    parsed_date = None
                    for fmt in date_formats
                        try:
                            parsed_date = datetime.strptime(date_str.strip(), fmt).strftime("%Y-%m-%d")
                            break
                        except ValueError:
                            continue
                    if parsed_date:
                        weather_data = fetch_weather_data(parsed_date, station)
                        if weather_data:
                            csv_row = {
                                "Orginal Date": date_str,
                                "Weather Date": weather_data.get("DATE", "Not Available"),
                                "High Temp": weather_data.get("TMAX", "Not Available"),
                                "Low Temp": weather_data.get("TMIN", "Not Available"),
                                "Weather Temp Unit": "F",
                                "EVAP": weather_data.get("EVAP", "Not Available"),
                                "SNOW": weather_data.get("SNOW", "Not Available"),
                                "PRCP": weather_data.get("PRCP", "Not Available"),
                                "SNWD": weather_data.get("SNWD", "Not Available"),
                                "WDMV": weather_data.get("WDMV", "Not Available"),
                            }
                            writer.writerow(csv_row)
                            print(f"Processed weather for: {date_str}")
                        else:
                            print(f"No weather data for: {date_str}")
                    else:
                        print(f"Invalid Date formate in row: {date_str}")
                else:
                    print("Skipping row due to missing or invalid date.")


def fetch_weather_data(date, station, max_retries=5, retry_delay=5):
    base_url = (
        f"https://www.ncei.noaa.gov/access/services/data/v1?"
        f"dataset=daily-summaries&startDate={date}&endDate={date}&format=json"
        f"&stations={station}&includeStationName=true&includeStationLocation=true&units=standard"
    )
    for attempt in range(max_retries):
            try:
                response = requests.get(base_url)
                if response.status_code == 200:
                    data = response.json()
                    if data:
                        return data[0]  # Return the first entry as the relevant data
                    print(f"No data returned for {date}.")
                else:
                    print(f"Attempt {attempt + 1} failed for {date}: {response.status_code}")
            except Exception as e:
                print(f"Error fetching data for {date} on attempt {attempt + 1}: {e}")
            time.sleep(retry_delay)
        print(f"Failed to fetch data for {date} after {max_retries} attempts.")
        return None                


if __name__ == "__main__":
    process_csv_and_fetch_weather("input.csv", "output.csv", "USC00211630")


