import requests
import json
import time
import pygame

# Initialize the pygame mixer
pygame.mixer.init()

# Define the API endpoint
url = "https://earthquake.usgs.gov/fdsnws/event/1/query"

# Set the initial request parameters
parameters = {
    "format": "geojson",
    "starttime": "now-30minutes",
    "minmagnitude": 4
}

while True:
    # Send the GET request and get the response
    response = requests.get(url, params=parameters)

    # Parse the response as JSON
    data = json.loads(response.text)

    # Check if there are any earthquakes with magnitude 4 or greater
    if data["metadata"]["count"] > 0:
        print("WARNING: Earthquake detected with magnitude 4 or greater!")
        # Play a sound beep to alert the user
        pygame.mixer.music.load("beep.wav")  # Load the sound file
        pygame.mixer.music.play()  # Play the sound
    else:
        print("No earthquakes detected.")

    # Wait for 30 minutes before making the next API call
    time.sleep(1800)  # 1800 seconds = 30 minutes

