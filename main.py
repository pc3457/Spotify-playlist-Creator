import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

client_id = "Your_client_id"
client_secret = "your_client_secret"
SPOTIFY_DISPLAY_NAME = "your_display_name"

input_date = input("Which date do you want to travel back in to? Insert Date in his format YYYY-MM-DD ")
# print(input_date)
URL = f"https://www.billboard.com/charts/hot-100/{input_date}/"

response = requests.get(URL)

web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

songs = soup.select("li ul li h3")

song_names = [song.get_text().strip() for song in songs]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=client_id,
        client_secret=client_secret,
        show_dialog=True,
        cache_path="token.txt",
        username=SPOTIFY_DISPLAY_NAME
    )
)

user_id = sp.current_user()["id"]

song_uris = []
year = input_date.split("-")[0]
for track in song_names:
    result = sp.search(q=f"track:{track} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{track} does not exist on Spotify, skipped.")

playlist = sp.user_playlist_create(user=user_id,name=f"{input_date} Billboard top 100.",public=False)

sp.playlist_add_items(playlist_id=playlist["id"],items=song_uris)
