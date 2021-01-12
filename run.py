import os

def run():
    # Search Spotify for random songs
    spotify_client = SpotifyClient(os.getenv('SPOTIFY_ATH_TOKEN'))
    random_tracks = spotify_client.get_random_tracks()
    track_ids = [track['id'] for track in random_tracks]
    
    # Once we get the list of random, add them to our library 

if __name__ == '__main__':
    run()