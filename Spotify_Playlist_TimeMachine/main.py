from  datetime import datetime
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth
import requests, os, spotipy

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

# Prompt the user to enter a valid date
while True:
    date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
    try:
        valid_date = datetime.strptime(date, '%Y-%m-%d')
        break
    except:
        print("That's not a valid date. Please try again.")

# Fetch the Billboard Hot 100 chart for the specified date
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
response.raise_for_status()

# Parse the HTML response using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Extract the names of the top 100 songs from the chart
songs_name = soup.select(selector="li h3", class_='c-title')[:100]
songs = []

# Clean up the song names and store them in a list
for song_name in songs_name:
    song = song_name.text.strip()
    songs.append(song)

# Authenticate with Spotify using the provided client ID and secret
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri="http://example.com",
        scope='playlist-modify-private'
    )
)

# Get the user ID of the authenticated Spotify user
user_id = sp.current_user()["id"]

song_uris = []
year = date.split("-")[0]

# Search for each song in Spotify and add its URI to the list
for song in songs:
    result = sp.search(q=f"track:{song}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Create a new playlist on the user's Spotify account
playlist = sp.user_playlist_create(user_id, f'{date} Billboard 100', public=False, description=f'{date} Billboard Top 100 Songs')

# Add the songs to the created playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)