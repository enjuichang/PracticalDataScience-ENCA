import ijson
import os

from pathlib import Path
from conf import PLAYLISTDIR

def scan_playlists():
    current_path = Path.cwd()
    json_files = os.listdir(current_path / PLAYLISTDIR)
    uris = []
    for file in json_files:
        with open(current_path / PLAYLISTDIR / file, 'rb') as f:
            uris.append( ijson.items(f, 'playlists.item.tracks.item.track_uri') )

    return uris