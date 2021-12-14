### Full script code below ###
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def ari_to_features(ari):
    
    cid = 'a3464137dc59465f81d287f5626212c5'

    with open("secret.txt") as f:
        secret = f.readlines()[0]

    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
    
    #Audio features
    features = sp.audio_features(ari)[0]
    
    #Artist of the track, for genres and popularity
    artist = sp.track(ari)["artists"][0]["id"]
    artist_pop = sp.artist(artist)["popularity"]
    artist_genres = sp.artist(artist)["genres"]
    
    #Track popularity
    track_pop = sp.track(ari)["popularity"]
    
    #Add in extra features
    features["artist_pop"] = artist_pop
    if artist_genres:
        features["genres"] = artist_genres[0]
    else:
        features["genres"] = "unknown"
    features["track_pop"] = track_pop
    
    return features
