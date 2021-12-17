from pprint import pprint
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import re
import pandas as pd

def extract(URL):
    client_id = 'd2ac9b58eebb4025a28f27e72e2ca133'

    with open("secret.txt") as f:
        client_secret = f.readlines()[0]

    client_credentials_manager = SpotifyClientCredentials(client_id=client_id,client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

       # the URI is split by ':' to get the username and playlist ID
    playlist_id = URL.split("/")[4].split("?")[0]
    playlist_tracks_data = sp.playlist_tracks(playlist_id)

    playlist_tracks_id = []
    playlist_tracks_titles = []
    playlist_tracks_artists = []
    playlist_tracks_first_artists = []
    playlist_tracks_pop = []
    artist_pop_list = []
    artist_genres_list = []
    album_name_list = []

    for track in playlist_tracks_data['items']:
        album_name_list.append(track["track"]['album']['name'])
        playlist_tracks_id.append(track['track']['id'])
        playlist_tracks_titles.append(track['track']['name'])
        playlist_tracks_pop.append(track['track']['popularity'])

        # adds a list of all artists involved in the song to the list of artists for the playlist
        artist_list = []
        for artist in track['track']['artists']:
            artist_list.append((artist['name'],artist['id']))
        playlist_tracks_artists.append(artist_list)
        playlist_tracks_first_artists.append(artist_list[0][0])
        artist = sp.artist(artist_list[0][1])
        artist_pop_list.append(artist["popularity"])
        
        if artist["genres"]:
            artist_genres = " ".join([re.sub(' ','_',i) for i in artist["genres"]])
        else:
            artist_genres = "unknown"

        artist_genres_list.append(artist_genres)

    features = sp.audio_features(playlist_tracks_id)
    features_df = pd.DataFrame(data=features, columns=features[0].keys())

    features_df["artist_pop"] = artist_pop_list
    features_df["genres"] = artist_genres_list
    features_df['album_name'] = album_name_list
    features_df["track_pop"] = playlist_tracks_pop
    features_df['track_name'] = playlist_tracks_titles
    features_df['artist_name'] = playlist_tracks_first_artists
    features_df['all_artists'] = playlist_tracks_artists
    features_df = features_df[['id', 'album_name','track_name', 'artist_name', 'all_artists',
                                'danceability', 'energy', 'key', 'loudness',
                                'mode', 'acousticness', 'instrumentalness',
                                'liveness', 'valence', 'tempo',
                                'mode', 'time_signature']]
    
    return features_df

if __name__ == "__main__":
    # Debug
    print(extract("https://open.spotify.com/playlist/0LCpnFsEdjhjPEZEFjGpgR?si=bab88565973048ba"))
    #df = extract("https://open.spotify.com/playlist/0LCpnFsEdjhjPEZEFjGpgR?si=bab88565973048ba")
    #df.to_csv("data/test_playlist.csv", index = False)