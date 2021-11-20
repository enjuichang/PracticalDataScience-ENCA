### Full script code below ###
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def ari_to_features(ari):
    
    cid = 'd2ac9b58eebb4025a28f27e72e2ca133'

    with open("secret.txt") as f:
        secret = f.readlines()[0]

    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
    
    return sp.audio_features(ari)
