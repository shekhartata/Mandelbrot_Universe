import spotipy
import requests
from spotipy.oauth2 import SpotifyOAuth


def get_track_audio_features(track_id, sp):
    try:
        features = sp.audio_features([track_id])
        return features
    except Exception as ex:
        print("Unable to fetch track features at this moment ..." + str(ex))


def get_track_features(list_tracks, sp):
    tracks_with_features = list()
    for track in list_tracks:
        audio_features = get_track_audio_features(track["id"], sp)
        if not audio_features:
            print("Skipping details for track %s" % track["name"])
            continue
        f = audio_features[0]
        tracks_with_features.append(dict(
            name=track['name'],
            id=track['id'],
            danceability=f['danceability'],
            energy=f['energy'],
            loudness=f['loudness'],
            speechiness=f['speechiness'],
            acousticness=f['acousticness'],
            tempo=f['tempo'],
            liveness=f['liveness'],
            valence=f['valence']
        ))
    return tracks_with_features


def get_all_liked_songs_list():
    """
    Returns list of saved tracks in User's liked playlist
    :return: type list
    """
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            redirect_uri="http://localhost:8000/controller/callback/",
            client_id="73ab81e228b842b58fb8f3d567522aa0",
            client_secret="f6dd237dd86c478dbd89d15df2b9cf18",
            scope="user-library-read user-library-modify playlist-modify-private "
                  "playlist-modify-public user-follow-read user-read-recently-played"
        )
    )
    print(sp.current_user())
    recent_tracks = list()
    trackList = sp.current_user_recently_played()
    for tracks in trackList["items"]:
        track_dict = dict()
        track_dict['name'] = tracks["track"]["name"]
        track_dict['id'] = tracks["track"]["id"]
        recent_tracks.append(track_dict)
    track_features = get_track_features(recent_tracks, sp)
    request_dict = {"recentTracks": track_features}
    requests.post(
        url="http://localhost:8000/controller/callback/", json=request_dict
    )


def main():
    print("Getting User's liked tracks")
    get_all_liked_songs_list()


if __name__ == '__main__':
    main()
