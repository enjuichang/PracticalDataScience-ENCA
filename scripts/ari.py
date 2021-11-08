### Full script code below ###

def ari_to_features(ari):
    import spotipy
    from spotipy.oauth2 import SpotifyClientCredentials
    
    cid = 'a3464137dc59465f81d287f5626212c5'

    with open("secret.txt") as f:
        secret = f.readlines()[0]

    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
    
    return sp.audio_features(ari)
