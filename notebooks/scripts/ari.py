### Full script code below ###
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import re 

def ari_to_features(ari):

    with open("secret.txt") as f:
        secret_ls = f.readlines()
        cid = secret_ls[0][:-2]
        secret = secret_ls[1]

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
        features["genres"] = " ".join([re.sub(' ','_',i) for i in artist_genres])
    else:
        features["genres"] = "unknown"
    features["track_pop"] = track_pop
    
    return features

if __name__ == "__main__":
    # Debug
    result = ari_to_features("1o0nAjgZwMDK9TI4TTUSNn")
    print(result)