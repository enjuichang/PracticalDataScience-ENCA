#import requests
#import spotipy
#from spotipy.oauth2 import SpotifyClientCredentials
#import pandas as pd
import pprint

#data_path = "../data/First_1000.json"
#raw_json = json.loads(open(data_path).read())


#response = requests.get("https://api.spotify.com/v1/playlist/4uKHT9uD9f2X3EUxUT4z8a?si=6513cf0d237e4f1f", {
    #'client_id': "5356afb958c84e71a2c37c43e2a2cbf2" ,
    #'client_secret': "83e531491e9c458ba658ac30c4c56bc0"
#})
#print(response)
#client_credentials_manager = SpotifyClientCredentials(client_id="5356afb958c84e71a2c37c43e2a2cbf2" , client_secret="83e531491e9c458ba658ac30c4c56bc0")
#sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

#results = sp.playlist_items("4uKHT9uD9f2X3EUxUT4z8a", fields=None, limit=100, offset=0, market=None, additional_types=('track', 'episode'))
#pprint.pprint(results)

#df = pd.json_normalize(results, 
                #record_path='name')


#df.to_csv("../data/test_playlist.csv")

### Full script code below ###

##def ari_to_features(ari):
    
    #cid = "5356afb958c84e71a2c37c43e2a2cbf2"

    #with open("secret.txt") as f:
        #secret = f.readlines()[0]

    #client_credentials_manager = SpotifyClientCredentials(client_id="5356afb958c84e71a2c37c43e2a2cbf2" , client_secret="83e531491e9c458ba658ac30c4c56bc0")
    #sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
    
    #Audio features
    #features = sp.audio_features(ari)[0]
    
    #Artist of the track, for genres and popularity
    #artist = sp.track(ari)["artists"][0]["id"]
    #artist_pop = sp.artist(artist)["popularity"]
    #artist_genres = sp.artist(artist)["genres"]
    
    #Track popularity
    #track_pop = sp.track(ari)["popularity"]
    
    #Add in extra features
    #features["artist_pop"] = artist_pop
    #if artist_genres:
        #features["genres"] = artist_genres[0]
    #else:
        #features["genres"] = "unknown"
    #features["track_pop"] = track_pop
    
    #return features

#print(ari_to_features("1o0nAjgZwMDK9TI4TTUSNn"))

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import pandas as pd

def extract(URL):
    client_id = "5356afb958c84e71a2c37c43e2a2cbf2" 
    client_secret = "83e531491e9c458ba658ac30c4c56bc0"

    client_credentials_manager = SpotifyClientCredentials(client_id=client_id,client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

       # the URI is split by ':' to get the username and playlist ID
    playlist_id = URL.split("/")[4].split("?")[0]
    playlist_tracks_data = sp.playlist_tracks(playlist_id)

    playlist_tracks_id = []
    playlist_tracks_titles = []
    playlist_tracks_artists = []
    playlist_tracks_first_artists = []

    for track in playlist_tracks_data['items']:
        playlist_tracks_id.append(track['track']['id'])
        playlist_tracks_titles.append(track['track']['name'])
        # adds a list of all artists involved in the song to the list of artists for the playlist
        artist_list = []
        for artist in track['track']['artists']:
            artist_list.append(artist['name'])
        playlist_tracks_artists.append(artist_list)
        playlist_tracks_first_artists.append(artist_list[0])

    features = sp.audio_features(playlist_tracks_id)
    features_df = pd.DataFrame(data=features, columns=features[0].keys())
    features_df['title'] = playlist_tracks_titles
    features_df['first_artist'] = playlist_tracks_first_artists
    features_df['all_artists'] = playlist_tracks_artists
    features_df = features_df[['id', 'title', 'first_artist', 'all_artists',
                                'danceability', 'energy', 'key', 'loudness',
                                'mode', 'acousticness', 'instrumentalness',
                                'liveness', 'valence', 'tempo',
                                'duration_ms', 'time_signature']]
    
    return features_df



