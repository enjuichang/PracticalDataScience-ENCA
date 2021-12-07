### Full script code below ###
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def ari_to_genre(ari):
    
    cid = 'a3464137dc59465f81d287f5626212c5'

    with open("secret.txt") as f:
        secret = f.readlines()[0]

    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
    
    artist = sp.track(ari)["artists"][0]["id"]
    
    return {"Artist": sp.artist(artist)["popularity"],
            "Track": sp.track(ari)["popularity"]}
