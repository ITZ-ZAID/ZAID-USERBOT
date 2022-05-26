import spotipy
import spotipy.util as util
from spotipy import SpotifyException

from main import SPOTIFY_USERNAME, SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET

redirect_uri = "http://localhost:8888/callback"
scope = 'user-read-currently-playing app-remote-control'

async def now_playing():
    if [x for x in (SPOTIFY_USERNAME, SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET) if x is None]:
        return "API details not set"
    else:
        token = util.prompt_for_user_token(
            SPOTIFY_USERNAME, scope, SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, redirect_uri)
        spotify = spotipy.Spotify(auth=token)

    current_track = spotify.currently_playing()
    return current_track


async def list_devices():
    if [x for x in (SPOTIFY_USERNAME, SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET) if x is None]:
        return "API details not set"
    else:
        token = util.prompt_for_user_token(
            SPOTIFY_USERNAME, scope, SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, redirect_uri)
        spotify = spotipy.Spotify(auth=token)

    current_devices = spotify.devices()
    return current_devices


async def pause():
    if [x for x in (SPOTIFY_USERNAME, SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET) if x is None]:
        return "API details not set"
    else:
        token = util.prompt_for_user_token(
            SPOTIFY_USERNAME, scope, SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, redirect_uri)
        spotify = spotipy.Spotify(auth=token)

    try:
        spotify.pause_playback()
        return True
    except SpotifyException:
        return False


async def play():
    if [x for x in (SPOTIFY_USERNAME, SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET) if x is None]:
        return "API details not set"
    else:
        token = util.prompt_for_user_token(
            SPOTIFY_USERNAME, scope, SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, redirect_uri)
        spotify = spotipy.Spotify(auth=token)

    try:
        spotify.start_playback()
        return True
    except SpotifyException:
        return False
