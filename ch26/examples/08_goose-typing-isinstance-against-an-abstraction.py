from collections.abc import Sized


class Playlist:
    def __init__(self, songs):
        self._songs = songs

    def __len__(self):
        return len(self._songs)


p = Playlist(["Song A", "Song B", "Song C"])
print(isinstance(p, Sized))
print(isinstance(p, list))
